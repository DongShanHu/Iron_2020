import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json
# 寄信相關套件
import smtplib
from email.mime.text import MIMEText

COMMASPACE = ', '


def send_mail_for_me(articles):
    # '利用 Gmail 的服務寄發通知信'
    send_gmail_user = '02130953@me.mcu.edu.tw'
    send_gmail_password = '0975375095'
    rece_gmail_user = 'ken83924@gmail.com'
    msg = MIMEText('您所追蹤的 訊息 已經出現在板上！文章：]')
    msg['Subject'] = 'PTT 監聽通知信'
    msg['From'] = send_gmail_user
    msg['To'] = rece_gmail_user
    print("寄信囉!!!!!")
    # 使用 SSL 加密 連線到 gmail 提供的 smtp
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(send_gmail_user, send_gmail_password)
    server.send_message(msg)
    server.quit()
 

PTT_URL = 'https://www.ptt.cc'


def get_web_page(url):
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html.parser')

    # 取得上一頁的連結
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []  # 儲存取得的文章資料
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        if d.find('div', 'date').string.strip() == date:  # 發文日期正確
            # 取得推文數
            push_count = 0
            if d.find('div', 'nrec').string:
                try:
                    push_count = int(d.find('div', 'nrec').string)  # 轉換字串為數字
                except ValueError:  # 若轉換失敗，不做任何事，push_count 保持為 0
                    pass

            # 取得文章連結及標題
            if d.find('a'):  # 有超連結，表示文章存在，未被刪除
                href = d.find('a')['href']
                title = d.find('a').string
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count
                })
    return articles, prev_url


def parse(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    links = soup.find(id='main-content').find_all('a')
    img_urls = []
    for link in links:
        if re.match(r'^https?://(i.)?(m.)?imgur.com', link['href']):
            img_urls.append(link['href'])
    return img_urls


folder_path = "D:/桌面專案/python 相關/Iron_30/表特/"


def save(img_urls, title, folder_path):
    if img_urls:
        try:
            dname = title.strip()  # 用 strip() 去除字串前後的空白
            os.makedirs(dname)
            for img_url in img_urls:
                if img_url.split('//')[1].startswith('m.'):
                    img_url = img_url.replace('//m.', '//i.')
                if not img_url.split('//')[1].startswith('i.'):
                    img_url = img_url.split(
                        '//')[0] + '//i.' + img_url.split('//')[1]
                if not img_url.endswith('.jpg'):
                    img_url += '.jpg'
                fname = img_url.split('/')[-1]

                urllib.request.urlretrieve(
                    img_url, os.path(folder_path).join(dname, fname))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    current_page = get_web_page(PTT_URL + '/bbs/Beauty/index.html')
    if current_page:
        articles = []  # 全部的今日文章
        # 今天日期, 去掉開頭的 '0' 以符合 PTT 網站格式
        date = time.strftime("%m/%d").lstrip('0')
        current_articles, prev_url = get_articles(
            current_page, date)  # 目前頁面的今日文章
        while current_articles:  # 若目前頁面有今日文章則加入 articles，並回到上一頁繼續尋找是否有今日文章
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, date)

        # 已取得文章列表，開始進入各文章讀圖
        for article in articles:
            print('Processing', article)
            page = get_web_page(PTT_URL + article['href'])
            if page:
                img_urls = parse(page)
                save(img_urls, ['titlearticle'], folder_path)
                article['num_image'] = len(img_urls)
        send_mail_for_me(articles)
    # 儲存文章資訊
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2,
                  sort_keys=True, ensure_ascii=False)
