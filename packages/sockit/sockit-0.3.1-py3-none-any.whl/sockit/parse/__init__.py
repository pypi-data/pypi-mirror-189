"""
Parse Module

Parses skills, occupations, experience, and education from resumes
and skills and occupations from job postings.
"""

import chardet
import docx2txt
import time
from collections import defaultdict
from html2text import HTML2Text
from itertools import chain
from PyPDF2 import PdfReader
from sockit import title
from sockit.asciitrans import *
from sockit.data import get_lookup, get_soc_title, get_trie
from sockit.log import Log
from sockit.re import *
from sockit.skillvector import SkillVector

MIN_YEAR = 1940
MAX_YEAR = int(time.strftime("%Y"))


def _split_sentences(text):
    """
    Require at least two letters/numbers before a period
    to avoid splitting on acronyms/abbreviations.
    """
    return re_newline.sub("\\1\n", text.strip()).split("\n")


def _find_years(text):
    """
    Find all years that fall within the range [MIN_YEAR, MAX_YEAR].
    """
    return sorted(set(
        y for y in map(int, re_year.findall(text))
        if MIN_YEAR <= y and y <= MAX_YEAR
    ))


def _find_year_months(text):
    """
    Find all year-months, searching over multiple formats.
    """
    year_months = set()
    for pattern, formatter in re_year_month:
        year_months.update(map(formatter, pattern.findall(text)))
    return sorted(year_months)


def _clean(text):
    """
    Convert some puncuation to spaces, and return alpha-numeric
    characters, spaces and periods.
    """
    return re_alphanum.sub("", re_punct.sub(" ", text.lower())).strip()


def _decode_ascii(text):
    """
    Automatically detect the encoding of a byte string with chardet,
    decode the string, transliterate non-ASCII characters, and return
    an ASCII string.
    """
    detect = chardet.detect(text)
    encoding = detect["encoding"] if detect["confidence"] > 0.8 else "utf8"
    return text.decode(encoding, errors="ignore").translate(asciitrans)


def _pdf_bytes(filename):
    """
    Extract a byte string from a PDF document using the PyPDF library
    """
    reader = PdfReader(filename)
    num_pages = len(reader.pages)
    return bytes(" ".join([
        reader.pages[x].extract_text() for x in range(num_pages)
    ]), "utf8")


def _html_bytes(filename):
    """
    Extract a byte string from an HTML document using html2text
    """
    parser = HTML2Text()
    parser.ignore_links = True
    parser.ignore_anchors = True
    parser.ignore_images = True
    parser.ignore_emphasis = True
    parser.ignore_tables = True
    text = open(filename, "rb").read()
    return bytes(parser.handle(_decode_ascii(text)), "utf8")


def _extract(filename, extension=None):
    """
    Extract ASCII text from a PDF, doc, docx, or text file
    (based on the extension) and return as a list of lines.
    """
    if extension is None:
        extension = filename.rpartition(".")[2]
    if extension == "pdf":
        text = _pdf_bytes(filename)
    elif extension == "docx":
        text = docx2txt.process(filename).encode("utf8")
    elif extension == "htm" or extension == "html":
        text = _html_bytes(filename)
    else:
        if extension != "txt":
            Log(__name__, "_extract").warn(f"treating unknown file extension '{extension}' as text file")
        with open(filename, "rb") as f:
            text = f.read()
    return _decode_ascii(text).splitlines()


def _segment(lines):
    """
    Identify resume section headers and segment lines by section.
    """
    headers = get_lookup("resume_headers")
    segments = defaultdict(list)
    current = "contact"
    for line in lines:
        line = _clean(line)
        if line:
            # Test if the line begins with a one or two word section header
            header = line.replace(".", "").split()
            # Ignore lines with more than 2 words
            if len(header) > 2:
                header = []
            # Try two-word phrase first
            if len(header) > 1 and header[0] + " " + header[1] in headers:
                current = headers[header[0] + " " + header[1]]
                # Keep text that follows the header
                if len(header) > 2:
                    segments[current].append(header[2])
            # Try single words next
            elif header and header[0] in headers:
                current = headers[header[0]]
                # Keep text that follows the header
                if len(header) > 1:
                    segments[current].append(" ".join(header[1:]))
            # No header found
            else:
                segments[current].append(line)
    return segments


def _parse_contact(lines):
    """
    Parse the contact section for zipcodes.
    """
    zipcodes = []
    for line in lines:
        zipcodes += re_zipcode.findall(line)
    return {
        "Zipcode": zipcodes
    }


