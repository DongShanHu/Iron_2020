from selenium import webdriver
from bs4 import BeautifulSoup

# chromedriver.exe執行檔所存在的路徑
brower = webdriver.Chrome("chromedriver.exe")
# 打開瀏覽器進入指定頁面
brower.get('https://www.ptt.cc/bbs/Beauty/index.html')
num_page = int(input("請問您想擷取幾頁？"))

info = []
while(num_page > 0):
    print("===============新頁面===============")
    # 取得當前的網址
    current_url = brower.current_url
    # 瀏覽器轉跳至當前的網址
    brower.get(current_url)
    html = brower.page_source
    # 讀進soup中
    soup = BeautifulSoup(html, "html.parser")
    container = soup.select('.r-ent')
    for item in container:
        print('日期:', item.select('.date')[0].text)
        print('推文數:', item.select('.nrec')[0].text)
        print('作者:', item.select('.author')[0].text)
        print('標題:', item.select('.title')[0].text)
        info.append("日期："+item.select('div.date')[0].text+"作者："+item.select(
            'div.author')[0].text+"標題："+item.select('div.title')[0].text + "推文數："+item.select('div.nrec')[0].text)
        print('=============Next===========')
    num_page = num_page-1

    # 這裡跟剛剛不一樣可以用selenium效果來做
    # 按頁面上的"‹ 上頁"link
    brower.find_element_by_link_text("‹ 上頁").click()
brower.close()  # 關閉瀏覽器
