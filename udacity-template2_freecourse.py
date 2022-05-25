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

chromedriver = r'C:\Alaka\Internship NaviSurge\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)


lis = ['https://www.udacity.com/course/ai-fundamentals--ud099','https://www.udacity.com/course/intro-to-descriptive-statistics--ud827','https://www.udacity.com/course/eigenvectors-and-eigenvalues--ud104','https://www.udacity.com/course/product-manager-interview-preparation--ud034','https://www.udacity.com/course/creating-an-analytical-dataset--ud977','https://www.udacity.com/course/problem-solving-with-advanced-analytics--ud976','https://www.udacity.com/course/managing-remote-teams-with-upwork--ud942','https://www.udacity.com/course/intro-to-data-analysis--ud170','https://www.udacity.com/course/sql-for-data-analysis--ud198','https://www.udacity.com/course/intro-to-inferential-statistics--ud201','https://www.udacity.com/course/intro-to-cloud-computing--ud080','https://www.udacity.com/course/self-driving-car-fundamentals-featuring-apollo--ud0419','https://www.udacity.com/course/microsoft-power-platform--ud091','https://www.udacity.com/course/linux-command-line-basics--ud595','https://www.udacity.com/course/how-to-install-android-studio--ud808','https://www.udacity.com/course/android-basics-multiscreen-apps--ud839','https://www.udacity.com/course/android-basics-user-input--ud836','https://www.udacity.com/course/android-basics-user-interface--ud834','https://www.udacity.com/course/what-is-programming--ud994','https://www.udacity.com/course/android-basics-networking--ud843','https://www.udacity.com/course/android-basics-data-storage--ud845','https://www.udacity.com/course/ux-design-for-mobile-developers--ud849','https://www.udacity.com/course/data-visualization-in-tableau--ud1006','https://www.udacity.com/course/writing-readmes--ud777','https://www.udacity.com/course/how-to-create-anything-in-android--ud802','https://www.udacity.com/course/localization-essentials--ud610','https://www.udacity.com/course/html5-canvas--ud292','https://www.udacity.com/course/intro-to-javascript--ud803','https://www.udacity.com/course/swift-for-beginners--ud1022','https://www.udacity.com/course/intro-to-statistics--st101','https://www.udacity.com/course/intro-to-html-and-css--ud001','https://www.udacity.com/course/introduction-to-python--ud1110','https://www.udacity.com/course/introduction-to-virtual-reality--ud1012','https://www.udacity.com/course/shell-workshop--ud206','https://www.udacity.com/course/statistics--st095','https://www.udacity.com/course/swift-for-developers--ud1025','https://www.udacity.com/course/networking-for-web-developers--ud256','https://www.udacity.com/course/intro-to-physics--ph100','https://www.udacity.com/course/wechat-mini-programs--ud667','https://www.udacity.com/course/version-control-with-git--ud123','https://www.udacity.com/course/intro-to-point-click-app-development--ud162','https://www.udacity.com/course/java-programming-basics--ud282','https://www.udacity.com/course/intro-to-psychology--ps001','https://www.udacity.com/course/engagement-monetization-mobile-games--ud407','https://www.udacity.com/course/craft-your-cover-letter--ud244','https://www.udacity.com/course/refresh-your-resume--ud243','https://www.udacity.com/course/strengthen-your-linkedin-network-and-brand--ud242','https://www.udacity.com/course/aiot-foundations--ud074','https://www.udacity.com/course/aws-machine-learning-foundations--ud065','https://www.udacity.com/course/introduction-to-machine-learning-using-microsoft-azure--ud00333','https://www.udacity.com/course/linear-algebra-refresher-course--ud953','https://www.udacity.com/course/machine-learning-unsupervised-learning--ud741','https://www.udacity.com/course/big-data-analytics-in-healthcare--ud758','https://www.udacity.com/course/intel-edge-AI-fundamentals-with-openvino--ud132','https://www.udacity.com/course/artificial-intelligence--ud954','https://www.udacity.com/course/data-visualization-and-d3js--ud507','https://www.udacity.com/course/machine-learning-for-trading--ud501','https://www.udacity.com/course/machine-learning--ud262','https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617','https://www.udacity.com/course/real-time-analytics-with-apache-storm--ud381','https://www.udacity.com/course/ab-testing--ud257','https://www.udacity.com/course/data-analysis-with-r--ud651','https://www.udacity.com/course/intro-to-tensorflow-lite--ud190','https://www.udacity.com/course/introduction-to-computer-vision--ud810','https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187','https://www.udacity.com/course/intro-to-artificial-intelligence--cs271','https://www.udacity.com/course/deep-learning-pytorch--ud188','https://www.udacity.com/course/aws-deepracer--ud014','https://www.udacity.com/course/intro-to-machine-learning--ud120','https://www.udacity.com/course/rapid-prototyping--ud723','https://www.udacity.com/course/product-design--ud509','https://www.udacity.com/course/app-monetization--ud518','https://www.udacity.com/course/ab-testing--ud979','https://www.udacity.com/course/classification-models--ud978','https://www.udacity.com/course/segmentation-and-clustering--ud981','https://www.udacity.com/course/time-series-forecasting--ud980','https://www.udacity.com/course/app-marketing--ud719','https://www.udacity.com/course/how-to-build-a-startup--ep245','https://www.udacity.com/course/get-your-startup-started--ud806','https://www.udacity.com/course/intro-to-data-science--ud359','https://www.udacity.com/course/database-systems-concepts-design--ud150','https://www.udacity.com/course/learn-spark-at-udacity--ud2002','https://www.udacity.com/course/data-analysis-and-visualization--ud404','https://www.udacity.com/course/cloud-native-fundamentals--ud064','https://www.udacity.com/course/hybrid-cloud-fundamentals--ud0321','https://www.udacity.com/course/differential-equations-in-action--cs222','https://www.udacity.com/course/intro-to-information-security--ud459','https://www.udacity.com/course/cyber-physical-systems-security--ud279','https://www.udacity.com/course/network-security--ud199','https://www.udacity.com/course/web-tooling-automation--ud892','https://www.udacity.com/course/responsive-web-design-fundamentals--ud893','https://www.udacity.com/course/website-performance-optimization--ud884','https://www.udacity.com/course/responsive-images--ud882','https://www.udacity.com/course/build-native-mobile-apps-with-flutter--ud905','https://www.udacity.com/course/uikit-fundamentals--ud788','https://www.udacity.com/course/building-high-conversion-web-forms--ud890','https://www.udacity.com/course/software-architecture-design--ud821','https://www.udacity.com/course/authentication-authorization-oauth--ud330','https://www.udacity.com/course/intro-to-ios-app-development-with-swift--ud585','https://www.udacity.com/course/introduction-to-operating-systems--ud923','https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615','https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012','https://www.udacity.com/course/learn-swift-programming-syntax--ud902','https://www.udacity.com/course/offline-web-applications--ud899','https://www.udacity.com/course/software-development-process--ud805','https://www.udacity.com/course/intro-to-progressive-web-apps--ud811','https://www.udacity.com/course/software-analysis-testing--ud333','https://www.udacity.com/course/computer-networking--ud436','https://www.udacity.com/course/firebase-analytics-ios--ud353','https://www.udacity.com/course/human-computer-interaction--ud400','https://www.udacity.com/course/2d-game-development-with-libgdx--ud405','https://www.udacity.com/course/intro-to-jquery--ud245','https://www.udacity.com/course/dynamic-web-applications-with-sinatra--ud268','https://www.udacity.com/course/how-to-make-a-platformer-using-libgdx--ud406','https://www.udacity.com/course/javascript-testing--ud549','https://www.udacity.com/course/object-oriented-javascript--ud711','https://www.udacity.com/course/compilers-theory-and-practice--ud168','https://www.udacity.com/course/object-oriented-programming-in-java--ud283','https://www.udacity.com/course/designing-restful-apis--ud388','https://www.udacity.com/course/gt-refresher-advanced-os--ud098','https://www.udacity.com/course/grand-central-dispatch-gcd--ud576','https://www.udacity.com/course/continuous-integration-and-deployment--ud1030','https://www.udacity.com/course/new-android-fundamentals--ud851','https://www.udacity.com/course/objective-c-for-swift-developers--ud1009','https://www.udacity.com/course/software-testing--cs258','https://www.udacity.com/course/interactive-3d-graphics--cs291','https://www.udacity.com/course/full-stack-foundations--ud088','https://www.udacity.com/course/auto-layout--ud1026','https://www.udacity.com/course/kotlin-bootcamp-for-programmers--ud9011','https://www.udacity.com/course/core-ml--ud1038','https://www.udacity.com/course/intro-to-theoretical-computer-science--cs313','https://www.udacity.com/course/data-wrangling-with-mongodb--ud032','https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352','https://www.udacity.com/course/software-debugging--cs259','https://www.udacity.com/course/deploying-a-hadoop-cluster--ud1000','https://www.udacity.com/course/server-side-swift--ud1031','https://www.udacity.com/course/programming-languages--cs262','https://www.udacity.com/course/intro-to-relational-databases--ud197','https://www.udacity.com/course/mobile-design-and-usability-for-ios--ud1034','https://www.udacity.com/course/intro-to-ajax--ud110','https://www.udacity.com/course/intro-to-algorithms--cs215','https://www.udacity.com/course/the-mvc-pattern-in-ruby--ud270','https://www.udacity.com/course/asynchronous-javascript-requests--ud109','https://www.udacity.com/course/embedded-systems--ud169','https://www.udacity.com/course/http-web-servers--ud303','https://www.udacity.com/course/advanced-android-with-kotlin--ud940','https://www.udacity.com/course/passwordless-login-solutions-for-ios--ud1028','https://www.udacity.com/course/firebase-in-a-weekend-by-google-ios--ud0351','https://www.udacity.com/course/deploying-applications-with-heroku--ud272','https://www.udacity.com/course/c-for-programmers--ud210','https://www.udacity.com/course/intro-to-backend--ud171','https://www.udacity.com/course/javascript-and-the-dom--ud117','https://www.udacity.com/course/firebase-analytics-android--ud354','https://www.udacity.com/course/google-maps-apis--ud864','https://www.udacity.com/course/mobile-design-and-usability-for-android--ud358','https://www.udacity.com/course/ios-design-patterns--ud1029','https://www.udacity.com/course/material-design-for-android-developers--ud862','https://www.udacity.com/course/data-science-interview-prep--ud944','https://www.udacity.com/course/android-interview-prep--ud241','https://www.udacity.com/course/machine-learning-interview-prep--ud1001','https://www.udacity.com/course/front-end-interview-prep--ud250','https://www.udacity.com/course/full-stack-interview-prep--ud252','https://www.udacity.com/course/data-structures-and-algorithms-in-swift--ud1011','https://www.udacity.com/course/ios-interview-prep--ud240','https://www.udacity.com/course/vr-interview-prep--ud251','https://www.udacity.com/course/secure-and-private-ai--ud185','https://www.udacity.com/course/model-building-and-validation--ud919','https://www.udacity.com/course/knowledge-based-ai-cognitive-systems--ud409','https://www.udacity.com/course/artificial-intelligence-for-robotics--cs373','https://www.udacity.com/course/reinforcement-learning--ud600','https://www.udacity.com/course/cyber-physical-systems-design-analysis--ud9876','https://www.udacity.com/course/front-end-frameworks--ud894','https://www.udacity.com/course/ios-networking-with-swift--ud421','https://www.udacity.com/course/javascript-design-patterns--ud989','https://www.udacity.com/course/android-performance--ud825','https://www.udacity.com/course/xcode-debugging--ud774','https://www.udacity.com/course/gradle-for-android-and-java--ud867','https://www.udacity.com/course/javascript-promises--ud898','https://www.udacity.com/course/client-server-communication--ud897','https://www.udacity.com/course/advanced-android-app-development--ud855','https://www.udacity.com/course/web-accessibility--ud891','https://www.udacity.com/course/browser-rendering-optimization--ud860','https://www.udacity.com/course/kotlin-for-android-developers--ud888','https://www.udacity.com/course/ios-persistence-and-core-data--ud325','https://www.udacity.com/course/introduction-to-graduate-algorithms--ud401','https://www.udacity.com/course/high-performance-computer-architecture--ud007','https://www.udacity.com/course/design-of-computer-programs--cs212','https://www.udacity.com/course/es6-javascript-improved--ud356','https://www.udacity.com/course/high-performance-computing--ud281','https://www.udacity.com/course/computability-complexity-algorithms--ud061','https://www.udacity.com/course/advanced-operating-systems--ud189','https://www.udacity.com/course/applied-cryptography--cs387','https://www.udacity.com/course/how-to-make-an-ios-app--ud607','https://www.udacity.com/course/intro-to-devops--ud611']

