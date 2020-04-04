import requests
from bs4 import BeautifulSoup
# 設定要擷取的網站
url = "https://www.ptt.cc/bbs/beauty/index.html"

# 取的標籤
def save(img_urls, title):
    if img_urls:
        try:
            dname = title.strip()  # 用 strip() 去除字串前後的空白
            os.makedirs(dname)
            for img_url in img_urls:
                if img_url.split('//')[1].startswith('m.'):
                    img_url = img_url.replace('//m.', '//i.')
                if not img_url.split('//')[1].startswith('i.'):
                    img_url = img_url.split('//')[0] + '//i.' + img_url.split('//')[1]
                if not img_url.endswith('.jpg'):
                    img_url += '.jpg'
                fname = img_url.split('/')[-1]
                urllib.request.urlretrieve(img_url, os.path.join(dname, fname))
        except Exception as e:
            print(e)


def get_Content(url, res, page):
    rs = page.select('.r-ent')
    for item in rs:
        print('日期:', item.select('.date')[0].text)
        print('推文數:', item.select('.nrec')[0].text)
        print('作者:', item.select('.author')[0].text)
        print('標題:', item.select('.title')[0].text)
        print('=============Next===========')


articles = []
for page in range(0, 2):
    res = requests.get(url, cookies={'over18': '1'})
    page = BeautifulSoup(res.text, "html.parser")
    btn = page.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url = next_page_url
    get_Content(url=url, res=res, page=page)
