import pandas as pd
import glob
from fpdf import FPDF
import pathlib

filepaths = glob.glob("invoices/*.xlsx")

for item in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filepath = pathlib.Path(item).stem
    invoice, date = filepath.split('-')
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)
    pdf.ln(5)
    df = pd.read_excel(item, sheet_name="Sheet 1")
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    # Add Headers of the table
    pdf.set_font(family="Times", size=10, style="B")
    we = [30, 60, 40, 30, 20]
    for i, col in enumerate(columns):
        pdf.cell(w=we[i], h=8, txt=col, border=1)
    pdf.ln()
    # Add the content of the table
    pdf.set_font(family="Times", size=10)
    for index, row in df.iterrows():
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=20, h=8, txt=str(row["total_price"]), border=1, ln=1)
    total_sum = df["total_price"].sum()
    aq = ["", "", "", "", str(total_sum)]
    for i, it in enumerate(aq):
        pdf.cell(w=we[i], h=8, txt=it, border=1)

    pdf.ln(10)
    pdf.set_text_color(40,40, 40)
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=25, h=8, txt=f"The total Price is {total_sum}", ln=1)
    pdf.cell(w=35, h=8, txt=f"PythonHow")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filepath}.pdf")
