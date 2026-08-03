from fpdf import FPDF
import csv
from functions import generate_pdf_from_csv, generate_pdf_from_text, strip_extension
import time

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', style= 'B', size=20)
        self.cell(0, 20, "Generated Report", border=1, align="C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', style= 'B', size=10)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

#Opening lines of program
opener = "=" * 50 + "\n" +   "PDF GENERATOR PROGRAM".center(50)  + "\n" + "=" * 50 + "\nInput your filename, and the program will convert it to a PDF for you!"
print(opener)

time.sleep(2)


while True:
    user_response = input("\nWhat file do you need converted to a PDF? (etc..txt, csv)?")
    file_breakup = user_response.split('.')
    
    if file_breakup[-1] == "txt":
        cleanfilename = strip_extension(user_response)
        finished_file = generate_pdf_from_text(user_response, cleanfilename)
        time.sleep(1)
        if finished_file is not None:
            break
       
    elif file_breakup[-1] == "csv":
        cleanfilename = strip_extension(user_response)
        finished_file = generate_pdf_from_csv(user_response, cleanfilename)
        time.sleep(1)

    else:
        breakpoint
