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

'''
#Extract all category URLs
driver.get('https://www.simplilearn.com/skillup/skillup-free-online-courses#Data-Science-&-Business-Analytics')

div = driver.find_element(By.XPATH, '//*[@id="exploreCourseDesktop"]/div/div/div[1]/div')

a = div.find_elements(By.TAG_NAME, 'a')

lis = []

for i in a:
    lis.append(i.get_attribute('href'))

print(lis)
'''
'''
#Extract all course URLs

lis = ['https://www.simplilearn.com/skillup/skillup-free-online-courses#Data-Science-&-Business-Analytics', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Cyber-Security', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#AI-&-Machine-Learning', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Software-Development', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Digital-Marketing', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#DevOps', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Cloud-Computing', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Big-Data', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Project-Management', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Agile-and-Scrum', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Quality-Management', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#Business-and-Leadership', 'https://www.simplilearn.com/skillup/skillup-free-online-courses#IT-Service-and-Architecture']

course_lis = []

for i in lis:
    driver.get(i)
    driver.refresh()
    time.sleep(5)
    j=1

    while(True):
        try:
            print(driver.find_element(By.XPATH, '//*[@id="exam-certification"]/li/div[2]/div[{}]/a'.format(j)).get_attribute('href'))
            course_lis.append(driver.find_element(By.XPATH, '//*[@id="exam-certification"]/li/div[2]/div[{}]/a'.format(j)).get_attribute('href'))
            j+=1
        except:
            break

print("\n\n", course_lis)

'''

