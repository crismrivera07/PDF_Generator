from fpdf import FPDF
import csv
import time
import os 
from functions import generate_pdf_from_csv, generate_pdf_from_text, strip_extension


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

time.sleep(1)


while True:
    user_response = input("\nWhat file do you need converted to a PDF? (etc..txt, csv)?")
    file_breakup = user_response.split('.')
    
    if file_breakup[-1] == "txt":
        cleanfilename = strip_extension(user_response)
        finished_file = generate_pdf_from_text(user_response, cleanfilename)
        time.sleep(1)
        if finished_file is not None:
            another_file = input("Would you like another file generated? (y or n) ")
            if another_file.lower() == 'y':
                continue
            else:
                print("Good luck, see you next time!")
                break
       
    elif file_breakup[-1] == "csv":
        cleanfilename = strip_extension(user_response)
        finished_file = generate_pdf_from_csv(user_response, cleanfilename)
        time.sleep(1)
        if finished_file is not None:
            break
    else:
        another_response = input("Would you like to generate another file?(input y or n) ")
        user_last_response = input("Right now - Only .CSV & .TXT files are supported, if you do not have that file type, type 'E' to exit, or 'C' to try again! ")
        if user_last_response.lower() == 'c':
            continue
        else:
            print("Our apologies for not supporting that file, see you next time! ")
            


        

