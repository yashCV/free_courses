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

print("Hello")
#driver.get('https://www.simplivlearning.com/free-courses?filter=%7B"course_language_id"%3A%7B"operation"%3A"in"%2C"value"%3A%5B"5a9925e100887bb70fc05f73"%5D%7D%2C"price"%3A%7B"from"%3A0%2C"to"%3A0%7D%7D')
'''
f = open("simpliv-freecourses.txt","w")

for i in range(4):
    driver.get('https://www.simplivlearning.com/free-courses/p-{}?filter=%7B"course_language_id"%3A%7B"operation"%3A"in"%2C"value"%3A%5B"5a9925e100887bb70fc05f73"%5D%7D%2C"price"%3A%7B"from"%3A0%2C"to"%3A0%7D%7D'.format(i+1))
    time.sleep(2)
    els = driver.find_elements(By.CLASS_NAME,"course-image-block")
    print(len(els))
    for i in els:
        f.write("'" + i.find_element(By.TAG_NAME,"a").get_attribute('href') + "', ")
        print("'" + i.find_element(By.TAG_NAME,"a").get_attribute('href') + "', ")
'''

print("Hello")
lis = ['https://www.simplivlearning.com/webdevelopment/getting-started-with-express', 'https://www.simplivlearning.com/lifecoach/the-science-of-change', 'https://www.simplivlearning.com/management/business-development-and-future-of-work-fortune-500-leaders', 'https://www.simplivlearning.com/management/business-development-and-career-planning-fortune-500-firms', 'https://www.simplivlearning.com/dataandanalytics/business-development-and-analytical-thinking-fortune-500', 'https://www.simplivlearning.com/management/business-process-management-and-decision-making-fortune-500-leaders', 'https://www.simplivlearning.com/communications/storytelling-and-future-of-work-fortune-500-leaders', 'https://www.simplivlearning.com/yoga/isha-kriya-a-powerful-meditation-for-self-transformation', 'https://www.simplivlearning.com/generalhealth/be-alcohol-free', 'https://www.simplivlearning.com/gaming/bridge-for-beginners', 'https://www.simplivlearning.com/generalengineering/how-computers-work', 'https://www.simplivlearning.com/socialmediamarketing/youtube-professional-course-for-absolute-beginners-beginners-to-intermediate-level', 'https://www.simplivlearning.com/careercoaching/resume-cv-for-freelancers-entrepreneurs-working-online', 'https://www.simplivlearning.com/generalengineering/the-biggest-problem-in-logistics-supply-chain-management-and-how-to-solve-increasing-your-profit', 'https://www.simplivlearning.com/computerskills/learn-to-code-in-very-easy-steps', 'https://www.simplivlearning.com/lifecoach/light-keys-for-peace-joy-and-abundance', 'https://www.simplivlearning.com/lifecoach/fuel-your-motivation-ultimate-action-strategies-that-works', 'https://www.simplivlearning.com/finance/forex-trading-for-beginners', 'https://www.simplivlearning.com/designtool/autocad-electrical-video-lecture', 'https://www.simplivlearning.com/designtool/autocad-2021-course', 'https://www.simplivlearning.com/3dandanimation/learn-vfx-by-adobe-after-effects', 'https://www.simplivlearning.com/finance/the-secrets-to-profitable-forex-trading', 'https://www.simplivlearning.com/excel/microsoft-excel-learn-from-scratch', 'https://www.simplivlearning.com/careercoaching/manage-conflicts-for-success-at-work-and-in-relationships', 'https://www.simplivlearning.com/searchengineoptimization/seo-cost-calculator-how-much-to-spend-on-seo-to-get-sales', 'https://www.simplivlearning.com/computerskills/creating-and-uploading-a-course-in-simpliv', 'https://www.simplivlearning.com/homeimprovement/is-toxic-mold-making-you-sick', 'https://www.simplivlearning.com/automotivedesign/learn-solidworks-video-lecture-course-free', 'https://www.simplivlearning.com/automotivedesign/learn-revit-architecture-video-lecture-course-free', 'https://www.simplivlearning.com/entrepreneurship/quality-assurance-and-stakeholder-engagement-fortune-500', 'https://www.simplivlearning.com/webdevelopment/introduction-to-redux-saga', 'https://www.simplivlearning.com/networkingandsecurity/cisco-packet-tracer-major-important-practicals', 'https://www.simplivlearning.com/webdevelopment/mastering-rest-apis-in-nodejs-zero-to-hero', 'https://www.simplivlearning.com/google/learn-google-sketchup-video-lecture-free', 'https://www.simplivlearning.com/automotivedesign/catia-v5-comprehensive-video-lecture-course-free', 'https://www.simplivlearning.com/automotivedesign/learn-creo-or-pro-e-video-course-free', 'https://www.simplivlearning.com/dance-and-singing/free-salsa-bachata-stretching-for-dancers-course-50-plus-videos', 'https://www.simplivlearning.com/sap/introduction-to-sap-engineering-workbench', 'https://www.simplivlearning.com/contentmarketing/technical-seo-advanced-userintent-structure-content-strategy', 'https://www.simplivlearning.com/entrepreneurship/business-development-and-stakeholder-engagement-fortune-500', 'https://www.simplivlearning.com/management/quality-assurance-and-career-planning-fortune-500-firms', 'https://www.simplivlearning.com/dataandanalytics/quality-assurance-and-analytical-thinking-fortune-500', 'https://www.simplivlearning.com/entrepreneurship/quality-assurance-and-future-of-work-fortune-500-leaders', 'https://www.simplivlearning.com/communications/storytelling-and-career-planning-fortune-500-firms']

