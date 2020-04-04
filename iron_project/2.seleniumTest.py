from selenium import webdriver
from selenium.webdriver.common.keys import Keys
brower = webdriver.Chrome('D:\\桌面專案\\python 相關\\Iron_30\\chromedriver')
brower.get('https://www.seleniumhq.org/')
# https://www.youtube.com/watch?v=GJjMjB3rkJM
# https://www.youtube.com/watch?v=bhYulVzYRng

elm = brower.find_element_by_link_text("Download")
print(elm.text)
elm.get_attribute('href')
print(elm.get_attribute)
elm.click()
elm = brower.find_element_by_link_text("Projects")
elm.click()
searchBar = brower.find_element_by_id("q")
searchBar.send_keys('download')
searchBar.send_keys([Keys.ENTER])
