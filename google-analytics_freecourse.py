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

driver.get('https://analytics.google.com/analytics/academy/')
time.sleep(2)
div = driver.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/h2').text
print(div)


instructor_images = driver.find_elements(By.CLASS_NAME, 'instructor-img')
#print(len(instructor_images))
#for i in instructor_images:
#    print(i.get_attribute('src'))

instructor_name_1 = driver.find_element(By.XPATH,'//*[@id="content"]/section[3]/div/ac-instructor[1]/div/div/h3').text
print(instructor_name_1)

instructor_bio_1 = driver.find_element(By.XPATH,'//*[@id="content"]/section[3]/div/ac-instructor[1]/div/div/p').text
print(instructor_bio_1)

instructor_image_1 = instructor_images[0].get_attribute('src')
print(instructor_image_1)

instructor_name_2 = driver.find_element(By.XPATH,'//*[@id="content"]/section[3]/div/ac-instructor[2]/div/div/h3').text
print(instructor_name_2)

instructor_bio_2 = driver.find_element(By.XPATH,'//*[@id="content"]/section[3]/div/ac-instructor[2]/div/div/p').text
print(instructor_bio_2)

instructor_image_2 = instructor_images[1].get_attribute('src')
print(instructor_image_2)

instructor_name_3 = driver.find_element(By.XPATH,'//*[@id="content"]/section[3]/div/ac-instructor[3]/div/div/h3').text
print(instructor_name_3)

instructor_bio_3 = driver.find_element(By.XPATH,'//*[@id="content"]/section[3]/div/ac-instructor[3]/div/div/p').text
print(instructor_bio_3)

instructor_image_3 = instructor_images[2].get_attribute('src')
print(instructor_image_3)

course_end_date = datetime.strptime("July 1, 2023", '%B %d, %Y').isoformat()

lis = ['https://analytics.google.com/analytics/academy/course/5', 'https://analytics.google.com/analytics/academy/course/6', 'https://analytics.google.com/analytics/academy/course/7', 'https://analytics.google.com/analytics/academy/course/8', 'https://analytics.google.com/analytics/academy/course/9', 'https://analytics.google.com/analytics/academy/course/10']

