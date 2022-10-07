import os
import pandas as pd
import warnings
import re 
warnings.filterwarnings("ignore")

BASE_IRI = "http://openenergy-platform.org/ontology/oeo/"
if __name__ == '__main__':
    cwd = os.getcwd()
    df = pd.read_excel('src/scripts/etd/etd.xlsx')
    df = df.replace('\n', '<br>', regex=True)
    buffer = df.to_markdown(index=False)
    buffer = re.sub(r"(?s)(http:\/\/openenergy-platform.org\/ontology\/oeo\/?)\w+-\w+\/(\w+)(?=_)_(\d+?)(?=\s)", r"\2:\3", buffer)
    # There is a weird typo in surface azimuth angle ?
    buffer = re.sub(r"(?s)(http:\/\/opennergy-plattform.org\/ontology\/oeo\/?)\/(\w+)(?=_)_(\d+?)(?=\s)", r"\2:\3", buffer)
    # Remove the thing above when the typo is fixed 
    output =re.sub(r"(?s)(\w+?)(?=:):(\d+?)(?=\s)", r"[\1:\2]({}".format(BASE_IRI)+ r"\1_\2)", buffer)
    #df.to_markdown(buf=cwd + "/src/scripts/etd/ETD.md", index=False)
    with open(cwd + "/src/scripts/etd/ETD.md", "w") as fil:
        fil.write(output)