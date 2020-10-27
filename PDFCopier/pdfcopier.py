import PyPDF2

import sys

file = sys.argv[1]

new_file = sys.argv[2]

# create a reader object
reader = PyPDF2.PdfFileReader(open(f"{file}", 'rb'))

# create a writer object
writer = PyPDF2.PdfFileWriter()

# user reader to get page/s
pages = reader.getPage(0)


# create a output variable and ad the page to the writer
# for later writing in context manager
new_pdf = writer.addPage(pages)

# using context mgr write file to new or existing file
# using writer to write the output file
with open(f"{new_file}", "wb") as cp:
	writer.write(cp)
