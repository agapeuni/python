
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver') #또는 chromedriver.exe
driver.implicitly_wait(5) # 묵시적 대기, 활성화를 최대 5초까지 기다린다.

# 페이지 가져오기(이동)
driver.get(url='https://www.google.com/')

# 요소 찾기 - 검색창찾고 키 전송

search_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('삼성전자')
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# 요소 찾기 - 지식백과에서 삼성전자 클릭
dic = driver.find_elements_by_xpath('//*[@id="wp_thbn_25"]')
dic[0].click()

time.sleep(2)
