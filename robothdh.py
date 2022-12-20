from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/s?k=self+help+books&sprefix=self+help+%2Caps%2C158&ref=nb_sb_ss_ts-doa-p_2_10')
time.sleep(5)

elements = driver.find_elements_by_xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]')

for element in elements:
    print(element.text)