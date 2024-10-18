from PyPDF2 import PdfMerger

allpdf = ["1.pdf","2.pdf"]

pdf = PdfMerger()

for newpdf in allpdf:
    pdf.append(newpdf)

pdf.write("Najmul.pdf")
pdf.close()
