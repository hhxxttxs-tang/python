import glob
from fpdf import FPDF #

pngFiles = glob.glob('/Users/ezhou/Downloads/java_solution/98*.png')

for img in pngFiles:
    print "processing ", img
    pdf = FPDF()
    pdf.add_page()
    pdf.image(img)
    pdfFileName = img.replace('.png', '.pdf')
    pdf.output(pdfFileName, "F")
