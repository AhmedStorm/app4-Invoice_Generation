import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for item in filepaths:
    df = pd.read_excel(item,sheet_name="Sheet 1")
    print(df)