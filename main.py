import tabula as tb
from PyPDF2 import PdfFileReader
import os

for i in range(1,5):
    if os.path.exists(f"data{i}"):
        os.remove(f"data{i}")

file = 'test.pdf'

pdf = PdfFileReader(open(file,'rb'))
print(pdf.getNumPages())


for i in range(1,(pdf.getNumPages()+1)):
    tb.convert_into(file,f"data{i}.csv",pages=i)
