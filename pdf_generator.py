from fpdf import FPDF
from io import BytesIO

def create_pdf(content, title):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 16)

    pdf.cell(200, 10, title, ln=True)

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 8, content)

    data = pdf.output(dest="S")

    buffer = BytesIO(data)

    return buffer