print(len(lis))

df = pd.DataFrame(columns=['partner_course_url','title','learn_type','description','cover_image','embedded_video_url','delivery_method','instruction_type','content','what_will_learn','prerequisites','target_students','instructor|1|name','instructor|1|designation','instructor|1|instructor_bio','instructor|1|instructor_image','instructor|2|name','instructor|2|designation','instructor|2|instructor_bio','instructor|2|instructor_image','instructor|3|name','instructor|3|designation','instructor|3|instructor_bio','instructor|3|instructor_image','instructor|4|name','instructor|4|designation','instructor|4|instructor_bio','instructor|4|instructor_image','review|1|reviewer_name','review|1|photo',	'review|1|review_date','review|1|review',	'review|1|rating',	'review|2|reviewer_name',	'review|2|photo',	'review|2|review_date',	'review|2|review',	'review|2|rating','corporate_sponsor_logo', 'corporate_sponsor_name', 'accreditation|1|name','accreditation|1|logo','accreditation|1|description','total_duration','total_duration_unit','total_video_content','total_video_content_unit','recommended_effort_per_week','avg_session_duration_with_instructor','batch|1|batch_start_date','batch|1|batch_end_date','enrollment_start_date','enrollment_end_date','level','languages','short_description','subtitle_languages','accessibilities','availabilities','pricing_type','currency','regular_price','sale_price','course_financing_available','finance_details','institute','personalized_teaching','live_class','job_assistance','internship','learning_mediums','case_based_learning','capstone_project'])

