import pandas as pd
import glob
from subprocess import Popen, PIPE
from pathlib import Path
import json
# import pyhornedowl as ho
import re
HERMIT_JAR = "C:/Software/hermit/HermiT.jar"
JAVA_PATH = "java"
ONTOLOGY_PATH = "C:/Work/04_LOD/repositories/ontology/oeo-full.owl"
EXISTING_TERMS_AND_DEFINITONS = "C:/Work/04_LOD/repositories/ontology/src/scripts/etd/glossary/glossary.csv"
COMPETENCY_QUESTION_DIRECTORY = "C:/Work/04_LOD/repositories/ontology/tests/competency_questions"

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
    conclusion = Path(conclusion).as_posix()
    p = Popen([f"{JAVA_PATH}", "-jar", f"{HERMIT_JAR}", f"--premise=file:///{premise}",  f"--conclusion=file:///{conclusion}", "-E"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
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

def main():
    terms_and_definitions = pd.read_csv(EXISTING_TERMS_AND_DEFINITONS)
    is_covered = {k: {"covered": False, "by": []} for k in terms_and_definitions["ID"] if "OEO_" in k}

    competency_questions = {Path(cq).stem: {"path": cq , "covers": [], "passed":False, "error": ""} for cq in glob.glob(COMPETENCY_QUESTION_DIRECTORY + "/*omn")}
    all_covered = []
    for k, v in competency_questions.items():
        try:
            competency_questions[k]["passed"] = check_competency_question(v["path"] ,ONTOLOGY_PATH)
        except RuntimeError as e:
            competency_questions[k]["passed"] = False
            competency_questions[k]["error"] = str(e)
        terms = search_term_in_question_file(v["path"]) 
        for term in terms:
            if term in is_covered.keys():
                is_covered[term]["covered"] = True
                is_covered[term]["by"].append(k)
        v["covers"] = terms
        all_covered.extend(terms)
    
    all_covered = list(set(all_covered))

    coverage = sum([1 for c in is_covered.values() if c["covered"]]) / len(terms_and_definitions[terms_and_definitions["ID"].str.contains("OEO_")])

    with open("file.json", "w") as f:
        json.dump({"coverage": "{:.0%}".format(coverage), "questions": competency_questions, "terms": is_covered}, f, indent=4) 

if __name__=="__main__":
    main()
    # cq = "C:/Work/04_LOD/repositories/ontology/tests/competency_questions/q1.omn"
    # check_competency_question(cq ,ONTOLOGY_PATH)
    # terms = search_term_in_question_file(cq)
    # onto = ho.open_ontology(ONTOLOGY_PATH)

    # for a in onto.get_axioms():
    #     #Example: ['AnnotationAssertion', 'http://purl.obolibrary.org/obo/CHEBI_27732', 'http://www.geneontology.org/formats/oboInOwl#hasAlternativeId', 'CHEBI:41472']
    #     if len(a)==4 and a[0]=='AxiomKind::AnnotationAssertion':
    #         if "http://www.w3.org/2000/01/rdf-schema#label" in a[2].lower():
    #             print(a[1], a[3])