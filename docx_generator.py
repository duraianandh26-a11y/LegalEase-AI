from docx import Document
from io import BytesIO

def create_docx(content, title):

    doc = Document()

    doc.add_heading(title, level=1)

    doc.add_paragraph(content)

    buffer = BytesIO()

    doc.save(buffer)

    buffer.seek(0)

    return buffer