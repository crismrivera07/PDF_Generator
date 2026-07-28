from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', style= 'B', size=20)
        self.cell(0, 20, "Generated Report", border=1, align="C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', style= 'B', size=10)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def generate_pdf_from_text(file):
    with open(file) as f:
        text = f.read()

    filename_break = file.split(".")
    filename = filename_break[0]
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('helvetica', style= '', size=10)
    pdf.multi_cell(0, 20, text, align="C")
    pdf.output(f"{filename}.pdf")
    return file

print(generate_pdf_from_text("text_file.txt"))




