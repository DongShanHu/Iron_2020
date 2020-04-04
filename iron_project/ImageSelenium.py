import time, os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import img2pdf
import os

driver = webdriver.Chrome('chromedriver')

for s in range(952, 953):
    if not os.path.exists(str(s)):
        os.mkdir(str(s))
    pageurl = 'https://www.8899.click/online/comic-103.html?ch={}-{}'
    driver.get(pageurl.format(s,1))
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pagenum = int(soup.select_one('#pagenum').text.split('/')[1].strip('頁')) 
    for i in range(pagenum):
        driver.get(pageurl.format(s, i+1))
        soup = BeautifulSoup(driver.page_source, 'lxml')
        imgurl = 'https:' + soup.select_one('#TheImg').get('src')
        res = requests.get(imgurl)
        with open('{}/{}.jpg'.format(s, i+ 1), 'wb') as f:
            f.write(res.content)
        time.sleep(1)
        for f in os.listdir('952/'):
    print(f)
    li = []
for e in ary:
    li.append(f'952/{e}.jpg')
    pdf_obj = img2pdf.convert(li)
    with open('952.pdf', 'wb') as f:
    f.write(pdf_obj)