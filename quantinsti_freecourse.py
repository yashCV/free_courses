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

df = pd.read_excel('courses_quantra--new.xlsx', index_col=None)

for i in df.index:
    driver.get(df.at[i, 'partner_course_url'])
    print(i, df.at[i, 'partner_course_url'])
    time.sleep(3)

    features = driver.find_element(By.CLASS_NAME, 'course-feature-unit').find_element(By.CLASS_NAME, 'section-body').get_attribute('textContent')

    page_content = driver.find_element(By.CLASS_NAME, 'LayoutDefault__main').get_attribute('textContent')

    modules = driver.find_element(By.ID, 'syllabus-accordion').find_elements(By.CLASS_NAME, 'accordion-item')

    content = ""
    for j in range(1,len(modules)+1):
        content = content + "<p><strong>Module " + str(j) + ": " + modules[j-1].find_element(By.CLASS_NAME,'accordion-item-title-text').get_attribute('textContent') + "</strong><br>"
        submodules = modules[j-1].find_elements(By.CLASS_NAME,'unit-data__name')
        #print(len(submodules))
        for k in range(1, len(submodules)+1):
            sm = submodules[k-1].get_attribute('textContent')
            content = content + str(k) + ". " + sm + "<br>"
        content = content + "</p>"

    print(content)

    capstone_project = False
    if(" capstone" in page_content.lower()):
        capstone_project = True
    print("capstone_project: ", capstone_project)
    case_based_learning = False
    if " case stud" in page_content.lower() or " case based " in page_content.lower() or " case-based " in page_content.lower():
        case_based_learning = True
    print("case_based_learning: ", case_based_learning)

    learning_mediums = ""
    if " hands-on" in page_content.lower() or " hands on" in page_content.lower():
        learning_mediums += 'Hands-On Learning, '
    if case_based_learning:
        learning_mediums += 'Case Studies, '
    if "industry" in page_content.lower():
        learning_mediums += 'Industry Exposure, '
    if(len(learning_mediums)>1):
        learning_mediums = learning_mediums[:-2]
    print("learning_mediums: ", learning_mediums)

    prerequisites = driver.find_element(By.CLASS_NAME, 'prerequisites_text').get_attribute('textContent')
    print("prerequisites: ", prerequisites)

    availabilities = "Limited Access"
    if("lifetime access" in features.lower()):
        availabilities = "Lifetime Access"
    print("availabilities: ", availabilities)

    virtual_labs = False
    if(" lab" in features.lower()):
        virtual_labs = True
    print("virtual_labs: ", virtual_labs)

    job_assistance = False
    if(" job " in features.lower()):
        job_assistance = True
    print("job_assistance: ", job_assistance)

    df.at[i, 'content_main_description'] = content
    df.at[i, 'capstone_project'] = capstone_project
    df.at[i, 'case_based_learning'] = case_based_learning
    df.at[i, 'learning_mediums'] = learning_mediums
    df.at[i, 'prerequisites'] = prerequisites
    df.at[i, 'availabilities'] = availabilities
    df.at[i, 'virtual_labs'] = virtual_labs
    df.at[i, 'job_assistance'] = job_assistance

    print("\n\n")
df.to_excel("Quantinsti-updated.xlsx")
