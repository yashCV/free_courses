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

df = pd.read_excel('withgoogle-trial4.xlsx')
map = pd.read_excel('google-redirect map.xlsx', index_col=None)
#applieddigitalskills = ['https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/build-your-online-business/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/connect-and-collaborate-from-anywhere-with-digital-tools/overview.html?utm_source=website&utm_medium=partner&utm_campaign=20191107-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191107-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/digital-tools-for-everyday-tasks/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/edit-your-cv/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/effective-communications-at-work/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/give-and-receive-feedback/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/manage-a-project-with-digital-tools/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/negotiate-your-salary/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/plan-effective-meetings/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/prepare-for-your-business-plan/overview.html?utm_source=website&utm_medium=partner&utm_campaign=20191106-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191106-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/send-professional-emails/overview.html?utm_source=website&utm_medium=partner&utm_campaign=20191108-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191108-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/start-a-cv/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/use-google-to-get-a-new-job/overview.html?utm_source=&utm_medium=&utm_campaign=20191014-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191014-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/college-and-continuing-education-uk/en-uk/write-a-business-plan/overview.html?utm_source=website&utm_medium=partner&utm_campaign=20191108-Digital%20Garage/YouTube--cce-stu-00&src=partners-website-20191108-Digital%20Garage/YouTube--cce-stu-00', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/annotate-text-in-google-docs/overview.html?utm_source=partners&utm_medium=website&utm_campaign=202051-GwGEMEA-AnnotateText--ad-learn-&src=partners-website-202051-GwGEMEA-AnnotateText--ad-learn-', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/create-a-photo-journal-in-google-docs/overview.html?utm_source=partners&utm_medium=website&utm_campaign=202051-GwGEMEA-CreateaPhotoJournal--ad-learn-&src=partners-website-202051-GwGEMEA-CreateaPhotoJournal--ad-learn-', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/create-a-presentation-all-about-a-topic/overview.html', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/create-quizzes-in-google-forms/overview.html?utm_source=partners&utm_medium=website&utm_campaign=202051-GwGEMEA-CreateQuizzes--ad-learn-&src=partners-website-202051-GwGEMEA-CreateQuizzes--ad-learn-', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/organize-files-in-drive/overview.html?utm_source=partners&utm_medium=website&utm_campaign=202051-GwGEMEA-OrganiseFilesinDrive--ad-learn-&src=partners-website-202051-GwGEMEA-OrganiseFilesinDrive--ad-learn-', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/plan-and-budget/overview.html', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/research-and-develop-a-topic/overview.html?utm_source=partners&utm_medium=website&utm_campaign=202051-GwGEMEA-ResearchandDevelopaTopic--ad-learn-&src=partners-website-202051-GwGEMEA-ResearchandDevelopaTopic--ad-learn-', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school-uk/en-uk/track-due-dates-and-tasks-in-gmail/overview.html', 'https://applieddigitalskills.withgoogle.com/c/middle-and-high-school/en/manage-project-communication/overview.html?utm_source=partners&utm_medium=website&utm_campaign=5/5/20-GwGEMEA-ManageProjectCommunication--cce-stu-&src=partners-website-5/5/20-GwGEMEA-ManageProjectCommunication--cce-stu-']

for k in map.index[0:23]:
    driver.get(map.at[k, 'Redirect Link'])
    print(k, map.at[k, 'Redirect Link'])
    time.sleep(3)
    '''
    content = "<p>"

    mods = driver.find_elements(By.CLASS_NAME, 'lesson-card')

    for i in range(1, len(mods)+1):
        m = mods[i-1].find_element(By.CLASS_NAME, 'card-title').get_attribute('textContent')
        #print(m)
        if(m[1]=='.'):
            m = m[0] + ":" + m[2:]
        content = content + "<strong>Module " + m + "</strong><br>"
        submods = mods[i-1].find_elements(By.TAG_NAME, 'a')
        #print(len(submods))
        for j in range(1, len(submods)+1):
            sm = submods[j-1].get_attribute('textContent')
            for child in submods[j-1].find_elements(By.XPATH, "./*"):
                sm = sm.replace(child.get_attribute('textContent'), "");
            sm = re.sub("\s\s+"," ",sm)
            #print(sm)
            if(sm[0] == ' '):
                sm = sm[1:]
            if(sm[-1] == ' '):
                sm = sm[:-1]
            content = content + str(j) + ". " + sm + "<br>"
    content = content + "</p>"

    print(content, "\n\n")
    '''

    try:
        skills = ""
        s = driver.find_elements(By.CLASS_NAME, 'h-c-grid__col--6')[1]
        print(s.find_element(By.TAG_NAME, 'p').get_attribute('textContent'))
        ul = s.find_elements(By.TAG_NAME, 'li')
        print(len(ul))
        for i in ul:
            skills = skills + i.get_attribute('textContent') + "|"
        if(len(skills)>1):
            skills = skills[:-1]
    except:
        skills = None

    print(map.at[k, 'Index'], map.at[k, 'Google Link'])
    print(skills)
    df.at[map.at[k, 'Index'],'skills'] = skills

df.to_excel('withgoogle-trial5.xlsx')
