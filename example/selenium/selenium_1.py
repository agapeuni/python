from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('window-size=1024,768')

browser = webdriver.Chrome('chromedriver', options=options)
browser.implicitly_wait(5)

browser.get(url='https://blog.naver.com/agapeuni')
browser.save_screenshot("example/selenium/WebSite.png")

browser.quit()
