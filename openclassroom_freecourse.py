import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import os
from datetime import datetime, timedelta, date
import dateutil
import dateutil.parser as parser
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import warnings
warnings.filterwarnings("ignore")

chromedriver = r'C:\Alaka\Internship Careervira\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)

df = pd.read_excel('withgoogle-trial5.xlsx')
map = pd.read_excel('google-redirect map.xlsx', index_col=None)

for k in map.index[30:41]:
    driver.get(map.at[k, 'Redirect Link'])
    print(k, map.at[k, 'Redirect Link'])
    print(k, map.at[k, 'Index'])
    time.sleep(3)

    try:
        what_will_learn = ""
        wwl = driver.find_element(By.XPATH, '/html/body/div[3]/main/article/div[3]/div/div/div/div[2]/div/section/div/div[1]/aside[1]/ul').find_elements(By.TAG_NAME, 'li')

        for i in wwl:
            what_will_learn = what_will_learn + i.get_attribute('textContent') + "|"

        if(len(what_will_learn)>1):
            what_will_learn = what_will_learn[:-1]

    except:
        try:
            wwl = driver.find_element(By.XPATH, '/html/body/div[3]/main/article/div[3]/div/div/div/div[2]/div/section/div/div[1]/aside[2]/ul').find_elements(By.TAG_NAME, 'li')

            for i in wwl:
                what_will_learn = what_will_learn + i.get_attribute('textContent') + "|"

            if(len(what_will_learn)>1):
                what_will_learn = what_will_learn[:-1]
        except:
            pass

    print(what_will_learn)

    df.at[map.at[k, 'Index'],'what_will_learn'] = what_will_learn

    try:
        content = ""
        modules = driver.find_elements(By.CLASS_NAME,'course-part-summary__section')
        #print(len(modules))
        content = ""
        for j in range(1,len(modules)+1):
            m = modules[j-1].find_element(By.TAG_NAME,'h3').get_attribute('textContent')
            m = re.sub("Part #[0-9]+ - ","", m)
            content = content + "<p><strong>Module " + str(j) + ": " + m + "</strong><br>"
            submodules = modules[j-1].find_element(By.TAG_NAME,'ol').find_elements(By.TAG_NAME,'li')
            #print(len(submodules))
            for b in range(1, len(submodules)+1):
                sm = submodules[b-1].get_attribute('textContent')
                content = content + sm + "<br>"
            content = content + "</p>"
        content = content.replace("\n","")
        print(content)
    except:
        pass

    df.at[map.at[k, 'Index'],'content_main_description'] = content

    try:
        instructor_name_1 = driver.find_elements(By.CLASS_NAME, 'course-bottom__subtitle')[0].get_attribute('textContent')
    except:
        instructor_name_1 = None
    try:
        instructor_name_2 = driver.find_elements(By.CLASS_NAME, 'course-bottom__subtitle')[1].get_attribute('textContent')
    except:
        instructor_name_2 = None
    try:
        instructor_bio_1 = driver.find_elements(By.CLASS_NAME, 'course-bottom__text-illustrated')[0].find_element(By.TAG_NAME, 'p').get_attribute('textContent').replace("\n","")
    except:
        instructor_bio_1 = None
    try:
        instructor_bio_2 = driver.find_elements(By.CLASS_NAME, 'course-bottom__text-illustrated')[1].find_element(By.TAG_NAME, 'p').get_attribute('textContent').replace("\n","")
    except:
        instructor_bio_2 = None
    try:
        instructor_image_1 = driver.find_elements(By.CLASS_NAME, 'course-bottom__text-illustrated')[0].find_element(By.TAG_NAME, 'span').get_attribute('style').replace('background-image: url("',"").replace('");',"")

    except:
        instructor_image_1 = None
    try:
        instructor_image_2 = driver.find_elements(By.CLASS_NAME, 'course-bottom__text-illustrated')[1].find_element(By.TAG_NAME, 'span').get_attribute('style').replace('background-image: url("',"").replace('");',"")
    except:
        instructor_image_2 = None

    print(instructor_name_1, instructor_name_2, instructor_bio_1, instructor_bio_2, "\n\n")
    print(instructor_image_1, instructor_image_2)
    df.at[map.at[k, 'Index'], 'instructor|1|name'] = instructor_name_1
    df.at[map.at[k, 'Index'], 'instructor|2|name'] = instructor_name_2
    df.at[map.at[k, 'Index'], 'instructor|1|bio'] = instructor_bio_1
    df.at[map.at[k, 'Index'], 'instructor|2|bio'] = instructor_bio_2
    df.at[map.at[k, 'Index'], 'instructor|1|instructor_image'] = instructor_image_1
    df.at[map.at[k, 'Index'], 'instructor|2|instructor_image'] = instructor_image_2

    print(df.iloc[map.at[k, 'Index']])

df.to_excel('withgoogle-trial6.xlsx', index=True)
