from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

input_path = 'D:/UserArea/J0134661/Desktop/便利機能/translate/RBJPE5518_Honda_Kei-Car_PLS_control_20220114.pdf'
output_path = 'D:/UserArea/J0134661/Desktop/便利機能/translate/result.txt'

manager = PDFResourceManager()

with open(output_path, "wb") as output:
    with open(input_path, 'rb') as input:
        with TextConverter(manager, output, codec='utf-8', laparams=LAParams()) as conv:
            interpreter = PDFPageInterpreter(manager, conv)
            for page in PDFPage.get_pages(input):
                interpreter.process_page(page)
 

