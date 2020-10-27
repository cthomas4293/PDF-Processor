import PyPDF2

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

template = PyPDF2.PdfFileReader(open(f"{file1}", 'rb'))
watermark = PyPDF2.PdfFileReader(open(f"{file2}", 'rb'))
output = PyPDF2.PdfFileWriter()

for item in range(template.getNumPages()):
    page = template.getPage(item)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open("marked_page.pdf", 'wb') as doc:
    output.write(doc)