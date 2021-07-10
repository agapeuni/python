
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

delay_time = 2

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('window-size=1024,768')

browser = webdriver.Chrome('chromedriver', options=options)
browser.implicitly_wait(time_to_wait=5)

# 브라우저에서 URL을 호출한다.
browser.get(url='https://www.naver.com/')
sleep(delay_time)

# 입력항목에 검색어를 입력하고 엔터
search_box = browser.find_element_by_xpath(
    '/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input')
search_box.send_keys('주한길')
search_box.send_keys(Keys.RETURN)
sleep(delay_time)

# 상단에 VIEW 메뉴를 클릭
menu = browser.find_element_by_xpath(
    '/html/body/div[3]/div[1]/div/div[2]/div[1]/div/ul/li[2]/a')
menu.click()
sleep(delay_time)

# 첫번째 결과 클릭
link = browser.find_element_by_xpath(
    '/html/body/div[3]/div[2]/div/div[1]/section/div/div[2]/panel-list/div/more-contents/div/ul/li[1]/div[1]/div/a')
link.click()

sleep(delay_time)

browser.close()