df = pd.DataFrame(columns=['title', 'learn_type', 'topics', 'skills', 'description', 'cover_image', 'cover_video', 'embedded_video_url', 'delivery_method', 'instruction_type', 'content_main_description', 'content_module|1|heading', 'content_module|1|subheading_1', 'content_module|1|subheading_2', 'content_module|1|subheading_3', 'content_module|1|subheading_4', 'content_module|1|subheading_5', 'content_module|2|heading', 'content_module|2|subheading_1', 'content_module|2|subheading_2', 'content_module|2|subheading_3', 'content_module|2|subheading_4', 'content_module|2|subheading_5', 'content_module|2|subheading_6', 'content_module|3|heading', 'content_module|3|subheading_1', 'content_module|3|subheading_2', 'content_module|3|subheading_3', 'content_module|3|subheading_4', 'content_module|4|heading', 'content_module|4|subheading_1', 'content_module|4|subheading_2', 'content_module|4|subheading_3', 'content_module|4|subheading_4', 'content_module|4|subheading_5', 'content_module|5|heading', 'content_module|5|subheading_1', 'content_module|5|subheading_2', 'content_module|5|subheading_3', 'content_module|6|heading', 'content_module|6|subheading_1', 'content_module|6|subheading_2', 'content_module|6|subheading_3', 'content_module|6|subheading_4', 'content_module|7|heading', 'content_module|7|subheading_1', 'content_module|7|subheading_2', 'content_module|7|subheading_3', 'what_will_learn', 'prerequisites', 'target_students', 'instructor|1|name', 'instructor|1|designation', 'instructor|1|instructor_bio', 'instructor|1|linkedin_url', 'instructor|1|facebook_url', 'instructor|1|twitter_url', 'instructor|1|instructor_image', 'instructor|2|name', 'instructor|2|designation', 'instructor|2|instructor_bio', 'instructor|2|linkedin_url', 'instructor|2|facebook_url', 'instructor|2|twitter_url', 'instructor|2|instructor_image', 'review|1|reviewer_name', 'review|1|photo', 'review|1|review_date', 'review|1|review', 'review|1|rating', 'review|2|reviewer_name', 'review|2|photo', 'review|2|review_date', 'review|2|review', 'review|2|rating', 'total_duration', 'total_duration_unit', 'total_video_content', 'total_video_content_unit', 'recommended_effort_per_week', 'avg_session_duration_with_instructor', 'level', 'languages', 'short_description', 'subtitle_languages', 'accessibilities', 'availabilities', 'Display Price', 'pricing_type', 'currency', 'regular_price', 'sale_price', 'additional_pricing_details', 'course_financing_available', 'indian_students_program_fee', 'indian_students_payment_deadline', 'indian_students_GST_included', 'indian_student_installments|1|installment_amount', 'indian_student_installments|1|payment_deadline', 'indian_student_installments|2|installment_amount', 'indian_student_installments|2|payment_deadline', 'international_students_program_fee', 'international_students_payment_deadline', 'international_student_installments|1|installment_amount', 'international_student_installments|1|payment_deadline', 'international_student_installments|2|installment_amount', 'international_student_installments|2|payment_deadline', 'institute', 'partner_course_url', 'corporate_sponsor|1|name', 'corporate_sponsor|1|logo', 'corporate_sponsor|2|name', 'corporate_sponsor|2|logo', 'accreditation|1|name', 'accreditation|1|logo', 'accreditation|1|description', 'accreditation|2|name', 'accreditation|2|logo', 'accreditation|2|description', 'assessment_content', 'post_course_interaction', 'international_faculty', 'human_interaction', 'personalized_teaching', 'live_class', 'job_assistance', 'internship', 'alumni_network', 'placement|1|company_name', 'placement|1|role_offered', 'placement|2|company_name', 'placement|2|role_offered', 'learning_mediums', 'virtual_labs', 'case_based_learning', 'capstone_project', 'average_salary', 'highest_salary', 'application_seat_ratio', 'bounce_rate', 'completion_ratio', 'enrollment_ratio', 'faculty_student_ratio', 'gender_diversity', 'student_stream_diversity', 'student_nationality_diversity', 'average_salary_hike', 'instructor_citations', 'syllabus', 'Faq|1|question', 'Faq|1|answer', 'Faq|2|question', 'Faq|2|answer', 'course_start_date', 'course_end_date', 'course_batch_size', 'course_batch_type', 'course_details_start_time', 'course_details_end_time', 'course_details_time_zone', 'course_details_enrollment_start_date', 'course_details_enrollment_end_date', 'additional_batch|1|batch_size', 'additional_batch|1|batch_start_date', 'additional_batch|1|batch_end_date', 'additional_batch|1|batch_enrollment_start_date', 'additional_batch|1|batch_enrollment_end_date', 'additional_batch|1|total_duration', 'additional_batch|1|total_duration_unit', 'additional_batch|1|pricing_type', 'additional_batch|1|regular_price', 'additional_batch|1|sale_price', 'additional_batch|1|batch_type', 'additional_batch|1|batch_time_zone', 'additional_batch|1|batch_start_time', 'additional_batch|1|batch_end_time', 'additional_batch|2|batch_size', 'additional_batch|2|batch_start_date', 'additional_batch|2|batch_end_date', 'additional_batch|2|batch_enrollment_start_date', 'additional_batch|2|batch_enrollment_end_date', 'additional_batch|2|total_duration', 'additional_batch|2|total_duration_unit', 'additional_batch|2|pricing_type', 'additional_batch|2|regular_price', 'additional_batch|2|sale_price', 'additional_batch|2|batch_type', 'additional_batch|2|batch_time_zone', 'additional_batch|2|batch_start_time', 'additional_batch|2|batch_end_time'])

