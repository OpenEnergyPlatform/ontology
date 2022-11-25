from glob import glob
import pandas as pd
from subprocess import Popen, PIPE
from pathlib import Path
import json
import re
from pytest_harvest import saved_fixture
import pytest
import os
import shutil

CWD = os.getcwd()
with open(Path(CWD).joinpath("VERSION").as_posix()) as version_file:
    __version__ = version_file.readlines()[0].strip()

HERMIT_JAR = Path(CWD).joinpath("build/hermit.jar").as_posix()
JAVA_PATH = shutil.which("java")
ONTOLOGY_PATH = (
    Path(CWD)
    .joinpath("build/oeo")
    .joinpath(f"{__version__}")
    .joinpath("oeo-full.owl")
    .as_posix()
)
EXISTING_TERMS_AND_DEFINITONS = (
    Path(CWD).joinpath("build/oeo").joinpath(f"{__version__}").joinpath("glossary.csv")
)
COMPETENCY_QUESTION_DIRECTORY = Path(CWD).joinpath("tests/competency_questions")


@pytest.fixture
@saved_fixture
def existing_terms_and_definitons():
    """
    Fixture containing the final report
    """
    terms_and_definitions = pd.read_csv(EXISTING_TERMS_AND_DEFINITONS)
    return list(terms_and_definitions["ID"])


def pytest_generate_tests(metafunc):
    if "competency_question_path" in metafunc.fixturenames:
        competency_question_list = [
            p for p in glob(COMPETENCY_QUESTION_DIRECTORY.as_posix() + "*/**.omn")
        ]
        selected_filer = metafunc.config.getoption("--selected")
        competency_question_list = [
            cq for cq in competency_question_list if selected_filer in cq
        ]
        metafunc.parametrize("competency_question_path", competency_question_list)


def check_competency_question(conclusion, premise):
    """Check competency question against the given ontology

    Args:
        conclusion (str): A filepath to the competency question.
        premise (str): A filepath to the reference ontology.

    Raises:
        RuntimeError: If calling HermiT raises an error this will be raised as a RuntimeError.

    Returns:
        (boolean): Returns True if the competency question was sucessfully checked against the ontology.
    """
    conclusion = Path(conclusion).resolve().as_posix()
    p = Popen(
        [
            f"{JAVA_PATH}",
            "-jar",
            f"{HERMIT_JAR}",
            f"--premise=file:///{premise}",
            f"--conclusion=file:///{conclusion}",
            "-E",
        ],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(err) == 0:
        return eval(output.strip().capitalize())
    else:
        raise RuntimeError(f"{err}")


def search_term_in_question_file(question, pattern=r"\w+_\d{8}"):
    """Search all the Ontology terms in a specific competency question file

    Args:
        question (sts): Filepath to the competency question file
        pattern (regexp, optional): Regular expression of the terms to be searched. Defaults to r"\w+_\d{8}".

    Returns:
        list: List of all the terms covered by the CQ.
    """
    terms = []
    with open(question, "r") as question_file:
        for line in question_file.readlines():
            terms.extend(re.findall(pattern, line))
    return terms


def test_competency_question(
    competency_question_path, existing_terms_and_definitons, results_bag
):
    """Metatest to produce competency question tests."""
    results_bag.questions = {}
    results_bag.terms = {}
    name = Path(competency_question_path).stem
    failure = ""
    if not name in results_bag.questions:
        results_bag.questions[name] = {"passed": False, "covers": []}
    try:
        results_bag.questions[name]["passed"] = check_competency_question(
            competency_question_path, ONTOLOGY_PATH
        )
    except RuntimeError as e:
        results_bag.questions[name]["passed"] = False
        results_bag.questions[name]["error"] = str(e)
        failure = str(e)

    terms = search_term_in_question_file(competency_question_path)
    results_bag.questions[name]["covers"].extend(terms)
    results_bag.questions[name]["covers"] = list(
        set(results_bag.questions[name]["covers"])
    )
    for term in terms:
        if term in existing_terms_and_definitons:
            if not term in results_bag.terms:
                results_bag.terms[term] = {"covered": False, "by": []}
            results_bag.terms[term]["covered"] = True
            results_bag.terms[term]["by"].append(name)
    if len(failure) > 0:
        raise RuntimeError(failure)


def test_synthesis(fixture_store, existing_terms_and_definitons):
    """This test should run at the end. Produces the final report.

    Args:
        fixture_store (fixture): These are all the availible fixtures.
        existing_terms_and_definitons (fixture): Fixture with existing terms and definitions.
    """
    report = {"coverage": "0%", "questions": {}, "terms": {}}
    for v in fixture_store["results_bag"].values():
        report["questions"].update(v["questions"])
        for term in v["terms"].keys():
            if term in report["terms"]:
                report["terms"][term]["by"].extend(v["terms"][term]["by"])
                report["terms"][term]["by"] = list(set(report["terms"][term]["by"]))
                report["terms"][term]["by"] = list(set(report["terms"][term]["by"]))
            else:
                report["terms"][term] = {
                    "covered": v["terms"][term]["covered"],
                    "by": v["terms"][term]["by"],
                }

    coverage = sum([1 for c in report.get("terms", {}).values() if c["covered"]]) / len(
        [term for term in existing_terms_and_definitons if "OEO_" in term]
    )
    report["coverage"] = "{:.0%}".format(coverage)
    with open(Path(CWD).joinpath("build/report.json"), "w") as f:
        json.dump(report, f, indent=4)
