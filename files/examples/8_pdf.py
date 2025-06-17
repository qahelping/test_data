from PyPDF2 import PdfReader

from files.files import PDF_FILE_PATH


reader = PdfReader(PDF_FILE_PATH)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)