lis = ['https://www.simplilearn.com/learn-business-analytics-excel-fundamentals-skillup', 'https://www.simplilearn.com/getting-started-data-science-with-python-skillup', 'https://www.simplilearn.com/learn-data-analytics-for-beginners-skillup', 'https://www.simplilearn.com/learn-data-science-with-r-basics-skillup', 'https://www.simplilearn.com/learn-power-bi-basics-free-course-skillup', 'https://www.simplilearn.com/learn-tableau-online-free-course-skillup', 'https://www.simplilearn.com/learn-ms-excel-free-training-course-skillup', 'https://www.simplilearn.com/data-science-free-course-for-beginners-skillup', 'https://www.simplilearn.com/learn-python-libraries-free-course-skillup', 'https://www.simplilearn.com/free-business-intelligence-course-online-skillup', 'https://www.simplilearn.com/free-data-visualization-course-online-skillup', 'https://www.simplilearn.com/introduction-to-excel-dashboard-for-beginners-skillup', 'https://www.simplilearn.com/learn-ethical-hacking-online-free-course-skillup', 'https://www.simplilearn.com/learn-cyber-security-basics-skillup', 'https://www.simplilearn.com/learn-cloud-security-basics-skillup', 'https://www.simplilearn.com/introduction-to-information-security-basics-skillup', 'https://www.simplilearn.com/free-cybercrime-course-for-beginners-skillup', 'https://www.simplilearn.com/learn-cissp-security-assessment-testing-operations-skillup', 'https://www.simplilearn.com/learn-cryptography-basics-free-skillup-course', 'https://www.simplilearn.com/learn-machine-learning-basics-skillup', 'https://www.simplilearn.com/learn-ai-basics-skillup', 'https://www.simplilearn.com/introduction-to-deep-learning-free-course-skillup', 'https://www.simplilearn.com/learn-machine-learning-algorithms-free-course-skillup', 'https://www.simplilearn.com/neural-network-training-from-scratch-free-course-skillup', 'https://www.simplilearn.com/learn-tensorflow-basics-free-course-skillup', 'https://www.simplilearn.com/free-course-on-machine-learning-with-r-skillup', 'https://www.simplilearn.com/introduction-to-image-recognition-basics-skillup', 'https://www.simplilearn.com/introduction-to-supervised-unsupervised-learning-for-beginners-skillup', 'https://www.simplilearn.com/learn-keras-for-beginners-free-course-skillup', 'https://www.simplilearn.com/learn-basics-of-natural-language-processing-free-course-skillup', 'https://www.simplilearn.com/advanced-c-plus-plus-course-skillup', 'https://www.simplilearn.com/free-android-app-development-course-skillup', 'https://www.simplilearn.com/free-flutter-foundation-course-skillup', 'https://www.simplilearn.com/free-opencv-training-course-skillup', 'https://www.simplilearn.com/learn-java-basics-skillup', 'https://www.simplilearn.com/learn-python-basics-free-course-skillup', 'https://www.simplilearn.com/learn-blockchain-basics-skillup', 'https://www.simplilearn.com/free-online-course-to-learn-sql-basics-skillup', 'https://www.simplilearn.com/learn-iot-basics-skillup', 'https://www.simplilearn.com/learn-javascript-basics-free-course-skillup', 'https://www.simplilearn.com/learn-rpa-basics-skillup', 'https://www.simplilearn.com/learn-react-js-basics-free-course-skillup', 'https://www.simplilearn.com/learn-salesforce-basics-skillup', 'https://www.simplilearn.com/learn-salesforce-admin-basics-skillup', 'https://www.simplilearn.com/learn-salesforce-developer-basics-skillup', 'https://www.simplilearn.com/free-online-full-stack-development-course-skillup', 'https://www.simplilearn.com/r-programming-free-course-skillup', 'https://www.simplilearn.com/free-python-programming-course-skillup', 'https://www.simplilearn.com/learn-angular-basics-free-course-skillup', 'https://www.simplilearn.com/learn-numpy-basics-free-course-skillup', 'https://www.simplilearn.com/learn-nodejs-basics-free-course-skillup', 'https://www.simplilearn.com/free-course-to-learn-cpp-basics-skillup', 'https://www.simplilearn.com/free-html-course-for-beginners-skillup', 'https://www.simplilearn.com/learn-junit-basics-free-course-skillup', 'https://www.simplilearn.com/introduction-to-java-spring-framework-fundamentals-skillup', 'https://www.simplilearn.com/free-full-stack-java-developer-course-skillup', 'https://www.simplilearn.com/introduction-to-java-servlets-jsp-basics-skillup', 'https://www.simplilearn.com/learn-java-hibernate-basics-skillup', 'https://www.simplilearn.com/cryptocurrency-for-beginners-free-course-skillup', 'https://www.simplilearn.com/front-end-developer-free-course-skillup', 'https://www.simplilearn.com/basics-of-automation-anywhere-free-course-skillup', 'https://www.simplilearn.com/learn-css-basics-free-training-course-skillup', 'https://www.simplilearn.com/introduction-to-basics-of-time-series-analysis-skillup', 'https://www.simplilearn.com/if-else-statements-loops-in-python-free-course-skillup', 'https://www.simplilearn.com/learn-php-basics-free-course-skillup', 'https://www.simplilearn.com/sorting-algorithms-in-data-structure-free-course-skillup', 'https://www.simplilearn.com/learn-basics-of-web-scraping-in-python-free-course-skillup', 'https://www.simplilearn.com/learn-basics-of-reactjs-components-free-course-skillup', 'https://www.simplilearn.com/python-opencv-basics-free-course-skillup', 'https://www.simplilearn.com/learn-basics-of-databases-free-course-skillup', 'https://www.simplilearn.com/affiliate-marketing-for-beginners-course-skillup', 'https://www.simplilearn.com/free-saas-business-fundamental-course-skillup', 'https://www.simplilearn.com/learn-digital-marketing-fundamentals-basics-skillup', 'https://www.simplilearn.com/learn-seo-basics-skillup', 'https://www.simplilearn.com/learn-social-media-basics-skillup', 'https://www.simplilearn.com/free-content-marketing-training-course-skillup', 'https://www.simplilearn.com/free-youtube-and-video-marketing-training-course-skillup', 'https://www.simplilearn.com/learn-advanced-ppc-advertising-skillup', 'https://www.simplilearn.com/free-facebook-marketing-and-advertising-training-course-skillup', 'https://www.simplilearn.com/learn-digital-marketing-basics-for-entrepreneurs-cxos-skillup', 'https://www.simplilearn.com/free-digital-marketing-strategy-training-course-skillup', 'https://www.simplilearn.com/learn-google-ads-fundamentals-free-course-skillup', 'https://www.simplilearn.com/learn-email-marketing-free-course-skillup', 'https://www.simplilearn.com/learn-mobile-marketing-free-training-course-skillup', 'https://www.simplilearn.com/learn-digital-social-selling-basics-skillup', 'https://www.simplilearn.com/introduction-to-learn-social-media-free-course-skillup', 'https://www.simplilearn.com/learn-instagram-marketing-free-course-skillup', 'https://www.simplilearn.com/digital-marketing-tools-techniques-free-online-course-skillup', 'https://www.simplilearn.com/free-web-analytics-training-course-skillup', 'https://www.simplilearn.com/learn-conversion-rate-optimization-free-course-skillup', 'https://www.simplilearn.com/free-google-analytics-training-course-for-beginners-skillup', 'https://www.simplilearn.com/free-marketing-automation-training-course-skillup', 'https://www.simplilearn.com/learn-ppc-basics-free-course-skillup', 'https://www.simplilearn.com/free-hootsuite-training-course-skillup', 'https://www.simplilearn.com/learn-twitter-marketing-basics-free-course-skillup', 'https://www.simplilearn.com/free-linkedin-marketing-course-skillup', 'https://www.simplilearn.com/free-snapchat-marketing-course-skillup', 'https://www.simplilearn.com/learn-fundamentals-of-influencer-marketing-and-orm-free-course-skillup', 'https://www.simplilearn.com/learn-pinterest-marketing-basics-free-course-skillup', 'https://www.simplilearn.com/learn-sms-marketing-app-marketing-free-course-skillup', 'https://www.simplilearn.com/learn-basics-of-paid-media-marketing-free-course-skillup', 'https://www.simplilearn.com/learn-git-basics-skillup', 'https://www.simplilearn.com/learn-selenium-basics-free-course-skillup', 'https://www.simplilearn.com/learn-kubernetes-basics-free-course-skillup', 'https://www.simplilearn.com/learn-docker-basics-free-course-skillup', 'https://www.simplilearn.com/learn-jenkins-basics-free-course-skillup', 'https://www.simplilearn.com/learn-ansible-basics-free-course-skillup', 'https://www.simplilearn.com/devops-tools-free-course-skillup', 'https://www.simplilearn.com/free-ci-cd-online-training-course-skillup', 'https://www.simplilearn.com/free-apache-maven-training-course-online-skillup', 'https://www.simplilearn.com/free-course-to-learn-puppet-basics-skillup', 'https://www.simplilearn.com/chef-in-devops-basics-free-course-skillup', 'https://www.simplilearn.com/learn-devops-basics-skillup', 'https://www.simplilearn.com/free-azure-fundamental-course-skillup', 'https://www.simplilearn.com/free-azure-303-course-skillup', 'https://www.simplilearn.com/learn-azure-basics-free-course-skillup', 'https://www.simplilearn.com/introduction-to-cloud-computing-basics-skillup', 'https://www.simplilearn.com/learn-aws-basics-free-training-course-skillup', 'https://www.simplilearn.com/learn-google-cloud-platform-fundamentals-free-course-skillup', 'https://www.simplilearn.com/learn-aws-services-basics-free-course-skillup', 'https://www.simplilearn.com/learn-azure-services-basics-free-course-skillup', 'https://www.simplilearn.com/free-azure-304-course-skillup', 'https://www.simplilearn.com/learn-hadoop-spark-basics-skillup', 'https://www.simplilearn.com/learn-mongodb-basics-skillup', 'https://www.simplilearn.com/introduction-to-hadoop-free-course-skillup', 'https://www.simplilearn.com/learn-apache-spark-basics-free-course-skillup', 'https://www.simplilearn.com/indexing-and-aggregation-in-mongo-db-free-course-skillup', 'https://www.simplilearn.com/learn-crud-operations-in-mongodb-free-course-skillup', 'https://www.simplilearn.com/learn-pyspark-free-course-skillup', 'https://www.simplilearn.com/learn-basics-of-data-analytics-with-spark-free-course-skillup', 'https://www.simplilearn.com/learn-basics-of-hadoop-components-free-beginners-course-skillup', 'https://www.simplilearn.com/big-data-tools-free-course-online-skillup', 'https://www.simplilearn.com/learn-project-management-fundamentals-skillup', 'https://www.simplilearn.com/capm-basics-skillup', 'https://www.simplilearn.com/free-online-pmp-course-for-beginners-skillup', 'https://www.simplilearn.com/learn-agile-scrum-foundations-basics-skillup', 'https://www.simplilearn.com/agile-scrum-master-basics-skillup', 'https://www.simplilearn.com/pmi-acp-basics-skillup', 'https://www.simplilearn.com/introduction-to-lean-management-basics-skillup', 'https://www.simplilearn.com/learn-minitab-basics-online-free-course-skillup', 'https://www.simplilearn.com/learn-six-sigma-basics-free-course-skillup', 'https://www.simplilearn.com/free-digital-transformation-training-course-skillup', 'https://www.simplilearn.com/learn-ccba-basics-skillup', 'https://www.simplilearn.com/cbap-basics-skillup', 'https://www.simplilearn.com/introduction-to-business-analysis-free-course-skillup', 'https://www.simplilearn.com/learn-design-thinking-basics-free-course-skillup', 'https://www.simplilearn.com/introduction-to-digital-leadership-skillup', 'https://www.simplilearn.com/introduction-to-digital-disruption-transformation-strategy-skillup', 'https://www.simplilearn.com/interview-preparation-free-course-skillup', 'https://www.simplilearn.com/togaf-foundations-skillup']

