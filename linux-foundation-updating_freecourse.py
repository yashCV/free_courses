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

df = pd.read_excel('Linux Foundation.xlsx', index_col=None)

for i in df.index:
    driver.get(df.at[i, 'partner_course_url'])
    print(i, df.at[i, 'partner_course_url'])
    time.sleep(3)

    page_content = driver.find_element(By.CLASS_NAME, 'main-content').get_attribute('textContent')

    capstone_project = False
    if(" capstone" in page_content.lower()):
        capstone_project = True
    print("capstone_project: ", capstone_project)
    case_based_learning = False
    if " case stud" in page_content.lower() or " case based " in page_content.lower() or " case-based " in page_content.lower():
        case_based_learning = True
    print("case_based_learning: ", case_based_learning)

    try:
        pricing_type = "Free"
        features = driver.find_element(By.CLASS_NAME, 'lf_pdp_fundamentals-includes-content').get_attribute('textContent')
        if("audit" in features.lower()):
            pricing_type = "Audit"
    except:
        pass

    print("pricing_type: ", pricing_type)
    review_name_1 = review_date_1 = review_1 = review_name_2 = review_date_2 = review_2 = None

    try:
        reviews = driver.find_elements(By.CLASS_NAME, 'lf_pdp_fundamentals-testimonials-comments-comment')
        review_name_1 = reviews[0].find_element(By.CLASS_NAME, 'lf_pdp_fundamentals-testimonials-comments-comment-left-name').get_attribute('textContent')
        review_date_1 = reviews[0].find_element(By.CLASS_NAME, 'lf_pdp_fundamentals-testimonials-comments-comment-left-date').get_attribute('textContent')
        review_1 = reviews[0].find_element(By.CLASS_NAME, 'lf_pdp_fundamentals-testimonials-comments-comment-content').get_attribute('textContent').strip()
        print("reviewer_name_1", review_name_1)
        print("review_date_1", review_date_1)
        print("review_1", review_1)

        review_name_2 = reviews[1].find_element(By.CLASS_NAME, 'lf_pdp_fundamentals-testimonials-comments-comment-left-name').get_attribute('textContent')
        review_date_2 = reviews[1].find_element(By.CLASS_NAME, 'lf_pdp_fundamentals-testimonials-comments-comment-left-date').get_attribute('textContent')
        review_2 = reviews[1].find_element(By.CLASS_NAME, 'lf_pdp_fundamentals-testimonials-comments-comment-content').get_attribute('textContent').strip()
        print("reviewer_name_2", review_name_2)
        print("review_date_2", review_date_2)
        print("review_2", review_2)

    except:
        print("No reviews")

    df.at[i, 'capstone_project'] = capstone_project
    df.at[i, 'case_based_learning'] = case_based_learning
    df.at[i, 'pricing_type'] = pricing_type
    df.at[i, 'review|1|reviewer_name'] = review_name_1
    df.at[i, 'review|1|review_date'] = review_date_1
    df.at[i, 'review|1|review'] = review_1
    df.at[i, 'review|2|reviewer_name'] = review_name_2
    df.at[i, 'review|2|review_date'] = review_date_2
    df.at[i, 'review|2|review'] = review_2

    print("\n\n")
df.to_excel("Linux Foundation-updated.xlsx")