df = pd.DataFrame(columns=['title', 'learn_type', 'topics', 'skills', 'description', 'cover_image', 'cover_video', 'embedded_video_url', 'delivery_method', 'instruction_type', 'content_main_description', 'content_module|1|heading', 'content_module|1|subheading_1', 'content_module|1|subheading_2', 'content_module|1|subheading_3', 'content_module|1|subheading_4', 'content_module|1|subheading_5', 'content_module|2|heading', 'content_module|2|subheading_1', 'content_module|2|subheading_2', 'content_module|2|subheading_3', 'content_module|2|subheading_4', 'content_module|2|subheading_5', 'content_module|2|subheading_6', 'content_module|3|heading', 'content_module|3|subheading_1', 'content_module|3|subheading_2', 'content_module|3|subheading_3', 'content_module|3|subheading_4', 'content_module|4|heading', 'content_module|4|subheading_1', 'content_module|4|subheading_2', 'content_module|4|subheading_3', 'content_module|4|subheading_4', 'content_module|4|subheading_5', 'content_module|5|heading', 'content_module|5|subheading_1', 'content_module|5|subheading_2', 'content_module|5|subheading_3', 'content_module|6|heading', 'content_module|6|subheading_1', 'content_module|6|subheading_2', 'content_module|6|subheading_3', 'content_module|6|subheading_4', 'content_module|7|heading', 'content_module|7|subheading_1', 'content_module|7|subheading_2', 'content_module|7|subheading_3', 'what_will_learn', 'prerequisites', 'target_students', 'instructor|1|name', 'instructor|1|designation', 'instructor|1|instructor_bio', 'instructor|1|linkedin_url', 'instructor|1|facebook_url', 'instructor|1|twitter_url', 'instructor|1|instructor_image', 'instructor|2|name', 'instructor|2|designation', 'instructor|2|instructor_bio', 'instructor|2|linkedin_url', 'instructor|2|facebook_url', 'instructor|2|twitter_url', 'instructor|2|instructor_image', 'instructor|3|name', 'instructor|3|designation', 'instructor|3|instructor_bio', 'instructor|3|linkedin_url', 'instructor|3|facebook_url', 'instructor|3|twitter_url', 'instructor|3|instructor_image', 'review|1|reviewer_name', 'review|1|photo', 'review|1|review_date', 'review|1|review', 'review|1|rating', 'review|2|reviewer_name', 'review|2|photo', 'review|2|review_date', 'review|2|review', 'review|2|rating', 'total_duration', 'total_duration_unit', 'total_video_content', 'total_video_content_unit', 'recommended_effort_per_week', 'avg_session_duration_with_instructor', 'level', 'languages', 'short_description', 'subtitle_languages', 'accessibilities', 'availabilities', 'Display Price', 'pricing_type', 'currency', 'regular_price', 'sale_price', 'additional_pricing_details', 'course_financing_available', 'indian_students_program_fee', 'indian_students_payment_deadline', 'indian_students_GST_included', 'indian_student_installments|1|installment_amount', 'indian_student_installments|1|payment_deadline', 'indian_student_installments|2|installment_amount', 'indian_student_installments|2|payment_deadline', 'international_students_program_fee', 'international_students_payment_deadline', 'international_student_installments|1|installment_amount', 'international_student_installments|1|payment_deadline', 'international_student_installments|2|installment_amount', 'international_student_installments|2|payment_deadline', 'institute', 'partner_course_url', 'corporate_sponsor|1|name', 'corporate_sponsor|1|logo', 'corporate_sponsor|2|name', 'corporate_sponsor|2|logo', 'accreditation|1|name', 'accreditation|1|logo', 'accreditation|1|description', 'accreditation|2|name', 'accreditation|2|logo', 'accreditation|2|description', 'assessment_content', 'post_course_interaction', 'international_faculty', 'human_interaction', 'personalized_teaching', 'live_class', 'job_assistance', 'internship', 'alumni_network', 'placement|1|company_name', 'placement|1|role_offered', 'placement|2|company_name', 'placement|2|role_offered', 'learning_mediums', 'virtual_labs', 'case_based_learning', 'capstone_project', 'average_salary', 'highest_salary', 'application_seat_ratio', 'bounce_rate', 'completion_ratio', 'enrollment_ratio', 'faculty_student_ratio', 'gender_diversity', 'student_stream_diversity', 'student_nationality_diversity', 'average_salary_hike', 'instructor_citations', 'syllabus', 'Faq|1|question', 'Faq|1|answer', 'Faq|2|question', 'Faq|2|answer', 'course_start_date', 'course_end_date', 'course_batch_size', 'course_batch_type', 'course_details_start_time', 'course_details_end_time', 'course_details_time_zone', 'course_details_enrollment_start_date', 'course_details_enrollment_end_date', 'additional_batch|1|batch_size', 'additional_batch|1|batch_start_date', 'additional_batch|1|batch_end_date', 'additional_batch|1|batch_enrollment_start_date', 'additional_batch|1|batch_enrollment_end_date', 'additional_batch|1|total_duration', 'additional_batch|1|total_duration_unit', 'additional_batch|1|pricing_type', 'additional_batch|1|regular_price', 'additional_batch|1|sale_price', 'additional_batch|1|batch_type', 'additional_batch|1|batch_time_zone', 'additional_batch|1|batch_start_time', 'additional_batch|1|batch_end_time', 'additional_batch|2|batch_size', 'additional_batch|2|batch_start_date', 'additional_batch|2|batch_end_date', 'additional_batch|2|batch_enrollment_start_date', 'additional_batch|2|batch_enrollment_end_date', 'additional_batch|2|total_duration', 'additional_batch|2|total_duration_unit', 'additional_batch|2|pricing_type', 'additional_batch|2|regular_price', 'additional_batch|2|sale_price', 'additional_batch|2|batch_type', 'additional_batch|2|batch_time_zone', 'additional_batch|2|batch_start_time', 'additional_batch|2|batch_end_time'])

