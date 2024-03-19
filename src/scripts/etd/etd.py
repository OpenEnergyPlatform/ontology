import os
import pandas as pd
import warnings
import re 
import string
import pathlib
warnings.filterwarnings("ignore")
import sys

GLOSSARY_HEADER = """# Existing Terms and Definitions

"""
BASE_LINK_WIKI = "https://github.com/OpenEnergyPlatform/ontology/wiki/"
BASE_IRI = "http://openenergy-platform.org/ontology/oeo/"

if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) > 0:
        target_path = arguments[0]
    else:
        target_path = 'src/scripts/etd'
    cwd = os.getcwd()
    df = pd.read_excel(pathlib.Path(target_path).joinpath("etd.xlsx").as_posix())

    df = df.replace('\n', '<br>', regex=True)
    df = df.sort_values("LABEL", key=lambda col: col.str.strip().str.lower())
    # Create one table per letter:
    pathlib.Path(target_path).joinpath("glossary").mkdir(parents=True, exist_ok=True) 
    # header = GLOSSARY_HEADER + " ".join([f"[{letter}]({BASE_LINK_WIKI}{letter})" for letter in string.ascii_uppercase]) + "\n"

    # with open(cwd + "/src/scripts/etd/glossary/glossary.md", "w") as fil:
    #     fil.write(header)
    output = GLOSSARY_HEADER + "\n"
    for letter in string.ascii_lowercase:
        current_df = df[df["LABEL"].str.lower().str.startswith(letter)]
        if current_df.empty:
            continue
        buffer = current_df.to_markdown(index=False)
        buffer = re.sub(r"(?s)(http:\/\/openenergy-platform.org\/ontology\/oeo\/?)\w+-\w+\/(\w+)(?=_)_(\d+?)(?=\s)", r"\2:\3", buffer)
        # There is a weird typo in surface azimuth angle ?
        buffer = re.sub(r"(?s)(http:\/\/opennergy-plattform.org\/ontology\/oeo\/?)\/(\w+)(?=_)_(\d+?)(?=\s)", r"\2:\3", buffer)
        # Remove the thing above when the typo is fixed 
        buffer =re.sub(r"(?s)(\w+?)(?=:):(\d+?)(?=\s)", r"[\1:\2]({}".format(BASE_IRI)+ r"\1_\2)", buffer)
        title = f"## {letter.capitalize()}\n\n"
        table = title + buffer + "\n\n"
        #df.to_markdown(buf=cwd + "/src/scripts/etd/ETD.md", index=False)
        output += table
    with open(pathlib.Path(target_path).joinpath("glossary/glossary.md").as_posix(), "w") as fil:
        fil.write(output)

    # create csv output
    df_csv = df.copy()
    df_csv["ID"] = df_csv["ID"].str.replace("http://openenergy-platform.org/ontology/oeo/oeo-physical/", "")
    df_csv["ID"] = df_csv["ID"].str.replace("http://openenergy-platform.org/ontology/oeo/oeo-model/", "")
    df_csv["ID"] = df_csv["ID"].str.replace(":", "_")
    df_csv.to_csv(pathlib.Path(target_path).joinpath("glossary/glossary.csv").as_posix(), index=False)