print(len(lis)) #150
print(len(set(lis))) #150

df = pd.DataFrame(columns=['title', 'learn_type', 'topics', 'skills', 'description', 'cover_image', 'cover_video', 'embedded_video_url', 'delivery_method', 'instruction_type', 'content_main_description', 'content_module|1|heading', 'content_module|1|subheading_1', 'content_module|1|subheading_2', 'content_module|2|heading', 'content_module|2|subheading_1', 'content_module|2|subheading_2', 'what_will_learn', 'prerequisites', 'target_students', 'instructor|1|name', 'instructor|1|designation', 'instructor|1|instructor_bio', 'instructor|1|linkedin_url', 'instructor|1|facebook_url', 'instructor|1|twitter_url', 'instructor|1|instructor_image', 'instructor|2|name', 'instructor|2|designation', 'instructor|2|instructor_bio', 'instructor|2|linkedin_url', 'instructor|2|facebook_url', 'instructor|2|twitter_url', 'instructor|2|instructor_image', 'instructor|3|name', 'instructor|3|designation', 'instructor|3|instructor_bio', 'instructor|3|linkedin_url', 'instructor|3|facebook_url', 'instructor|3|twitter_url', 'instructor|3|instructor_image', 'instructor|4|name', 'instructor|4|designation', 'instructor|4|instructor_bio', 'instructor|4|linkedin_url', 'instructor|4|facebook_url', 'instructor|4|twitter_url', 'instructor|4|instructor_image', 'review|1|reviewer_name', 'review|1|photo', 'review|1|review_date', 'review|1|review', 'review|1|rating', 'review|2|reviewer_name', 'review|2|photo', 'review|2|review_date', 'review|2|review', 'review|2|rating', 'total_duration', 'total_duration_unit', 'total_video_content', 'total_video_content_unit', 'recommended_effort_per_week', 'avg_session_duration_with_instructor', 'level', 'languages', 'short_description', 'subtitle_languages', 'accessibilities', 'availabilities', 'Display Price', 'pricing_type', 'currency', 'regular_price', 'sale_price', 'additional_pricing_details', 'course_financing_available', 'indian_students_program_fee', 'indian_students_payment_deadline', 'indian_students_GST_included', 'indian_student_installments|1|installment_amount', 'indian_student_installments|1|payment_deadline', 'indian_student_installments|2|installment_amount', 'indian_student_installments|2|payment_deadline', 'international_students_program_fee', 'international_students_payment_deadline', 'international_student_installments|1|installment_amount', 'international_student_installments|1|payment_deadline', 'international_student_installments|2|installment_amount', 'international_student_installments|2|payment_deadline', 'institute', 'partner_course_url', 'corporate_sponsor|1|name', 'corporate_sponsor|1|logo', 'corporate_sponsor|2|name', 'corporate_sponsor|2|logo', 'accreditation|1|name', 'accreditation|1|logo', 'accreditation|1|description', 'accreditation|2|name', 'accreditation|2|logo', 'accreditation|2|description', 'assessment_content', 'post_course_interaction', 'international_faculty', 'human_interaction', 'personalized_teaching', 'live_class', 'job_assistance', 'internship', 'alumni_network', 'placement|1|company_name', 'placement|1|role_offered', 'placement|2|company_name', 'placement|2|role_offered', 'learning_mediums', 'virtual_labs', 'case_based_learning', 'capstone_project', 'average_salary', 'highest_salary', 'application_seat_ratio', 'bounce_rate', 'completion_ratio', 'enrollment_ratio', 'faculty_student_ratio', 'gender_diversity', 'student_stream_diversity', 'student_nationality_diversity', 'average_salary_hike', 'instructor_citations', 'syllabus', 'Faq|1|question', 'Faq|1|answer', 'Faq|2|question', 'Faq|2|answer', 'course_start_date', 'course_end_date', 'course_batch_size', 'course_batch_type', 'course_details_start_time', 'course_details_end_time', 'course_details_time_zone', 'course_details_enrollment_start_date', 'course_details_enrollment_end_date', 'additional_batch|1|batch_size', 'additional_batch|1|batch_start_date', 'additional_batch|1|batch_end_date', 'additional_batch|1|batch_enrollment_start_date', 'additional_batch|1|batch_enrollment_end_date', 'additional_batch|1|total_duration', 'additional_batch|1|total_duration_unit', 'additional_batch|1|pricing_type', 'additional_batch|1|regular_price', 'additional_batch|1|sale_price', 'additional_batch|1|batch_type', 'additional_batch|1|batch_time_zone', 'additional_batch|1|batch_start_time', 'additional_batch|1|batch_end_time', 'additional_batch|2|batch_size', 'additional_batch|2|batch_start_date', 'additional_batch|2|batch_end_date', 'additional_batch|2|batch_enrollment_start_date', 'additional_batch|2|batch_enrollment_end_date', 'additional_batch|2|total_duration', 'additional_batch|2|total_duration_unit', 'additional_batch|2|pricing_type', 'additional_batch|2|regular_price', 'additional_batch|2|sale_price', 'additional_batch|2|batch_type', 'additional_batch|2|batch_time_zone', 'additional_batch|2|batch_start_time', 'additional_batch|2|batch_end_time'])

