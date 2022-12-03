# import PyPDF2

# pdfFileObj = open('sample1.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj=pdfReader.getPage(1)
# print(pageObj.extractText())
# pdfFileObj.close()

#importing required file obj
import PyPDF2
import re
pdfFileObj = open('sample1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
#creating a page object
pageObj=pdfReader.getPage(1)
#extracting text from page
data=(pageObj.extractText())
new=re.compile(r"boring")
search=(new.search(data))
print(search.group(0))
# closing the pdf file object
pdfFileObj.close()