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

df = pd.read_excel('google-skillshop.xlsx', index_col=None)

for i in df.index:
    driver.get(df.at[i, 'partner_course_url'])
    print(i, df.at[i, 'partner_course_url'])
    time.sleep(3)

    page_content = driver.find_element(By.CLASS_NAME, 'coursepage__contentmain').get_attribute('textContent')

    capstone_project = False
    if("capstone" in page_content.lower()):
        capstone_project = True
    print(capstone_project)

    case_based_learning = False
    if " case stud" in page_content.lower() or " case based " in page_content.lower() or " case-based " in page_content.lower():
        case_based_learning = True
    print(case_based_learning)

    internship = False
    if(" internship" in page_content.lower()):
        internship = True
    print(internship)

    job_assistance = False
    if(" job " in page_content.lower()):
        job_assistance = True
    print(job_assistance)

    df.at[i, 'capstone_project'] = capstone_project
    df.at[i, 'case_based_learning'] = case_based_learning
    df.at[i, 'internship'] = internship
    df.at[i, 'job_assistance'] = job_assistance

    print("\n\n")
df.to_excel("google-skillshop-updated.xlsx")