for i in range(len(lis)):
    print(i, lis[i])
    driver.get(lis[i])
    html = requests.get(lis[i]).text
    #soup = BeautifulSoup(html, 'html.parser')

    time.sleep(2)

    partner_course_url = lis[i]

    try:
        title = driver.find_element(By.CLASS_NAME,'top-heading').text
    except:
        title = None
        print("title")

    try:
        topic = driver.find_element(By.XPATH,'//*[@id="BreadCrumbs"]/div/div/div/a[2]').text
    except:
        topic = None
        print("topic")


    try:
        level = driver.find_element(By.CLASS_NAME,'level').text.replace(" Level", "")
        print(level)
    except:
        level = None
        print("level")

    try:
        short_description = driver.find_element(By.CLASS_NAME,'heading-2').text
    except:
        short_description = None
        print("short_description")

    try:
        description = driver.find_element(By.XPATH,'//*[@id="freemium-course"]/div[1]/div/div/div[1]/p[2]').text
    except:
        description = None
        print("description")

    try:
        ul = driver.find_element(By.CLASS_NAME, 'best-suited').find_element(By.TAG_NAME, 'ul')
        li = ul.find_elements(By.TAG_NAME, 'li')
        target_students = ""
        for i in li:
            target_students = target_students + i.text + "|"
        if(len(target_students)>1):
            target_students = target_students[:-1]
    except:
        print("target_students")

    try:
        ul = driver.find_element(By.CLASS_NAME, 'skill-covered').find_element(By.TAG_NAME, 'ul')
        li = ul.find_elements(By.TAG_NAME, 'li')
        what_will_learn = ""
        for i in li:
            what_will_learn = what_will_learn + i.text + "|"
        if(len(what_will_learn)>1):
            what_will_learn = what_will_learn[:-1]
    except:
        print("what_will_learn")

    modules = driver.find_element(By.ID,'curriculum_content_child').find_elements(By.CLASS_NAME,'level-1')
    content = ""
    for j in range(1,len(modules)+1):
        #print(modules[j-1].find_element(By.TAG_NAME,"h4").text)
        m = modules[j-1].find_element(By.TAG_NAME,"h3").get_attribute('textContent')
        #m = re.sub("(^Lesson [0-9]+ - )|(^Lesson [0-9][0-9]: )", "", m)
        #print(m)
        content = content + "<p><strong>" + m + "</strong><br>"

        submodules = modules[j-1].find_element(By.CLASS_NAME,'level-2').find_elements(By.TAG_NAME,'h4')
        for k in range(1, len(submodules)+1):
            #print(submodules[k-1].find_element(By.TAG_NAME, "h5").get_attribute('textContent'))
            sm = submodules[k-1].get_attribute('textContent')
            #sm = re.sub("[0-9]+(\.[0-9]*)?\s", "", sm)
            #print(sm)
            content = content + str(k) + ". " + sm + "<br>"
        content = content + "</p>"

    print("content", content)

    try:
        reviews = driver.find_elements(By.CLASS_NAME,'review-card')

        try:
            review_name_1 = reviews[0].find_element(By.TAG_NAME, 'h3').text
            print(review_name_1)
        except:
            review_name_1 = None
            print("No review_name_1")

        try:
            review_rating_1 = reviews[0].find_element(By.CLASS_NAME,'star_in').get_attribute('style').replace("px;","").replace("width:","").replace(" ","")
            review_rating_1 = round(float(review_rating_1)/16.75)
            print("review_rating_1", review_rating_1)
        except:
            review_rating_1 = None
            print("No review_rating_1")

        try:
            review_1 = reviews[0].find_element(By.TAG_NAME,'p').text
            print(review_1)
        except:
            review_1 = None
            print("No review_1")

        try:
            review_photo_1 = reviews[0].find_element(By.TAG_NAME,'img').get_attribute('src')
            print(review_photo_1)
        except:
            review_photo_1 = None
            print("review_photo_1")
    except:
        review_name_1 = None
        review_rating_1 =  None
        review_1 = None
        review_photo_1 = None

    try:
        reviews = driver.find_elements(By.CLASS_NAME,'review-card')

        try:
            review_name_2 = reviews[1].find_element(By.TAG_NAME, 'h3').text
            print(review_name_2)
        except:
            review_name_2 = None
            print("No review_name_1")

        try:
            review_rating_2 = reviews[1].find_element(By.CLASS_NAME,'star_in').get_attribute('style').replace("px;","").replace("width:","").replace(" ","")
            review_rating_2 = round(float(review_rating_2)/16.8)
            print("review_rating_2", review_rating_2)
        except:
            review_rating_2 = None
            print("No review_rating_2")

        try:
            review_2 = reviews[1].find_element(By.TAG_NAME,'p').text
            print(review_2)
        except:
            review_2 = None
            print("No review_2")

        try:
            review_photo_2 = reviews[1].find_element(By.TAG_NAME,'img').get_attribute('src')
            print(review_photo_2)
        except:
            review_photo_2 = None
            print("review_photo_2")
    except:
        review_name_2 = None
        review_rating_2 =  None
        review_2 = None
        review_photo_2 = None

    try:
        course_instructors = driver.find_element(By.ID, 'course-advisers').find_element(By.CLASS_NAME, 'c_list')
        instructors = course_instructors.find_elements(By.TAG_NAME, 'li')
        print(len(instructors))

        if(len(instructors)>3):
            try:
                instructor_name_4 = instructors[3].find_element(By.TAG_NAME, 'h3').text
                print(instructor_name_4)
            except:
                instructor_name_4 = None
                print("instructor_name_4")

            try:
                instructor_designation_4 = instructors[3].find_element(By.TAG_NAME, 'span').text
                print(instructor_designation_4)
            except:
                instructor_designation_4 = None
                print("instructor_designation_4")

            try:
                instructor_bio_4 = instructors[3].find_element(By.TAG_NAME, 'p').text
                print(instructor_bio_4)
            except:
                instructor_bio_4 = None
                print("instructor_bio_4")

            try:
                instructor_image_4 = instructors[3].find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(instructor_image_4)
            except:
                instructor_image_4 = None
                print("instructor_image_4")

            try:
                instructor_twitter_4 = instructors[3].find_element(By.CLASS_NAME, 'tw').get_attribute('href')
                print(instructor_twitter_4)
            except:
                instructor_twitter_4 = None
                print("instructor_twitter_4")

            try:
                instructor_facebook_4 = instructors[3].find_element(By.CLASS_NAME, 'fb').get_attribute('href')
                print(instructor_facebook_4)
            except:
                instructor_facebook_4 = None
                print("instructor_facebook_4")

            try:
                instructor_linkedin_4 = instructors[3].find_element(By.CLASS_NAME, 'lkin').get_attribute('href')
                print(instructor_linkedin_4)
            except:
                instructor_linkedin_4 = None
                print("instructor_linkedin_4")

        else:
            instructor_name_4 = instructor_bio_4 = instructor_image_4 = instructor_designation_4 = instructor_twitter_4 = instructor_linkedin_4 = instructor_facebook_4 = None

        if(len(instructors)>2):
            try:
                instructor_name_3 = instructors[2].find_element(By.TAG_NAME, 'h3').text
                print(instructor_name_3)
            except:
                instructor_name_3 = None
                print("instructor_name_3")

            try:
                instructor_designation_3 = instructors[2].find_element(By.TAG_NAME, 'span').text
                print(instructor_designation_3)
            except:
                instructor_designation_3 = None
                print("instructor_designation_3")

            try:
                instructor_bio_3 = instructors[2].find_element(By.TAG_NAME, 'p').text
                print(instructor_bio_3)
            except:
                instructor_bio_3 = None
                print("instructor_bio_3")

            try:
                instructor_image_3 = instructors[2].find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(instructor_image_3)
            except:
                instructor_image_3 = None
                print("instructor_image_3")

            try:
                instructor_twitter_3 = instructors[2].find_element(By.CLASS_NAME, 'tw').get_attribute('href')
                print(instructor_twitter_3)
            except:
                instructor_twitter_3 = None
                print("instructor_twitter_3")

            try:
                instructor_facebook_3 = instructors[2].find_element(By.CLASS_NAME, 'fb').get_attribute('href')
                print(instructor_facebook_3)
            except:
                instructor_facebook_3 = None
                print("instructor_facebook_3")

            try:
                instructor_linkedin_3 = instructors[2].find_element(By.CLASS_NAME, 'lkin').get_attribute('href')
                print(instructor_linkedin_3)
            except:
                instructor_linkedin_3 = None
                print("instructor_linkedin_3")

        else:
            instructor_name_3 = instructor_bio_3 = instructor_image_3 = instructor_designation_3 = instructor_twitter_3 = instructor_linkedin_3 = instructor_facebook_3 = None

        if(len(instructors)>1):
            try:
                instructor_name_2 = instructors[1].find_element(By.TAG_NAME, 'h3').text
                print(instructor_name_2)
            except:
                instructor_name_2 = None
                print("instructor_name_2")

            try:
                instructor_designation_2 = instructors[1].find_element(By.TAG_NAME, 'span').text
                print(instructor_designation_2)
            except:
                instructor_designation_2 = None
                print("instructor_designation_2")

            try:
                instructor_bio_2 = instructors[1].find_element(By.TAG_NAME, 'p').text
                print(instructor_bio_2)
            except:
                instructor_bio_2 = None
                print("instructor_bio_2")

            try:
                instructor_image_2 = instructors[1].find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(instructor_image_2)
            except:
                instructor_image_2 = None
                print("instructor_image_2")

            try:
                instructor_twitter_2 = instructors[1].find_element(By.CLASS_NAME, 'tw').get_attribute('href')
                print(instructor_twitter_2)
            except:
                instructor_twitter_2 = None
                print("instructor_twitter_2")

            try:
                instructor_facebook_2 = instructors[1].find_element(By.CLASS_NAME, 'fb').get_attribute('href')
                print(instructor_facebook_2)
            except:
                instructor_facebook_2 = None
                print("instructor_facebook_2")

            try:
                instructor_linkedin_2 = instructors[1].find_element(By.CLASS_NAME, 'lkin').get_attribute('href')
                print(instructor_linkedin_2)
            except:
                instructor_linkedin_2 = None
                print("instructor_linkedin_2")

        else:
            instructor_name_2 = instructor_bio_2 = instructor_image_2 = instructor_designation_2 = instructor_twitter_2 = instructor_linkedin_2 = instructor_facebook_2 = None

        if(len(instructors)>0):
            try:
                instructor_name_1 = instructors[0].find_element(By.TAG_NAME, 'h3').text
                print(instructor_name_1)
            except:
                instructor_name_1 = None
                print("instructor_name_1")

            try:
                instructor_designation_1 = instructors[0].find_element(By.TAG_NAME, 'span').text
                print(instructor_designation_1)
            except:
                instructor_designation_1 = None
                print("instructor_designation_1")

            try:
                instructor_bio_1 = instructors[0].find_element(By.TAG_NAME, 'p').text
                print(instructor_bio_1)
            except:
                instructor_bio_1 = None
                print("instructor_bio_1")

            try:
                instructor_image_1 = instructors[0].find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(instructor_image_1)
            except:
                instructor_image_1 = None
                print("instructor_image_1")

            try:
                instructor_twitter_1 = instructors[0].find_element(By.CLASS_NAME, 'tw').get_attribute('href')
                print(instructor_twitter_1)
            except:
                instructor_twitter_1 = None
                print("instructor_twitter_1")

            try:
                instructor_facebook_1 = instructors[0].find_element(By.CLASS_NAME, 'fb').get_attribute('href')
                print(instructor_facebook_1)
            except:
                instructor_facebook_1 = None
                print("instructor_facebook_1")

            try:
                instructor_linkedin_1 = instructors[0].find_element(By.CLASS_NAME, 'lkin').get_attribute('href')
                print(instructor_linkedin_1)
            except:
                instructor_linkedin_1 = None
                print("instructor_linkedin_1")

        else:
            instructor_name_1 = instructor_bio_1 = instructor_image_1 = instructor_designation_1 = instructor_twitter_1 = instructor_linkedin_1 = instructor_facebook_1 = None
    except:
        instructor_name_4 = instructor_bio_4 = instructor_image_4 = instructor_designation_4 = instructor_twitter_4 = instructor_linkedin_4 = instructor_facebook_4 = None
        instructor_name_3 = instructor_bio_3 = instructor_image_3 = instructor_designation_3 = instructor_twitter_3 = instructor_linkedin_3 = instructor_facebook_3 = None
        instructor_name_2 = instructor_bio_2 = instructor_image_2 = instructor_designation_2 = instructor_twitter_2 = instructor_linkedin_2 = instructor_facebook_2 = None
        instructor_name_1 = instructor_bio_1 = instructor_image_1 = instructor_designation_1 = instructor_twitter_1 = instructor_linkedin_1 = instructor_facebook_1 = None

    div = driver.find_element(By.CLASS_NAME, 'key-feature')
    #print(div.find_element(By.CLASS_NAME, 'time').find_element(By.TAG_NAME, 'b').text)

    try:
        total_video_content, total_video_content_unit = div.find_element(By.CLASS_NAME, 'time').find_element(By.TAG_NAME, 'b').text.split(" ")
    except:
        total_video_content = None
        total_video_content_unit = None
        print("total_video_content, total_video_content_unit")

    try:
        access = div.find_element(By.CLASS_NAME, 'days').find_element(By.TAG_NAME, 'b').text
        if(" Days of Access" in access):
            availabilities = "Limited Access"
    except:
        availabilities = None
        print("availabilities")

    #driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID,"Faqs"))

    try:
        faq_question_1 = driver.find_element(By.ID, 'course-faq-hide').find_elements(By.TAG_NAME, "li")[0].find_element(By.TAG_NAME, "h3").text
        print(faq_question_1)
    except:
        faq_question_1 = None
        print("faq_question_1")

    try:
        faq_answer_1 = driver.find_element(By.ID, 'course-faq-hide').find_elements(By.TAG_NAME, "li")[0].find_element(By.CLASS_NAME, "exam-body").text
        print(faq_answer_1)
    except:
        faq_answer_1 = None
        print("faq_answer_1")

    try:
        faq_question_2 = driver.find_element(By.ID, 'course-faq-hide').find_elements(By.TAG_NAME, "li")[1].find_element(By.TAG_NAME, "h3").text
        print(faq_question_2)
    except:
        faq_question_2 = None
        print("faq_question_2")

    try:
        #driver.find_element(By.ID, 'course-faq-hide').find_elements(By.TAG_NAME, "li")[1].click()
        #time.sleep(2)
        faq_answer_2 = driver.find_elements(By.CLASS_NAME, "exam-body")[1].get_attribute("textContent")
        print(faq_answer_2)
    except:
        faq_answer_2 = None
        print("faq_answer_2")

    case_based_learning = False
    if " case stud" in description.lower() or " case based" in description.lower() or " case stud" in content.lower() or " case based" in content.lower() or " case stud" in what_will_learn.lower() or " case based" in what_will_learn.lower():
        case_based_learning = True

    learning_mediums = ""
    if "hands-on" in description.lower() or "hands-on" in what_will_learn.lower() or "hands-on" in content.lower():
        learning_mediums += 'Hands-On Learning, '
    if case_based_learning:
        learning_mediums += 'Case Studies, '
    if "industry" in description.lower() or "industry" in what_will_learn.lower()or "industry" in content.lower():
        learning_mediums += 'Industry Exposure, '
    if(len(learning_mediums)>1):
        learning_mediums = learning_mediums[:-2]

    capstone_project = False
    if("capstone" in description.lower() or "capstone" in what_will_learn.lower() or "capstone" in content.lower()):
        capstone_project = True

    virtual_labs = False
    if(" lab " in description.lower() or " lab " in what_will_learn.lower() or " lab " in content.lower() or " labs " in description.lower() or " labs " in what_will_learn.lower() or " labs " in content.lower()):
        virtual_labs = True

    try:
        btn = driver.find_element(By.XPATH, '//*[@id="introVideo"]/span')
        btn.click()
        time.sleep(2)

        embedded_video_url = driver.find_element(By.XPATH, '//*[@id="jw-player-home-banner"]/div[2]/video').get_attribute('src')
        print(embedded_video_url)
    except:
        embedded_video_url = None
        print("embedded_video_url")

    df = df.append({'title':title, 'learn_type':"Certification", 'topics':topic, 'skills':None, 'description':description, 'cover_image':None, 'cover_video':None, 'embedded_video_url':embedded_video_url, 'delivery_method':"Online", 'instruction_type':"Self Paced", 'content_main_description':content, 'content_module|1|heading':None, 'content_module|1|subheading_1':None, 'content_module|1|subheading_2':None, 'content_module|2|heading':None, 'content_module|2|subheading_1':None, 'content_module|2|subheading_2':None, 'what_will_learn':what_will_learn, 'prerequisites':None, 'target_students':target_students, 'instructor|1|name':instructor_name_1, 'instructor|1|designation':instructor_designation_1, 'instructor|1|instructor_bio':instructor_bio_1, 'instructor|1|linkedin_url':instructor_linkedin_1, 'instructor|1|facebook_url':instructor_facebook_1, 'instructor|1|twitter_url':instructor_twitter_1, 'instructor|1|instructor_image':instructor_image_1, 'instructor|2|name':instructor_name_2, 'instructor|2|designation':instructor_designation_2, 'instructor|2|instructor_bio':instructor_bio_2, 'instructor|2|linkedin_url':instructor_linkedin_2, 'instructor|2|facebook_url':instructor_facebook_2, 'instructor|2|twitter_url':instructor_twitter_2, 'instructor|2|instructor_image':instructor_image_2, 'instructor|3|name':instructor_name_3, 'instructor|3|designation':instructor_designation_3, 'instructor|3|instructor_bio':instructor_bio_3, 'instructor|3|linkedin_url':instructor_linkedin_3, 'instructor|3|facebook_url':instructor_facebook_3, 'instructor|3|twitter_url':instructor_twitter_3, 'instructor|3|instructor_image':instructor_image_3, 'instructor|4|name':instructor_name_4, 'instructor|4|designation':instructor_designation_4, 'instructor|4|instructor_bio':instructor_bio_4, 'instructor|4|linkedin_url':instructor_linkedin_4, 'instructor|4|facebook_url':instructor_facebook_4, 'instructor|4|twitter_url':instructor_twitter_4, 'instructor|4|instructor_image':instructor_image_4,'review|1|reviewer_name':review_name_1, 'review|1|photo':review_photo_1, 'review|1|review_date':None, 'review|1|review':review_1, 'review|1|rating':review_rating_1, 'review|2|reviewer_name':review_name_2, 'review|2|photo':review_photo_2, 'review|2|review_date':None, 'review|2|review':review_2, 'review|2|rating':review_rating_2, 'total_duration':None, 'total_duration_unit':None, 'total_video_content':total_video_content, 'total_video_content_unit':total_video_content_unit, 'recommended_effort_per_week':None, 'avg_session_duration_with_instructor':None, 'level':level, 'languages':"English", 'short_description':short_description, 'subtitle_languages':"English", 'accessibilities':"Desktop, Laptop", 'availabilities':availabilities, 'Display Price':None, 'pricing_type':"Free", 'currency':None, 'regular_price':None, 'sale_price':None, 'additional_pricing_details':None, 'course_financing_available':None, 'indian_students_program_fee':None, 'indian_students_payment_deadline':None, 'indian_students_GST_included':None, 'indian_student_installments|1|installment_amount':None, 'indian_student_installments|1|payment_deadline':None, 'indian_student_installments|2|installment_amount':None, 'indian_student_installments|2|payment_deadline':None, 'international_students_program_fee':None, 'international_students_payment_deadline':None, 'international_student_installments|1|installment_amount':None, 'international_student_installments|1|payment_deadline':None, 'international_student_installments|2|installment_amount':None, 'international_student_installments|2|payment_deadline':None, 'institute':"Simplilearn", 'partner_course_url':partner_course_url, 'corporate_sponsor|1|name':None, 'corporate_sponsor|1|logo':None, 'corporate_sponsor|2|name':None, 'corporate_sponsor|2|logo':None, 'accreditation|1|name':None, 'accreditation|1|logo':None, 'accreditation|1|description':None, 'accreditation|2|name':None, 'accreditation|2|logo':None, 'accreditation|2|description':None, 'assessment_content':None, 'post_course_interaction':None, 'international_faculty':None, 'human_interaction':False, 'personalized_teaching':False, 'live_class':False, 'job_assistance':False, 'internship':False, 'alumni_network':None, 'placement|1|company_name':None, 'placement|1|role_offered':None, 'placement|2|company_name':None, 'placement|2|role_offered':None, 'learning_mediums':learning_mediums, 'virtual_labs':virtual_labs, 'case_based_learning':case_based_learning, 'capstone_project':capstone_project, 'average_salary':None, 'highest_salary':None, 'application_seat_ratio':None, 'bounce_rate':None, 'completion_ratio':None, 'enrollment_ratio':None, 'faculty_student_ratio':None, 'gender_diversity':None, 'student_stream_diversity':None, 'student_nationality_diversity':None, 'average_salary_hike':None, 'instructor_citations':None, 'syllabus':None, 'Faq|1|question':faq_question_1, 'Faq|1|answer':faq_answer_1, 'Faq|2|question':faq_question_2, 'Faq|2|answer':faq_answer_2, 'course_start_date':None, 'course_end_date':None, 'course_batch_size':None, 'course_batch_type':None, 'course_details_start_time':None, 'course_details_end_time':None, 'course_details_time_zone':None, 'course_details_enrollment_start_date':None, 'course_details_enrollment_end_date':None, 'additional_batch|1|batch_size':None, 'additional_batch|1|batch_start_date':None, 'additional_batch|1|batch_end_date':None, 'additional_batch|1|batch_enrollment_start_date':None, 'additional_batch|1|batch_enrollment_end_date':None, 'additional_batch|1|total_duration':None, 'additional_batch|1|total_duration_unit':None, 'additional_batch|1|pricing_type':None, 'additional_batch|1|regular_price':None, 'additional_batch|1|sale_price':None, 'additional_batch|1|batch_type':None, 'additional_batch|1|batch_time_zone':None, 'additional_batch|1|batch_start_time':None, 'additional_batch|1|batch_end_time':None, 'additional_batch|2|batch_size':None, 'additional_batch|2|batch_start_date':None, 'additional_batch|2|batch_end_date':None, 'additional_batch|2|batch_enrollment_start_date':None, 'additional_batch|2|batch_enrollment_end_date':None, 'additional_batch|2|total_duration':None, 'additional_batch|2|total_duration_unit':None, 'additional_batch|2|pricing_type':None, 'additional_batch|2|regular_price':None, 'additional_batch|2|sale_price':None, 'additional_batch|2|batch_type':None, 'additional_batch|2|batch_time_zone':None, 'additional_batch|2|batch_start_time':None, 'additional_batch|2|batch_end_time':None}, ignore_index = True)

df.to_excel("simplilearn-updated.xlsx")
