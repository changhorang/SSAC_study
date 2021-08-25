from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
import time
import os

os.chdir(r'./Mini Project 1')

driver = webdriver.Chrome()
url ='https://www.naver.com/'
driver.get(url)
time.sleep(3)

word = '코로나 현황'
input_search = driver.find_elements_by_css_selector('input.input_text')[0]
input_search.send_keys(word)
input_search.submit()
time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="_cs_production_type"]/div/div[4]/div/div[1]/div/div/div/ul/li[1]/a').click()
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

cumulative_confirmed_cases = soup.select('div.inner_box > div.local_info')

cumulative_confirmed_data = []
for data in cumulative_confirmed_cases:
    area = data.select('strong')[0].text[:2].strip()
    population = data.select('p.population_number')[0].text.strip()
    cumulative_confirmed_data.append([area, population])


columns = ['Area', 'Population']

pd_cumulative_confirmed_data = pd.DataFrame(cumulative_confirmed_data, columns=columns)

pd_cumulative_confirmed_data.to_excel('./pd_cumulative_confirmed_data.xlsx', index = False)