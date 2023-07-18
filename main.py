import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

#create a list of text filepaths
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}",ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date:{date}")



    pdf.output(f"PDFs/{filename}.pdf")

# #Create one PDF file
# pdf = FPDF(orientation="P", unit="mm", format="A4")
#
# #go through each texy file
# for filepath in filepaths:
#     #add a page to the PDF document for each text file
#     pdf.add_page()
#     #get the filenames without the extension
#     #and convert it to title case (e.g. Cat)
#     filename = Path(filepath).stem
#     name = filename.title()
#
#     pdf.cell(w=50, h=8, txt=name, ln=1)
#     pdf.set_font(family="Times", size=16, style="B")
#
# pdf.output("output.pdf")