for i in range(len(lis)):
    print(i, lis[i])
    driver.get(lis[i])
    time.sleep(2)
    partner_course_url = lis[i]
    title = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[1]/h1').text
    embedded_video_url = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[1]/aa-youtube/div/iframe').get_attribute('src')
    description = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[2]').get_attribute('innerHTML')

    try:
        content_module_1_heading = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[1]/li').text
        content_module_1_heading = re.sub("^Unit\s[1-9]:\s","",content_module_1_heading)
    except:
        content_module_1_heading = None
    try:
        content_module_1_subheading_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[1]/ul/li[1]/span').text
        content_module_1_subheading_1 = re.sub("^Lesson\s[1-9]:\s","",content_module_1_subheading_1)
    except:
        content_module_1_subheading_1 = None
    try:
        content_module_1_subheading_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[1]/ul/li[2]/span').text
        content_module_1_subheading_2 = re.sub("^Lesson\s[1-9]:\s","",content_module_1_subheading_2)
    except:
        content_module_1_subheading_2 = None
    try:
        content_module_1_subheading_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[1]/ul/li[3]/span').text
        content_module_1_subheading_3 = re.sub("^Lesson\s[1-9]:\s","",content_module_1_subheading_3)
    except:
        content_module_1_subheading_3 = None
    try:
        content_module_1_subheading_4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[1]/ul/li[4]/span').text
        content_module_1_subheading_4 = re.sub("^Lesson\s[1-9]:\s","",content_module_1_subheading_4)
    except:
        content_module_1_subheading_4 = None
    try:
        content_module_1_subheading_5 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[1]/ul/li[5]/span').text
        content_module_1_subheading_5 = re.sub("^Lesson\s[1-9]:\s","",content_module_1_subheading_5)
    except:
        content_module_1_subheading_5 = None

    print(content_module_1_heading)
    print(content_module_1_subheading_1)
    print(content_module_1_subheading_2)
    print(content_module_1_subheading_3)
    print(content_module_1_subheading_4)
    print(content_module_1_subheading_5)

    try:
        content_module_2_heading = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[2]/li').text
        content_module_2_heading = re.sub("^Unit\s[1-9]:\s","",content_module_2_heading)
    except:
        content_module_2_heading = None
    try:
        content_module_2_subheading_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[2]/ul/li[1]/span').text
        content_module_2_subheading_1 = re.sub("^Lesson\s[1-9]:\s","",content_module_2_subheading_1)
    except:
        content_module_2_subheading_1 = None
    try:
        content_module_2_subheading_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[2]/ul/li[2]/span').text
        content_module_2_subheading_2 = re.sub("^Lesson\s[1-9]:\s","",content_module_2_subheading_2)
    except:
        content_module_2_subheading_2 = None
    try:
        content_module_2_subheading_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[2]/ul/li[3]/span').text
        content_module_2_subheading_3 = re.sub("^Lesson\s[1-9]:\s","",content_module_2_subheading_3)
    except:
        content_module_2_subheading_3 = None
    try:
        content_module_2_subheading_4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[2]/ul/li[4]/span').text
        content_module_2_subheading_4 = re.sub("^Lesson\s[1-9]:\s","",content_module_2_subheading_4)
    except:
        content_module_2_subheading_4 = None
    try:
        content_module_2_subheading_5 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[2]/ul/li[5]/span').text
        content_module_2_subheading_5 = re.sub("^Lesson\s[1-9]:\s","",content_module_2_subheading_5)
    except:
        content_module_2_subheading_5 = None
    try:
        content_module_2_subheading_6 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[2]/ul/li[6]/span').text
        content_module_2_subheading_6 = re.sub("^Lesson\s[1-9]:\s","",content_module_2_subheading_6)
    except:
        content_module_2_subheading_6 = None

    print(content_module_2_heading)
    print(content_module_2_subheading_1)
    print(content_module_2_subheading_2)
    print(content_module_2_subheading_3)
    print(content_module_2_subheading_4)
    print(content_module_2_subheading_5)
    print(content_module_2_subheading_6)


    try:
        content_module_3_heading = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[3]/li').text
        content_module_3_heading = re.sub("^Unit\s[1-9]:\s","",content_module_3_heading)
    except:
        content_module_3_heading = None
    try:
        content_module_3_subheading_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[3]/ul/li[1]/span').text
        content_module_3_subheading_1 = re.sub("^Lesson\s[1-9]:\s","",content_module_3_subheading_1)
    except:
        content_module_3_subheading_1 = None
    try:
        content_module_3_subheading_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[3]/ul/li[2]/span').text
        content_module_3_subheading_2 = re.sub("^Lesson\s[1-9]:\s","",content_module_3_subheading_2)
    except:
        content_module_3_subheading_2 = None
    try:
        content_module_3_subheading_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[3]/ul/li[3]/span').text
        content_module_3_subheading_3 = re.sub("^Lesson\s[1-9]:\s","",content_module_3_subheading_3)
    except:
        content_module_3_subheading_3 = None
    try:
        content_module_3_subheading_4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[3]/ul/li[4]/span').text
        content_module_3_subheading_4 = re.sub("^Lesson\s[1-9]:\s","",content_module_3_subheading_4)
    except:
        content_module_3_subheading_4 = None

    print(content_module_3_heading)
    print(content_module_3_subheading_1)
    print(content_module_3_subheading_2)
    print(content_module_3_subheading_3)
    print(content_module_3_subheading_4)

    try:
        content_module_4_heading = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[4]/li').text
        content_module_4_heading = re.sub("^Unit\s[1-9]:\s","",content_module_4_heading)

    except:
        content_module_4_heading = None
    try:
        content_module_4_subheading_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[4]/ul/li[1]/span').text
        content_module_4_subheading_1 = re.sub("^Lesson\s[1-9]:\s","",content_module_4_subheading_1)
    except:
        content_module_4_subheading_1 = None
    try:
        content_module_4_subheading_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[4]/ul/li[2]/span').text
        content_module_4_subheading_2 = re.sub("^Lesson\s[1-9]:\s","",content_module_4_subheading_2)
    except:
        content_module_4_subheading_2 = None
    try:
        content_module_4_subheading_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[4]/ul/li[3]/span').text
        content_module_4_subheading_3 = re.sub("^Lesson\s[1-9]:\s","",content_module_4_subheading_3)
    except:
        content_module_4_subheading_3 = None
    try:
        content_module_4_subheading_4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[4]/ul/li[4]/span').text
        content_module_4_subheading_4 = re.sub("^Lesson\s[1-9]:\s","",content_module_4_subheading_4)
    except:
        content_module_4_subheading_4 = None
    try:
        content_module_4_subheading_5 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[4]/ul/li[5]/span').text
        content_module_4_subheading_5 = re.sub("^Lesson\s[1-9]:\s","",content_module_4_subheading_5)
    except:
        content_module_4_subheading_5 = None

    print(content_module_4_heading)
    print(content_module_4_subheading_1)
    print(content_module_4_subheading_2)
    print(content_module_4_subheading_3)
    print(content_module_4_subheading_4)
    print(content_module_4_subheading_5)


    try:
        content_module_5_heading = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[5]/li').text
        content_module_5_heading = re.sub("^Unit\s[1-9]:\s","",content_module_5_heading)
    except:
        content_module_5_heading = None
    try:
        content_module_5_subheading_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[5]/ul/li[1]/span').text
        content_module_5_subheading_1 = re.sub("^Lesson\s[1-9]:\s","",content_module_5_subheading_1)
    except:
        content_module_5_subheading_1 = None
    try:
        content_module_5_subheading_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[5]/ul/li[2]/span').text
        content_module_5_subheading_2 = re.sub("^Lesson\s[1-9]:\s","",content_module_5_subheading_2)
    except:
        content_module_5_subheading_2 = None
    try:
        content_module_5_subheading_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[5]/ul/li[3]/span').text
        content_module_5_subheading_3 = re.sub("^Lesson\s[1-9]:\s","",content_module_5_subheading_3)
    except:
        content_module_5_subheading_3 = None

    print(content_module_5_heading)
    print(content_module_5_subheading_1)
    print(content_module_5_subheading_2)
    print(content_module_5_subheading_3)


    try:
        content_module_6_heading = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[6]/li').text
        content_module_6_heading = re.sub("^Unit\s[1-9]:\s","",content_module_6_heading)
    except:
        content_module_6_heading = None
    try:
        content_module_6_subheading_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[6]/ul/li[1]/span').text
        content_module_6_subheading_1 = re.sub("^Lesson\s[1-9]:\s","",content_module_6_subheading_1)
    except:
        content_module_6_subheading_1 = None
    try:
        content_module_6_subheading_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[6]/ul/li[2]/span').text
        content_module_6_subheading_2 = re.sub("^Lesson\s[1-9]:\s","",content_module_6_subheading_2)
    except:
        content_module_6_subheading_2 = None
    try:
        content_module_6_subheading_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[6]/ul/li[3]/span').text
        content_module_6_subheading_3 = re.sub("^Lesson\s[1-9]:\s","",content_module_6_subheading_3)
    except:
        content_module_6_subheading_3 = None
    try:
        content_module_6_subheading_4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[6]/ul/li[4]/span').text
        content_module_6_subheading_4 = re.sub("^Lesson\s[1-9]:\s","",content_module_6_subheading_4)
    except:
        content_module_6_subheading_4 = None

    print(content_module_6_heading)
    print(content_module_6_subheading_1)
    print(content_module_6_subheading_2)
    print(content_module_6_subheading_3)
    print(content_module_6_subheading_4)

    try:
        content_module_7_heading = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[7]/li').text
        content_module_7_heading = re.sub("^Unit\s[1-9]:\s","",content_module_7_heading)
    except:
        content_module_7_heading = None
    try:
        content_module_7_subheading_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[7]/ul/li[1]/span').text
        content_module_7_subheading_1 = re.sub("^Lesson\s[1-9]:\s","",content_module_7_subheading_1)
    except:
        content_module_7_subheading_1 = None
    try:
        content_module_7_subheading_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[7]/ul/li[2]/span').text
        content_module_7_subheading_2 = re.sub("^Lesson\s[1-9]:\s","",content_module_7_subheading_2)
    except:
        content_module_7_subheading_2 = None
    try:
        content_module_7_subheading_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div/section[2]/div[3]/ul[7]/ul/li[3]/span').text
        content_module_7_subheading_3 = re.sub("^Lesson\s[1-9]:\s","",content_module_7_subheading_3)
    except:
        content_module_7_subheading_3 = None

    print(content_module_7_heading)
    print(content_module_7_subheading_1)
    print(content_module_7_subheading_2)
    print(content_module_7_subheading_3)
    print("\n")

    try:
        case_based_learning = None
        if " case stud" in description.lower() or " case based" in description.lower() or " case stud" in content.lower() or " case based" in content.lower():
            case_based_learning = True
    except:
        pass

    try:
        learning_mediums = ""
        if "hands-on" in description.lower() or "hands-on" in content.lower():
            learning_mediums += 'Hands-On Learning, '
        if case_based_learning:
            learning_mediums += 'Case Studies, '
        if "industry" in description.lower() or "industry" in content.lower():
            learning_mediums += 'Industry Exposure, '
        if(len(learning_mediums)>1):
            learning_mediums = learning_mediums[:-2]
    except:
        pass

    try:
        capstone_project = None
        if("capstone" in description.lower() or "capstone" in content.lower()):
            capstone_project = True
    except:
        pass

    driver.get(lis[i]+"/faqs")
    time.sleep(2)

    faq_1_question = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div[2]/div[2]/div/ol/li[1]/div[1]/div').text
    faq_1_answer = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div[2]/div[2]/div/ol/li[1]/div[2]/div').text
    print(faq_1_question)
    print(faq_1_answer)
    faq_2_question = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div[2]/div[2]/div/ol/li[2]/div[1]/div').text
    faq_2_answer = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div/div[2]/div[2]/div/ol/li[2]/div[2]/div').text
    print(faq_2_question)
    print(faq_2_answer)


    df = df.append({'title':title, 'learn_type':"Certification", 'topics':None, 'skills':None, 'description':description, 'cover_image':None, 'cover_video':None, 'embedded_video_url':embedded_video_url, 'delivery_method':"Online", 'instruction_type':"Self Paced", 'content_main_description':None, 'content_module|1|heading':content_module_1_heading, 'content_module|1|subheading_1':content_module_1_subheading_1, 'content_module|1|subheading_2':content_module_1_subheading_2, 'content_module|1|subheading_3':content_module_1_subheading_3, 'content_module|1|subheading_4':content_module_1_subheading_4, 'content_module|1|subheading_5':content_module_1_subheading_5, 'content_module|2|heading':content_module_2_heading, 'content_module|2|subheading_1':content_module_2_subheading_1, 'content_module|2|subheading_2':content_module_2_subheading_2, 'content_module|2|subheading_3':content_module_2_subheading_3, 'content_module|2|subheading_4':content_module_2_subheading_4, 'content_module|2|subheading_5':content_module_2_subheading_5, 'content_module|2|subheading_6':content_module_2_subheading_6, 'content_module|3|heading':content_module_3_heading, 'content_module|3|subheading_1':content_module_3_subheading_1, 'content_module|3|subheading_2':content_module_3_subheading_2, 'content_module|3|subheading_3':content_module_3_subheading_3, 'content_module|3|subheading_4':content_module_3_subheading_4, 'content_module|4|heading':content_module_4_heading, 'content_module|4|subheading_1':content_module_4_subheading_1, 'content_module|4|subheading_2':content_module_4_subheading_2, 'content_module|4|subheading_3':content_module_4_subheading_2, 'content_module|4|subheading_4':content_module_4_subheading_4, 'content_module|4|subheading_5':content_module_4_subheading_5, 'content_module|5|heading':content_module_5_heading, 'content_module|5|subheading_1':content_module_5_subheading_1, 'content_module|5|subheading_2':content_module_5_subheading_2, 'content_module|5|subheading_3':content_module_5_subheading_3, 'content_module|6|heading':content_module_6_heading, 'content_module|6|subheading_1':content_module_6_subheading_1, 'content_module|6|subheading_2':content_module_6_subheading_2, 'content_module|6|subheading_3':content_module_6_subheading_3, 'content_module|6|subheading_4':content_module_6_subheading_4, 'content_module|7|heading':content_module_7_heading, 'content_module|7|subheading_1':content_module_7_subheading_1, 'content_module|7|subheading_2':content_module_7_subheading_2, 'content_module|7|subheading_3':content_module_7_subheading_3, 'what_will_learn':None, 'prerequisites':None, 'target_students':None, 'instructor|1|name':instructor_name_1, 'instructor|1|designation':None, 'instructor|1|instructor_bio':instructor_bio_1, 'instructor|1|linkedin_url':None, 'instructor|1|facebook_url':None, 'instructor|1|twitter_url':None, 'instructor|1|instructor_image':instructor_image_1, 'instructor|2|name':instructor_name_2, 'instructor|2|designation':None, 'instructor|2|instructor_bio':instructor_bio_2, 'instructor|2|linkedin_url':None, 'instructor|2|facebook_url':None, 'instructor|2|twitter_url':None, 'instructor|2|instructor_image':instructor_image_2, 'instructor|3|name':instructor_name_3, 'instructor|3|designation':None, 'instructor|3|instructor_bio':instructor_bio_3, 'instructor|3|linkedin_url':None, 'instructor|3|facebook_url':None, 'instructor|3|twitter_url':None, 'instructor|3|instructor_image':instructor_image_3, 'review|1|reviewer_name':None, 'review|1|photo':None, 'review|1|review_date':None, 'review|1|review':None, 'review|1|rating':None, 'review|2|reviewer_name':None, 'review|2|photo':None, 'review|2|review_date':None, 'review|2|review': None, 'review|2|rating':None, 'total_duration':None, 'total_duration_unit':None, 'total_video_content':None, 'total_video_content_unit':None, 'recommended_effort_per_week':None, 'avg_session_duration_with_instructor':None, 'level':None, 'languages':"English", 'short_description':None, 'subtitle_languages':"English", 'accessibilities':"Desktop, Laptop", 'availabilities':"Lifetime Access", 'Display Price':None, 'pricing_type':"Free", 'currency':None, 'regular_price':None, 'sale_price':None, 'additional_pricing_details':None, 'course_financing_available':None, 'indian_students_program_fee':None, 'indian_students_payment_deadline':None, 'indian_students_GST_included':None, 'indian_student_installments|1|installment_amount':None, 'indian_student_installments|1|payment_deadline':None, 'indian_student_installments|2|installment_amount':None, 'indian_student_installments|2|payment_deadline':None, 'international_students_program_fee':None, 'international_students_payment_deadline':None, 'international_student_installments|1|installment_amount':None, 'international_student_installments|1|payment_deadline':None, 'international_student_installments|2|installment_amount':None, 'international_student_installments|2|payment_deadline':None, 'institute':"Googlle", 'partner_course_url':partner_course_url, 'corporate_sponsor|1|name':None, 'corporate_sponsor|1|logo':None, 'corporate_sponsor|2|name':None, 'corporate_sponsor|2|logo':None, 'accreditation|1|name':None, 'accreditation|1|logo':None, 'accreditation|1|description':None, 'accreditation|2|name':None, 'accreditation|2|logo':None, 'accreditation|2|description':None, 'assessment_content':None, 'post_course_interaction':None, 'international_faculty':None, 'human_interaction':False, 'personalized_teaching':False, 'live_class':False, 'job_assistance':False, 'internship':False, 'alumni_network':None, 'placement|1|company_name':None, 'placement|1|role_offered':None, 'placement|2|company_name':None, 'placement|2|role_offered':None, 'learning_mediums':learning_mediums, 'virtual_labs':False, 'case_based_learning':case_based_learning, 'capstone_project':capstone_project, 'average_salary':None, 'highest_salary':None, 'application_seat_ratio':None, 'bounce_rate':None, 'completion_ratio':None, 'enrollment_ratio':None, 'faculty_student_ratio':None, 'gender_diversity':None, 'student_stream_diversity':None, 'student_nationality_diversity':None, 'average_salary_hike':None, 'instructor_citations':None, 'syllabus':None, 'Faq|1|question':faq_1_question, 'Faq|1|answer':faq_1_answer, 'Faq|2|question':faq_2_question, 'Faq|2|answer':faq_2_answer, 'course_start_date':None, 'course_end_date':None, 'course_batch_size':None, 'course_batch_type':None, 'course_details_start_time':None, 'course_details_end_time':None, 'course_details_time_zone':None, 'course_details_enrollment_start_date':None, 'course_details_enrollment_end_date':course_end_date, 'additional_batch|1|batch_size':None, 'additional_batch|1|batch_start_date':None, 'additional_batch|1|batch_end_date':None, 'additional_batch|1|batch_enrollment_start_date':None, 'additional_batch|1|batch_enrollment_end_date':None, 'additional_batch|1|total_duration':None, 'additional_batch|1|total_duration_unit':None, 'additional_batch|1|pricing_type':None, 'additional_batch|1|regular_price':None, 'additional_batch|1|sale_price':None, 'additional_batch|1|batch_type':None, 'additional_batch|1|batch_time_zone':None, 'additional_batch|1|batch_start_time':None, 'additional_batch|1|batch_end_time':None, 'additional_batch|2|batch_size':None, 'additional_batch|2|batch_start_date':None, 'additional_batch|2|batch_end_date':None, 'additional_batch|2|batch_enrollment_start_date':None, 'additional_batch|2|batch_enrollment_end_date':None, 'additional_batch|2|total_duration':None, 'additional_batch|2|total_duration_unit':None, 'additional_batch|2|pricing_type':None, 'additional_batch|2|regular_price':None, 'additional_batch|2|sale_price':None, 'additional_batch|2|batch_type':None, 'additional_batch|2|batch_time_zone':None, 'additional_batch|2|batch_start_time':None, 'additional_batch|2|batch_end_time':None}, ignore_index = True)

df.to_excel("google-analytics.xlsx")
