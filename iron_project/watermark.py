from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import PyPDF2
# 讀要畫浮水印的檔
minutesFile = open('基於聊天機器人互動資訊之保險經紀人分組-論文(完稿).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(5)

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 120, "This is mine !!")
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# 讀浮水印檔
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
# 寫入
pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(minutesFirstPage)
print(pdfReader.numPages)
# 一頁一頁新增進去
for pageNum in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pageObj.mergePage(new_pdf.getPage(0))
    pdfWriter.addPage(pageObj)
    pdfWriter.encrypt('KYLE')
resultPdfFile = open('AddwatermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