def _parse_education(lines):
    """
    Parse the education section for degrees, years, schools, and field of study.
    """
    degrees_trie = get_trie("degrees")
    schools_trie = get_trie("schools")
    fields_trie = get_trie("fields_of_study")

    matches = []
    for line in lines:
        matches.append({
            "degrees": degrees_trie.search(line),
            "years": _find_years(line),
            "schools":  schools_trie.search(re_alpha.sub("", line)),
            "fields_of_study" :  fields_trie.search(line)
        })
    # Guess at whether degrees precede years/school, in which case the
    # search for degrees should go in reverse
    if matches and matches[0]["degrees"]:
        matches = matches[::-1]
    # Coalesce sets of degree/year/school, assuming reverse chronological order
    results = []
    template = {"degree": None, "school": None, "years": [], "fields_of_study" : []}
    result = template.copy()
    for match in matches:
        if match["degrees"]:
            result["degree"] = max(match["degrees"])
        if match["fields_of_study"]:
            result["fields_of_study"] = max(match["fields_of_study"])
        if match["years"]:
            result["years"] = match["years"]
        if match["schools"]:
            result["school"] = match["schools"][0]
        if result["degree"]:
            results.insert(0, result)
            result = template.copy()
    return {
        "Education": results
    }


def _parse_experience(lines):
    """
    Parse the experience section for job titles and date ranges.
    """
    title_trie = get_trie("alternative_titles")
    matches = []
    for line in lines:
        line = line.replace(".", "")
        match = {
            "socs": title_trie.search(line, return_nodes=True),
            "years": _find_years(line),
            "dates": _find_year_months(line)
        }
        if ("present" in line or "current" in line) and ("presented" not in line):
            match["current"] = True
        matches.append(match)
    # Guess at whether job dates precede titles, in which case the
    # search for dates should go in reverse
    if matches and matches[0]["years"]:
        matches = matches[::-1]
    # Coalesce sets of SOCs/titles/years/dates
    results = []
    template = {"socs": [], "raw_titles": [], "titles": [], "years": [], "dates": [], "current": False}
    result = template.copy()
    for match in matches:
        if match["socs"]:
            result["socs"] = sum([x[1] for x in match["socs"]], start=[])
            result["raw_titles"] = [" ".join(x[0]) for x in match["socs"]]
            result["titles"] = [get_soc_title(soc) for soc in result["socs"]]
        if match["years"]:
            result["years"] = match["years"]
        if match["dates"]:
            result["dates"] = match["dates"]
        if match.get("current"):
            result["current"] = True
        if result["socs"] and result["years"]:
            results.insert(0, result)
            result = template.copy()
    return {
        "Experience": results
    }


def _parse_skills(experience_lines, skill_lines):
    """
    Parse the experience or skills section for RIPL-edited skills.
    """
    skills_trie = get_trie("skills")
    skills = []
    for line in chain(experience_lines, skill_lines):
        line = line.replace(".", "")
        skills += skills_trie.search(line)
    return {"Skills": skills}


def parse_resume(filename, extension=None):
    """
    Parse a resume file.
    """
    lines = _extract(filename, extension)
    segments = _segment(lines)
    results = {}

    if "contact" in segments:
        results.update(_parse_contact(segments["contact"]))

    if "education" in segments:
        results.update(_parse_education(segments["education"]))

    if "experience" in segments:
        results.update(_parse_experience(segments["experience"]))

    if "experience" in segments or "skills" in segments:
        results.update(_parse_skills(
            segments.get("experience", []),
            segments.get("skills", [])
        ))

    results['SkillVector'] = SkillVector(skill_list=results.get("Skills", []))

    # Find closest SOC
    results["Occupations"] = results["SkillVector"].rank_socs(n=10)

    return results


def parse_job_posting(filename, extension=None, prediction=False):
    """
    Parse a job posting description.
    """
    nonskills_trie = get_trie("nonskills")
    skills_trie = get_trie("skills")

    results = {
        "NonSkills": [],
        "Skills": {}
    }

    lines = _extract(filename, extension)
    if len(lines) == 1:
        lines = _split_sentences(lines[0])

    for line in lines:
        line = _clean(line.strip())
        nonskills = nonskills_trie.search(line)
        if nonskills:
            results["NonSkills"] += nonskills
        else:
            for skill in skills_trie.search(line):
                results["Skills"][skill] = results["Skills"].get(skill, 0) + 1

    results["NonSkills"] = list(sorted(set(results["NonSkills"])))
    results["SkillVector"] = SkillVector(skill_dictionary=results["Skills"])

    # Find closest SOC
    results["Occupations"] = results["SkillVector"].rank_socs(n=10)
    if prediction:
        results["PredictedOccupations"] = results["SkillVector"].predict_socs(n=3)

    return results
