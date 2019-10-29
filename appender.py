from os import listdir
from PyPDF2 import PdfFileMerger


path = "/media/kudokun/General/Deep Learning/39. Neural Networks"
merger = PdfFileMerger()
for pdf in listdir(path):
    print(pdf)
    merger.append(path + "/" + pdf)
merger.write("result.pdf")
merger.close()
