import subprocess
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    subprocess.run(['say', text])