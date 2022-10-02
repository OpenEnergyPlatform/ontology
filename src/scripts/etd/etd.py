import os
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

if __name__ == '__main__':
    cwd = os.getcwd()
    df = pd.read_excel('etd.xlsx')
    df = df.replace('\n', '<br>', regex=True)
    df.to_markdown(buf=cwd + "/ETD.md", index=False)