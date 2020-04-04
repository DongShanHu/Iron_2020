
import os
import img2pdf
for f in os.listdir('圖片/'):
    print(f)
ary = []
ary.append(int(f.split('.jpg')[3]))
print(ary)
ary.sort()
li = []
for e in ary:
    li.append(f'圖片/{e}.jpg')
pdf_obj = img2pdf.convert(li)
with open('x.pdf', 'wb') as f:
    f.write(pdf_obj)
