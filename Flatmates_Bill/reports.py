import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as
    their names, their due amount and the period of the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image('files/house.png', w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=15)
        pdf.cell(w=100, h=40, txt=flatmate_1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate_1.pay(bill, flatmate_2), border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.set_font(family='Times', size=15)
        pdf.cell(w=100, h=40, txt=flatmate_2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate_2.pay(bill, flatmate_1), border=0)

        # Change directory to files, generate and open the PDF
        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)