print("Hello")
for i in range(0,len(lis)):
    print(i, lis[i])
    partner_course_url = lis[i]
    driver.get(lis[i])
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME,'post-title').text

    except:
        title = None
        print("title")

    #try:
    description = driver.find_element(By.ID,'collapse-1').get_attribute('innerHTML')
    print(description)
    #except:
    #    description = None
    #    print("description")

    try:
        short_description = driver.find_element(By.CLASS_NAME,'headline').text
        print(short_description)
        print(short_description, len(short_description))

        if(len(short_description) == 0):
            short_description = driver.find_element(By.ID,'collapse-1').find_elements(By.TAG_NAME,'p')[0].text
            print(short_description)

    except:
        short_description = None
        print("short_description")

    try:
        topics = driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/main/div[1]/div/div/ul/li[2]/p').text
        print("topic", topics)
    except:
        topics = None
        print("topics")

    try:
        level = driver.find_elements(By.CLASS_NAME,'single-feature')[-4].find_elements(By.TAG_NAME,'span')[1].text
        print(level)
    except:
        level = None
        print("level")

    try:
        review = driver.find_elements(By.CLASS_NAME,'rev-info')[0].text
        print("review", review)
        review_name_1, review_date_1  = review.split(" – ")
        print(review_name_1, review_date_1)
    except:
        review_name_1 = None
        review_date_1 = None
        print("review_name_1")
    try:
        review_rating_1 = driver.find_element(By.XPATH,'//*[@id="reviews"]/div[2]/div[1]/div/div[1]/span/div/div[2]').get_attribute('style')
        print("review_rating_1", review_rating_1)
        review_rating_1 = review_rating_1.replace("width: ","").replace("%;","")
        review_rating_1 = round(int(float(review_rating_1))/20)
        print(review_rating_1)
    except:
        review_rating_1 = None
        print("review_rating_1")

    try:
        review_photo_1 = driver.find_element(By.XPATH,'//*[@id="reviews"]/div[2]/div[1]/figure/img').get_attribute('src')
        print(review_photo_1)
    except:
        review_photo_1 = None
        print("review_photo_1")

    try:
        review_1 = driver.find_elements(By.CLASS_NAME,'rev-text')[0].text
        print(review_1)
    except:
        review_1 = None
        print("review_1")

    try:
        review = driver.find_elements(By.CLASS_NAME,'rev-info')[1].text
        print("review", review)
        review_name_2, review_date_2  = review.split(" – ")
        print(review_name_2, review_date_2)
    except:
        review_name_2 = None
        review_date_2 = None
        print("review_name 2")

    try:
        review_rating_2 = driver.find_element(By.XPATH,'//*[@id="reviews"]/div[2]/div[2]/div/div[1]/span/div/div[2]').get_attribute('style')
        print("review_rating_2", review_rating_2)
        review_rating_2 = review_rating_2.replace("width: ","").replace("%;","")
        review_rating_2 = round(int(float(review_rating_2))/20)
        print(review_rating_2)
    except:
        review_rating_2 = None
        print("review_rating_2")

    try:
        review_photo_2 = driver.find_element(By.XPATH,'//*[@id="reviews"]/div[2]/div[2]/figure/img').get_attribute('src')
        print(review_photo_2)
    except:
        review_photo_2 = None
        print("review_photo_2")

    try:
        review_2 = driver.find_elements(By.CLASS_NAME,'rev-text')[1].text
        print(review_2)
    except:
        review_2 = None
        print("review_2")

    try:
        total_video_content = driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/main/div[1]/div/div/ul/li[3]/p').text
        total_video_content = total_video_content[0:5].replace(":",".")
        total_video_content = float(total_video_content)
        total_video_content_unit ="Hours"
        print(total_video_content, total_video_content_unit)
    except:
        total_video_content = None
        total_video_content_unit = None
        print("total_video_content, total_video_content_unit")

    try:
        prereq = driver.find_element(By.XPATH,'//*[@id="description"]/ul[1]')
        prerequisites = ""

        li = prereq.find_elements(By.TAG_NAME,"li")
        for a in li:
            prerequisites = prerequisites + a.text + "|"

        if(len(prerequisites)>1):
            prerequisites = prerequisites[0:-1]
        print(prerequisites)

    except:
        prerequisites = None
        print("prerequisites")

    try:
        wwl = driver.find_element(By.XPATH,'//*[@id="description"]/ul[last()]')
        what_will_learn = ""

        li = wwl.find_elements(By.TAG_NAME,"li")

        for a in li:
            what_will_learn = what_will_learn + a.text + "|"

        if(len(what_will_learn)>1):
            what_will_learn = what_will_learn[0:-1]
        print(what_will_learn)
    except:
        what_will_learn = None
        print("what_will_learn")

    #time.sleep(2)
    modules = driver.find_elements(By.CLASS_NAME,'panel-title')
    content = ""
    for j in range(1,len(modules)+1):
        print(modules[j-1].find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"span").text)
        content = content + "<p><strong>Module " + str(j) + ": " + modules[j-1].find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"span").text + "</strong><br>"
        try:
            k = 1
            while(True):
                print(driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/main/div[2]/div[1]/div/div/section[2]/div[2]/div[{}]/div[2]/div[{}]/div/div/div/a/span[2]'.format(j,k)).get_attribute('innerHTML'))
                content = content + str(k) + ". " + driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/main/div[2]/div[1]/div/div/section[2]/div[2]/div[{}]/div[2]/div[{}]/div/div/div/a/span[2]'.format(j, k)).get_attribute('innerHTML') + "<br>"
                k+=1
        except:
            content = content + "</p>"

    print("content", content)


    case_based_learning = None
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

    capstone_project = None
    if("capstone" in description.lower() or "capstone" in what_will_learn.lower() or "capstone" in content.lower()):
        capstone_project = True

    try:
        instructor = driver.find_element(By.CLASS_NAME,'author-name')
        instructor_name_1 = instructor.find_element(By.TAG_NAME, 'span').text
        print(instructor_name_1)
        btn = instructor.get_attribute('href')
        driver.get(btn)
        time.sleep(2)
    except:
        instructor_name_1 = None
        print("No instructor_name_1")

    try:
        instructor_designation_1 = driver.find_element(By.CLASS_NAME,'author-designation').text
        print(instructor_designation_1)
    except:
        instructor_designation_1 = None
        print("No instructor_designation_1")

    try:
        instructor_bio_1 = driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/div[7]/div[1]/div/div[2]/div[2]/p[2]').text
        print(instructor_bio_1)
    except:
        instructor_bio_1 = None
        print("No instructor_bio_1")

    try:
        instructor_image_1 = driver.find_element(By.CLASS_NAME,'avatar-img').get_attribute('style')
        print(instructor_image_1)
    except:
        instructor_image_1 = None
        print("No instructor_image_1")

    print(short_description)

    df = df.append({'title':title, 'learn_type':"Certification", 'topics':topics, 'skills':None, 'description':description, 'cover_image':None, 'cover_video':None, 'embedded_video_url':None, 'delivery_method':"Online", 'instruction_type':"Self Paced", 'content_main_description':content, 'content_module|1|heading':None, 'content_module|1|subheading_1':None, 'content_module|1|subheading_2':None, 'content_module|2|heading':None, 'content_module|2|subheading_1':None, 'content_module|2|subheading_2':None, 'what_will_learn':what_will_learn, 'prerequisites':prerequisites, 'target_students':None, 'instructor|1|name':instructor_name_1, 'instructor|1|designation':instructor_designation_1, 'instructor|1|instructor_bio':instructor_bio_1, 'instructor|1|linkedin_url':None, 'instructor|1|facebook_url':None, 'instructor|1|twitter_url':None, 'instructor|1|instructor_image':instructor_image_1, 'instructor|2|name':None, 'instructor|2|designation':None, 'instructor|2|instructor_bio':None, 'instructor|2|linkedin_url':None, 'instructor|2|facebook_url':None, 'instructor|2|twitter_url':None, 'instructor|2|instructor_image':None, 'review|1|reviewer_name':review_name_1, 'review|1|photo':review_photo_1, 'review|1|review_date':review_date_1, 'review|1|review':review_1, 'review|1|rating':review_rating_1, 'review|2|reviewer_name':review_name_2, 'review|2|photo':review_photo_2, 'review|2|review_date':review_date_2, 'review|2|review':review_2, 'review|2|rating':review_rating_2, 'total_duration':None, 'total_duration_unit':None, 'total_video_content':total_video_content, 'total_video_content_unit':total_video_content_unit, 'recommended_effort_per_week':None, 'avg_session_duration_with_instructor':None, 'level':level, 'languages':"English", 'short_description':short_description, 'subtitle_languages':"English", 'accessibilities':"Desktop, Laptop, Mobile", 'availabilities':"Lifetime Access", 'Display Price':None, 'pricing_type':"Free", 'currency':None, 'regular_price':None, 'sale_price':None, 'additional_pricing_details':None, 'course_financing_available':None, 'indian_students_program_fee':None, 'indian_students_payment_deadline':None, 'indian_students_GST_included':None, 'indian_student_installments|1|installment_amount':None, 'indian_student_installments|1|payment_deadline':None, 'indian_student_installments|2|installment_amount':None, 'indian_student_installments|2|payment_deadline':None, 'international_students_program_fee':None, 'international_students_payment_deadline':None, 'international_student_installments|1|installment_amount':None, 'international_student_installments|1|payment_deadline':None, 'international_student_installments|2|installment_amount':None, 'international_student_installments|2|payment_deadline':None, 'institute':"Simpliv", 'partner_course_url':partner_course_url, 'corporate_sponsor|1|name':None, 'corporate_sponsor|1|logo':None, 'corporate_sponsor|2|name':None, 'corporate_sponsor|2|logo':None, 'accreditation|1|name':None, 'accreditation|1|logo':None, 'accreditation|1|description':None, 'accreditation|2|name':None, 'accreditation|2|logo':None, 'accreditation|2|description':None, 'assessment_content':None, 'post_course_interaction':None, 'international_faculty':None, 'human_interaction':False, 'personalized_teaching':False, 'live_class':False, 'job_assistance':False, 'internship':False, 'alumni_network':None, 'placement|1|company_name':None, 'placement|1|role_offered':None, 'placement|2|company_name':None, 'placement|2|role_offered':None, 'learning_mediums':learning_mediums, 'virtual_labs':False, 'case_based_learning':case_based_learning, 'capstone_project':capstone_project, 'average_salary':None, 'highest_salary':None, 'application_seat_ratio':None, 'bounce_rate':None, 'completion_ratio':None, 'enrollment_ratio':None, 'faculty_student_ratio':None, 'gender_diversity':None, 'student_stream_diversity':None, 'student_nationality_diversity':None, 'average_salary_hike':None, 'instructor_citations':None, 'syllabus':None, 'Faq|1|question':None, 'Faq|1|answer':None, 'Faq|2|question':None, 'Faq|2|answer':None, 'course_start_date':None, 'course_end_date':None, 'course_batch_size':None, 'course_batch_type':None, 'course_details_start_time':None, 'course_details_end_time':None, 'course_details_time_zone':None, 'course_details_enrollment_start_date':None, 'course_details_enrollment_end_date':None, 'additional_batch|1|batch_size':None, 'additional_batch|1|batch_start_date':None, 'additional_batch|1|batch_end_date':None, 'additional_batch|1|batch_enrollment_start_date':None, 'additional_batch|1|batch_enrollment_end_date':None, 'additional_batch|1|total_duration':None, 'additional_batch|1|total_duration_unit':None, 'additional_batch|1|pricing_type':None, 'additional_batch|1|regular_price':None, 'additional_batch|1|sale_price':None, 'additional_batch|1|batch_type':None, 'additional_batch|1|batch_time_zone':None, 'additional_batch|1|batch_start_time':None, 'additional_batch|1|batch_end_time':None, 'additional_batch|2|batch_size':None, 'additional_batch|2|batch_start_date':None, 'additional_batch|2|batch_end_date':None, 'additional_batch|2|batch_enrollment_start_date':None, 'additional_batch|2|batch_enrollment_end_date':None, 'additional_batch|2|total_duration':None, 'additional_batch|2|total_duration_unit':None, 'additional_batch|2|pricing_type':None, 'additional_batch|2|regular_price':None, 'additional_batch|2|sale_price':None, 'additional_batch|2|batch_type':None, 'additional_batch|2|batch_time_zone':None, 'additional_batch|2|batch_start_time':None, 'additional_batch|2|batch_end_time':None}, ignore_index = True)

df.to_excel("simpliv.xlsx")