for i in range(0,len(lis)):
    print(i, lis[i])
    driver.get(lis[i])
    partner_course_url = lis[i]

    try:
        level = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/main/section[3]/section/div[2]/div[1]/div[3]/h5').text
        print(level)
    except:
        level = None

    try:
        title = driver.find_element(By.CLASS_NAME,'course-hero_courseTitle__1Djr9').text
        delivery_method = "Online"
        languages  = "English"
        subtitle_languages = "English"
        institute = "Udacity"
        instruction_type = "Self Paced"
        learn_type = "Certification"
        accessibilities = "Desktop, Laptop"
        availabilities = "Limited Access"

    except:
        title = None
        delivery_method = None
        languages = None
        learn_type = None
        subtitle_languages = None
        institute = None
        accessibilities = None
        instruction_type = None
        availabilities = None
        print("title, delivery method, languages, subtitle_languages, level, instruction_type, accessibilities, institute, learn_type")

    try:
        corporate_sponsor_logo = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/main/section[2]/section/div/div[1]/div/img").get_attribut('src')
    except:
        corporate_sponsor_logo = None

    try:
        pricing = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[3]/section/div[2]/div[1]/div[1]/h5').text
        print(pricing)
        if "free" in pricing.lower():
            pricing_type = "Free"
            sale_price = 0
            regular_price = 0
            currency = None
            course_financing_available = False
            finance_details = None
        else:
            pricing_type = "Paid"
            regular_price = pricing
            regular_price = re.sub("[^0-9]", "", regular_price)

            sale_price = pricing
            sale_price = re.sub("[^0-9]", "", sale_price)
            if "EUR" in pricing or "£" in pricing:
                currency = "EUR"
            elif "USD" in pricing or "$" in pricing:
                currency = "USD"
            else:
                currency = "INR"

    except:
        pricing_type = None
        regular_price = None
        sale_price = None
        course_financing_available = None
        finance_details = None
        print("Pricing type, regular_price, sale_price, course_financing_available, finance_details")

    try:
        prerequisites = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[7]/section/div').text
        print("prerequisites", prerequisites)
    except:
        prerequisites = None
        print("prerequisites")

    try:
        short_description = driver.find_element(By.CLASS_NAME,'course-hero_courseSubtitle__nv4P4').text
        print("short_description", short_description)
    except:
        short_description = None
        print("short_description")

    try:
        total_duration, total_duration_unit = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[3]/section/div[2]/div[1]/div[2]/h5').text.replace("Approx. ","").split(" ")
        print(total_duration, total_duration_unit)
    except:
         total_duration = None
         total_duration_unit = None
         print("total_duration total_duration_unit")

    try:
        cont = driver.find_elements(By.CLASS_NAME,'course-syllabus_lessonUpper__3JA3U')
        content = ""
        for i in range(len(cont)):
            content = content + "<p><strong>Module "+ str(i+1) + "</strong>" + cont[i].find_element(By.TAG_NAME,'h2').text + "</p>\n"
        if(len(content)>2):
            cont = cont[0:-2]
        print("content", content,"hello")
    except:
        content = None
        print("content")

    try:
        modules = driver.find_elements(By.CLASS_NAME,'course-syllabus_points__1wR0B')
        what_will_learn = ""
        for a in modules:
            l = a.find_elements(By.TAG_NAME,'li')
            for b in l:
                what_will_learn = what_will_learn + b.text + "|"

        what_will_learn = what_will_learn[0:-1]
        #what_will_learn = re.sub('(Complimentary )?Module [0-9]+: ','',what_will_learn)
        print("what_will_learn", what_will_learn)
    except:
        what_will_learn = None
        print("what_will_learn")

    try:
        description = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[3]/section/div[1]/div').text
        print("description", description)
    except:
        description = None
        print("description")

    try:
        instructor_names = driver.find_elements(By.CLASS_NAME,'course-instructors_instructorName__13-ML')
        try:
            instructor_1_name = instructor_names[0].text
            print(instructor_1_name)
        except:
            instructor_1_name = None
        try:
            instructor_2_name = instructor_names[1].text
            print(instructor_2_name)
        except:
            instructor_2_name = None
        try:
            instructor_3_name = instructor_names[2].text
        except:
            instructor_3_name = None
        try:
            instructor_4_name = instructor_names[3].text
        except:
            instructor_4_name = None

    except:
        print("Instructor names")

    try:
        instructor_designation = driver.find_elements(By.CLASS_NAME,'course-instructors_instructorTitle__2Srzt')
        try:
            instructor_1_designation = instructor_designation[0].text
            print(instructor_1_designation)
        except:
            instructor_1_designation = None
        try:
            instructor_2_designation = instructor_designation[1].text
            print(instructor_2_designation)
        except:
            instructor_2_designation = None
        try:
            instructor_3_designation = instructor_designation[2].text
        except:
            instructor_3_designation = None
        try:
            instructor_4_designation = instructor_designation[3].text
        except:
            instructor_4_designation = None
    except:
        print("Instructor designations")

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5);")
        instructor_images=[]

        try:
            for k in range(4):
                pic = driver.find_elements(By.CLASS_NAME,"course-instructors_instructorPhoto__12E9e")[k]
                driver.execute_script("arguments[0].scrollIntoView(true);",pic)
                time.sleep(1)
                #print(pic.get_attribute('src'))
                instructor_images.append(pic.get_attribute('src'))
        except:
            pass

        try:
            instructor_1_image = instructor_images[0]
            print(instructor_1_image)
        except:
            instructor_1_image = None
        try:
            instructor_2_image = instructor_images[1]
            print(instructor_2_image)
        except:
            instructor_2_image = None
        try:
            instructor_3_image = instructor_images[2]
        except:
            instructor_3_image = None
        try:
            instructor_4_image = instructor_images[3]
        except:
            instructor_4_image = None
    except:
        print("Instructor images")

    try:
        features = driver.find_element(By.CLASS_NAME,'text-left').text
        benefits = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[8]/section/div/div/div[3]/ul').text

        personalized_teaching = False
        if "one-on-one" in features.lower() or "one-on-one" in benefits.lower() or "one on one" in features.lower() or "one on one" in benefits.lower():
            personalized_teaching = True

        live_class = False
        if " live class" in features.lower() or " live class" in benefits.lower() or "interactive" in features.lower() or "interactive" in benefits.lower():
            live_class = True

        internship = False
        if "internship" in features.lower() or "internship" in benefits.lower():
            internship = True

        job_assistance = False
        if "career" in features.lower() or "career" in benefits.lower() or "job" in features.lower() or "job" in benefits.lower():
            job_assistance = True

        case_based_learning = False
        if " case stud" in features.lower() or " case based" in benefits.lower():
            case_based_learning = True

        learning_mediums = ""
        if "hands-on" in features.lower() or "hands-on" in benefits.lower():
            learning_mediums += 'Hands-On Learning, '
        if case_based_learning:
            learning_mediums += 'Case Studies, '
        if "industry exposure" in features.lower() or "industry exposure" in benefits.lower():
            learning_mediums += 'Industry Exposure, '
        if(len(learning_mediums)>1):
            learning_mediums = learning_mediums[:-2]

        capstone_project = False
        if("capstone" in features.lower() or "capstone" in benefits.lower() or "capstone" in content.lower() or "capstone" in what_will_learn.lower()):
            capstone_project = True

        print(internship, case_based_learning, learning_mediums, job_assistance, personalized_teaching)

    except:
        internship = None
        case_based_learning = None
        learning_mediums = None
        job_assistance = None
        personalized_teaching = None
        capstone_project = None
        print("internship, case_based_learning, learning_mediums, job_assistance, personalized_teaching, capstone_project")


    df = df.append({'partner_course_url':partner_course_url,'title':title,'learn_type':learn_type,'description':description,'cover_image':None,'embedded_video_url':None,'delivery_method':delivery_method,'instruction_type':instruction_type,'content':content,'what_will_learn':what_will_learn,'prerequisites':prerequisites,'target_students':None,'instructor|1|name':instructor_1_name,'instructor|1|designation':instructor_1_designation,'instructor|1|instructor_bio':None,'instructor|1|instructor_image':instructor_1_image, 'instructor|2|name':instructor_2_name, 'instructor|2|designation':instructor_2_designation,'instructor|2|instructor_bio':None,'instructor|2|instructor_image':instructor_2_image, 'instructor|3|name':instructor_3_name, 'instructor|3|designation':instructor_3_designation, 'instructor|3|instructor_bio':None, 'instructor|3|instructor_image':instructor_3_image, 'instructor|4|name':instructor_4_name,  'instructor|4|designation':instructor_4_designation, 'instructor|4|instructor_bio':None, 'instructor|4|instructor_image':instructor_4_image, 'review|1|reviewer_name':None, 'review|1|photo':None,	'review|1|review_date':None,'review|1|review':None, 'review|1|rating':None,	'review|2|reviewer_name':None,	'review|2|photo':None,'review|2|review_date':None,'review|2|review':None, 'corporate_sponsor_logo':corporate_sponsor_logo, 'corporate_sponsor_name':None, 'accreditation|1|name':None, 'accreditation|1|logo':None, 'accreditation|1|description':None, 'review|2|rating':None, 'total_duration':total_duration, 'total_duration_unit':total_duration_unit, 'total_video_content':None, 'total_video_content_unit':None, 'recommended_effort_per_week':None, 'avg_session_duration_with_instructor':None, 'batch|1|batch_start_date':None, 'batch|1|batch_end_date':None, 'enrollment_start_date':None, 'enrollment_end_date':None, 'level':level, 'languages':languages, 'short_description':short_description, 'subtitle_languages':subtitle_languages, 'accessibilities':accessibilities, 'availabilities':availabilities, 'pricing_type':pricing_type, 'currency':currency, 'regular_price':regular_price, 'sale_price':sale_price, 'course_financing_available':course_financing_available, 'finance_details':finance_details, 'institute':institute, 'personalized_teaching':personalized_teaching, 'live_class':live_class, 'job_assistance':job_assistance, 'internship':internship, 'learning_mediums':learning_mediums, 'case_based_learning':case_based_learning, 'capstone_project':capstone_project}, ignore_index = True)

