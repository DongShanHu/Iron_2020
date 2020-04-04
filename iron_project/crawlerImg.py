import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json


PTT_URL = 'https://www.ptt.cc'


def get_web_page(url):
    time.sleep(0.7)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
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


folder_path = '..ㄈ/表特/'


def save(img_urls, title):
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
                img_url, os.path.join(dname, fname))
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
            time.sleep(0.1)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
        # 已取得文章列表，開始進入各文章讀圖
        for article in articles:
            print('Processing', article)
            page = get_web_page(PTT_URL + article['href'])
            if page:
                img_urls = parse(page)
                save(img_urls, article['title'])
                article['num_image'] = len(img_urls)

        # 儲存文章資訊
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2,
                      sort_keys=True, ensure_ascii=False)
