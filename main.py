import pandas as pd
import glob
from fpdf import FPDF
import pathlib
filepaths = glob.glob("invoices/*.xlsx")
# print(filepaths)

for item in filepaths:
    df = pd.read_excel(item, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filepath = pathlib.Path(item).stem
    invoice = filepath.split('-')[0]
    date = filepath.split('-')[1]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice}")
    pdf.ln()
    pdf.cell(w=50, h=8, txt=f"Date {date}")
    pdf.output(f"PDFs/{filepath}.pdf")