df.to_excel("udacity-template2.xlsx")

'''
    print(title)
    print(institute)
    print(delivery_method)
    print(languages)
    print(instruction_type)
    print(subtitle_languages)
    print(instructor_1_name)
    print(instructor_1_image)
    print(instructor_1_bio)
    print(instructor_1_designation)
    print(instructor_2_name)
    print(instructor_2_image)
    print(instructor_2_bio)
    print(instructor_2_designation)
    print(instructor_3_name)
    print(instructor_3_image)
    print(instructor_3_bio)
    print(instructor_3_designation)
    print(instructor_4_name)
    print(instructor_4_image)
    print(instructor_4_bio)
    print(instructor_4_designation)
    print(pricing_type)
    print(currency)
    print(regular_price)
    print(sale_price)
    print(prerequisites)
    print(target_students)
    print("18",review_name_1)
    print("19",review_rating_1)
    print(review_date_1)
    print("21",review_1)
    print("18",review_name_2)
    print("19",review_rating_2)
    print(review_date_2)
    print("21",review_2)
    print("39",short_description)
    print(total_duration)
    print(total_duration_unit)
    print(enrollment_end_date)
    print(recommended_effort_per_week)
    print(content)
    print(what_will_learn)
    print(description)
    print(case_based_learning)
    print(capstone_project)
    print(internship)
    print(job_assistance)
    print("\n\n")
'''
