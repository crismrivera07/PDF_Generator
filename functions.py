import csv
from fpdf import FPDF
from pathlib import Path

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', style= 'B', size=20)
        self.cell(0, 20, "Generated Report", border=1, align="C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', style= 'B', size=10)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def generate_pdf_from_text(file, newfilename):
    try:
        with open(file) as f:
            text = f.read()
    except FileNotFoundError:
        print("Oops, that file does not exist, please try again! ")
        return 

    filename_break = file.split(".")
    filename = filename_break[0]
    folder = Path("/Users/crispy/PDF Reader/PDFs")
    folder.mkdir(exist_ok=True)
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('helvetica', style= '', size=10)
    pdf.multi_cell(0, 20, text, align="C")
    new_path = folder / f"{newfilename}.pdf"
    pdf.output(f"{new_path}") 
    print("\nHere is your text file, generated as a PDF file.")
    return True 

def generate_pdf_from_csv(csv_file, newfilename):
    try:
        with open(csv_file, newline='', encoding='utf-8-sig', mode='r') as f:
            data = list(csv.reader(f, delimiter=','))
    except FileNotFoundError:
        print("Oops, that file does not exist, pleas try again! ")
        return 

    folder = Path("/Users/crispy/PDF Reader/PDFs")
    folder.mkdir(exist_ok=True)
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('helvetica', style= 'I', size=10)
    with pdf.table() as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    new_path = folder / f"{newfilename}.pdf"
    pdf.output(f"{new_path}") 
    print("\nHere is your csv file, generated as a PDF file.")
    return True

def strip_extension(file):
    broken_up_filename = file.split('.')
    extension = broken_up_filename.pop(-1)
    return ".".join(broken_up_filename)
