#from sys import intern
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
'''
driver.get(r"https://www.udacity.com/courses/all?level=advanced")
c = driver.find_elements(By.CLASS_NAME,'card_container__25DrK')
print(len(c))
f = open("udacity-courses-advanced.txt", "w")
print("hello")
for i in c:
    print("hello2")
    print(i.get_attribute('href'))
    f.write("'" + i.get_attribute('href') + "', ")
f.close()
'''

'''
lis = ['https://www.udacity.com/school-of-ai', 'https://www.udacity.com/school-of-autonomous-systems', 'https://www.udacity.com/school-of-business', 'https://www.udacity.com/school-of-cloud-computing', 'https://www.udacity.com/school-of-data-science', 'https://www.udacity.com/school-of-product-management', 'https://www.udacity.com/school-of-programming']
#'https://www.udacity.com/school-of-cybersecurity',
f = open("udacity-courses.txt", "w")
for i in lis:
    driver.get(i)
    ul = driver.find_element(By.XPATH,'//*[@id="id-XAUOyPX1W90jqb8oXqAXq"]/div/div/ul')
    li = ul.find_elements(By.TAG_NAME, 'li')
    print(len(li))
    for j in li:
        print(j.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        f.write("'" + j.find_element(By.TAG_NAME, 'a').get_attribute('href') + "'")
f.close()
'''
'''
driver.get('https://www.udacity.com/school-of-cybersecurity')
f = open("udacity-courses.txt", "a")
for i in range(1,7):
    c = driver.find_element(By.XPATH,'//*[@id="id-5qTxLbTDqKdQODX8PWWWen"]/div/ul/li[{}]/article/div/div[2]/a'.format(i))
    print(c.get_attribute('href'))
    f.write("'" + c.get_attribute('href') + "'")
f.close()
'''

lis = ['https://www.udacity.com/course/product-manager-nanodegree--nd036','https://www.udacity.com/course/business-analytics-nanodegree--nd098','https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104','https://www.udacity.com/course/intro-to-programming-nanodegree--nd000','https://www.udacity.com/course/digital-marketing-nanodegree--nd018','https://www.udacity.com/course/ux-designer-nanodegree--nd578','https://www.udacity.com/course/learn-sql--nd072','https://www.udacity.com/course/java-programming-nanodegree--nd079','https://www.udacity.com/course/ai-programming-python-nanodegree--nd089','https://www.udacity.com/course/react-nanodegree--nd019','https://www.udacity.com/course/data-analysis-and-visualization-with-power-BI-nanodegree--nd331','https://www.udacity.com/course/ios-developer-nanodegree--nd003','https://www.udacity.com/course/intro-to-cybersecurity-nanodegree--nd545','https://www.udacity.com/course/agile-software-development-nanodegree--nd144','https://www.udacity.com/course/ai-product-manager-nanodegree--nd088','https://www.udacity.com/course/data-visualization-nanodegree--nd197','https://www.udacity.com/course/marketing-analytics-nanodegree--nd028','https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803','https://www.udacity.com/course/predictive-analytics-for-business-nanodegree--nd008t','https://www.udacity.com/course/digital-freelancer-nanodegree--nd083','https://www.udacity.com/course/rpa-developer-nanodegree--nd340','https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118','https://www.udacity.com/course/ai-fundamentals--ud099','https://www.udacity.com/course/intro-to-descriptive-statistics--ud827','https://www.udacity.com/course/eigenvectors-and-eigenvalues--ud104','https://www.udacity.com/course/product-manager-interview-preparation--ud034','https://www.udacity.com/course/creating-an-analytical-dataset--ud977','https://www.udacity.com/course/problem-solving-with-advanced-analytics--ud976','https://www.udacity.com/course/managing-remote-teams-with-upwork--ud942','https://www.udacity.com/course/intro-to-data-analysis--ud170','https://www.udacity.com/course/sql-for-data-analysis--ud198','https://www.udacity.com/course/intro-to-inferential-statistics--ud201','https://www.udacity.com/course/intro-to-cloud-computing--ud080','https://www.udacity.com/course/self-driving-car-fundamentals-featuring-apollo--ud0419','https://www.udacity.com/course/microsoft-power-platform--ud091','https://www.udacity.com/course/linux-command-line-basics--ud595','https://www.udacity.com/course/how-to-install-android-studio--ud808','https://www.udacity.com/course/android-basics-multiscreen-apps--ud839','https://www.udacity.com/course/android-basics-user-input--ud836','https://www.udacity.com/course/android-basics-user-interface--ud834','https://www.udacity.com/course/what-is-programming--ud994','https://www.udacity.com/course/android-basics-networking--ud843','https://www.udacity.com/course/android-basics-data-storage--ud845','https://www.udacity.com/course/ux-design-for-mobile-developers--ud849','https://www.udacity.com/course/data-visualization-in-tableau--ud1006','https://www.udacity.com/course/writing-readmes--ud777','https://www.udacity.com/course/how-to-create-anything-in-android--ud802','https://www.udacity.com/course/localization-essentials--ud610','https://www.udacity.com/course/html5-canvas--ud292','https://www.udacity.com/course/intro-to-javascript--ud803','https://www.udacity.com/course/swift-for-beginners--ud1022','https://www.udacity.com/course/intro-to-statistics--st101','https://www.udacity.com/course/intro-to-html-and-css--ud001','https://www.udacity.com/course/introduction-to-python--ud1110','https://www.udacity.com/course/introduction-to-virtual-reality--ud1012','https://www.udacity.com/course/shell-workshop--ud206','https://www.udacity.com/course/statistics--st095','https://www.udacity.com/course/swift-for-developers--ud1025','https://www.udacity.com/course/networking-for-web-developers--ud256','https://www.udacity.com/course/intro-to-physics--ph100','https://www.udacity.com/course/wechat-mini-programs--ud667','https://www.udacity.com/course/version-control-with-git--ud123','https://www.udacity.com/course/intro-to-point-click-app-development--ud162','https://www.udacity.com/course/java-programming-basics--ud282','https://www.udacity.com/course/intro-to-psychology--ps001','https://www.udacity.com/course/engagement-monetization-mobile-games--ud407','https://www.udacity.com/course/craft-your-cover-letter--ud244','https://www.udacity.com/course/refresh-your-resume--ud243','https://www.udacity.com/course/strengthen-your-linkedin-network-and-brand--ud242','https://www.udacity.com/course/data-engineer-nanodegree--nd027','https://www.udacity.com/course/blockchain-developer-nanodegree--nd1309','https://www.udacity.com/course/data-analyst-nanodegree--nd002','https://www.udacity.com/course/c-plus-plus-nanodegree--nd213','https://www.udacity.com/course/aws-machine-learning-engineer-nanodegree--nd189','https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011','https://www.udacity.com/course/data-product-manager-nanodegree--nd030','https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044','https://www.udacity.com/course/deep-learning-nanodegree--nd101','https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940','https://www.udacity.com/course/intermediate-python-nanodegree--nd303','https://www.udacity.com/course/ai-for-trading--nd880','https://www.udacity.com/course/full-stack-javascript-developer-nanodegree--nd0067','https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256','https://www.udacity.com/course/cloud-developer-nanodegree--nd9990','https://www.udacity.com/course/cloud-dev-ops-nanodegree--nd9991','https://www.udacity.com/course/java-developer-nanodegree--nd035','https://www.udacity.com/course/intro-to-self-driving-cars--nd113','https://www.udacity.com/course/growth-product-manager-nanodegree--nd037','https://www.udacity.com/course/intro-to-machine-learning-nanodegree--nd229','https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230','https://www.udacity.com/course/cloud-native-application-architecture-nanodegree--nd064','https://www.udacity.com/course/cloud-developer-using-microsoft-azure-nanodegree--nd081','https://www.udacity.com/course/intermediate-javascript-nanodegree--nd032','https://www.udacity.com/course/cloud-devops-using-microsoft-azure-nanodegree--nd082','https://www.udacity.com/course/site-reliability-engineer-nanodegree--nd087','https://www.udacity.com/course/security-engineer-nanodegree--nd698','https://www.udacity.com/course/data-science-for-business-leaders--nd045','https://www.udacity.com/course/ai-for-business-leaders--nd054','https://www.udacity.com/course/machine-learning-engineer-for-microsoft-azure-nanodegree--nd00333','https://www.udacity.com/course/privacy-engineer-nanodegree--nd325','https://www.udacity.com/course/cloud-computing-for-business-leaders-nanodegree--nd046','https://www.udacity.com/course/security-analyst-nanodegree--nd324','https://www.udacity.com/course/hybrid-cloud-engineer-nanodegree--nd321','https://www.udacity.com/course/enterprise-security-nanodegree--nd0035','https://www.udacity.com/course/security-architect-nanodegree--nd992','https://www.udacity.com/course/aiot-foundations--ud074','https://www.udacity.com/course/aws-machine-learning-foundations--ud065','https://www.udacity.com/course/introduction-to-machine-learning-using-microsoft-azure--ud00333','https://www.udacity.com/course/linear-algebra-refresher-course--ud953','https://www.udacity.com/course/machine-learning-unsupervised-learning--ud741','https://www.udacity.com/course/big-data-analytics-in-healthcare--ud758','https://www.udacity.com/course/intel-edge-AI-fundamentals-with-openvino--ud132','https://www.udacity.com/course/artificial-intelligence--ud954','https://www.udacity.com/course/data-visualization-and-d3js--ud507','https://www.udacity.com/course/machine-learning-for-trading--ud501','https://www.udacity.com/course/machine-learning--ud262','https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617','https://www.udacity.com/course/real-time-analytics-with-apache-storm--ud381','https://www.udacity.com/course/ab-testing--ud257','https://www.udacity.com/course/data-analysis-with-r--ud651','https://www.udacity.com/course/intro-to-tensorflow-lite--ud190','https://www.udacity.com/course/introduction-to-computer-vision--ud810','https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187','https://www.udacity.com/course/intro-to-artificial-intelligence--cs271','https://www.udacity.com/course/deep-learning-pytorch--ud188','https://www.udacity.com/course/aws-deepracer--ud014','https://www.udacity.com/course/intro-to-machine-learning--ud120','https://www.udacity.com/course/rapid-prototyping--ud723','https://www.udacity.com/course/product-design--ud509','https://www.udacity.com/course/app-monetization--ud518','https://www.udacity.com/course/ab-testing--ud979','https://www.udacity.com/course/classification-models--ud978','https://www.udacity.com/course/segmentation-and-clustering--ud981','https://www.udacity.com/course/time-series-forecasting--ud980','https://www.udacity.com/course/app-marketing--ud719','https://www.udacity.com/course/how-to-build-a-startup--ep245','https://www.udacity.com/course/get-your-startup-started--ud806','https://www.udacity.com/course/intro-to-data-science--ud359','https://www.udacity.com/course/database-systems-concepts-design--ud150','https://www.udacity.com/course/learn-spark-at-udacity--ud2002','https://www.udacity.com/course/data-analysis-and-visualization--ud404','https://www.udacity.com/course/cloud-native-fundamentals--ud064','https://www.udacity.com/course/hybrid-cloud-fundamentals--ud0321','https://www.udacity.com/course/differential-equations-in-action--cs222','https://www.udacity.com/course/intro-to-information-security--ud459','https://www.udacity.com/course/cyber-physical-systems-security--ud279','https://www.udacity.com/course/network-security--ud199','https://www.udacity.com/course/web-tooling-automation--ud892','https://www.udacity.com/course/responsive-web-design-fundamentals--ud893','https://www.udacity.com/course/website-performance-optimization--ud884','https://www.udacity.com/course/responsive-images--ud882','https://www.udacity.com/course/build-native-mobile-apps-with-flutter--ud905','https://www.udacity.com/course/uikit-fundamentals--ud788','https://www.udacity.com/course/building-high-conversion-web-forms--ud890','https://www.udacity.com/course/software-architecture-design--ud821','https://www.udacity.com/course/authentication-authorization-oauth--ud330','https://www.udacity.com/course/intro-to-ios-app-development-with-swift--ud585','https://www.udacity.com/course/introduction-to-operating-systems--ud923','https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615','https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012','https://www.udacity.com/course/learn-swift-programming-syntax--ud902','https://www.udacity.com/course/offline-web-applications--ud899','https://www.udacity.com/course/software-development-process--ud805','https://www.udacity.com/course/intro-to-progressive-web-apps--ud811','https://www.udacity.com/course/software-analysis-testing--ud333','https://www.udacity.com/course/computer-networking--ud436','https://www.udacity.com/course/firebase-analytics-ios--ud353','https://www.udacity.com/course/human-computer-interaction--ud400','https://www.udacity.com/course/2d-game-development-with-libgdx--ud405','https://www.udacity.com/course/intro-to-jquery--ud245','https://www.udacity.com/course/dynamic-web-applications-with-sinatra--ud268','https://www.udacity.com/course/how-to-make-a-platformer-using-libgdx--ud406','https://www.udacity.com/course/javascript-testing--ud549','https://www.udacity.com/course/object-oriented-javascript--ud711','https://www.udacity.com/course/compilers-theory-and-practice--ud168','https://www.udacity.com/course/object-oriented-programming-in-java--ud283','https://www.udacity.com/course/designing-restful-apis--ud388','https://www.udacity.com/course/gt-refresher-advanced-os--ud098','https://www.udacity.com/course/grand-central-dispatch-gcd--ud576','https://www.udacity.com/course/continuous-integration-and-deployment--ud1030','https://www.udacity.com/course/new-android-fundamentals--ud851','https://www.udacity.com/course/objective-c-for-swift-developers--ud1009','https://www.udacity.com/course/software-testing--cs258','https://www.udacity.com/course/interactive-3d-graphics--cs291','https://www.udacity.com/course/full-stack-foundations--ud088','https://www.udacity.com/course/auto-layout--ud1026','https://www.udacity.com/course/kotlin-bootcamp-for-programmers--ud9011','https://www.udacity.com/course/core-ml--ud1038','https://www.udacity.com/course/intro-to-theoretical-computer-science--cs313','https://www.udacity.com/course/data-wrangling-with-mongodb--ud032','https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352','https://www.udacity.com/course/software-debugging--cs259','https://www.udacity.com/course/deploying-a-hadoop-cluster--ud1000','https://www.udacity.com/course/server-side-swift--ud1031','https://www.udacity.com/course/programming-languages--cs262','https://www.udacity.com/course/intro-to-relational-databases--ud197','https://www.udacity.com/course/mobile-design-and-usability-for-ios--ud1034','https://www.udacity.com/course/intro-to-ajax--ud110','https://www.udacity.com/course/intro-to-algorithms--cs215','https://www.udacity.com/course/the-mvc-pattern-in-ruby--ud270','https://www.udacity.com/course/asynchronous-javascript-requests--ud109','https://www.udacity.com/course/embedded-systems--ud169','https://www.udacity.com/course/http-web-servers--ud303','https://www.udacity.com/course/advanced-android-with-kotlin--ud940','https://www.udacity.com/course/passwordless-login-solutions-for-ios--ud1028','https://www.udacity.com/course/firebase-in-a-weekend-by-google-ios--ud0351','https://www.udacity.com/course/deploying-applications-with-heroku--ud272','https://www.udacity.com/course/c-for-programmers--ud210','https://www.udacity.com/course/intro-to-backend--ud171','https://www.udacity.com/course/javascript-and-the-dom--ud117','https://www.udacity.com/course/firebase-analytics-android--ud354','https://www.udacity.com/course/google-maps-apis--ud864','https://www.udacity.com/course/mobile-design-and-usability-for-android--ud358','https://www.udacity.com/course/ios-design-patterns--ud1029','https://www.udacity.com/course/material-design-for-android-developers--ud862','https://www.udacity.com/course/data-science-interview-prep--ud944','https://www.udacity.com/course/android-interview-prep--ud241','https://www.udacity.com/course/machine-learning-interview-prep--ud1001','https://www.udacity.com/course/front-end-interview-prep--ud250','https://www.udacity.com/course/full-stack-interview-prep--ud252','https://www.udacity.com/course/data-structures-and-algorithms-in-swift--ud1011','https://www.udacity.com/course/ios-interview-prep--ud240','https://www.udacity.com/course/vr-interview-prep--ud251','https://www.udacity.com/course/data-scientist-nanodegree--nd025','https://www.udacity.com/course/machine-learning-dev-ops-engineer-nanodegree--nd0821','https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd0013','https://www.udacity.com/course/computer-vision-nanodegree--nd891','https://www.udacity.com/course/sensor-fusion-engineer-nanodegree--nd313','https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893','https://www.udacity.com/course/natural-language-processing-nanodegree--nd892','https://www.udacity.com/course/data-architect-nanodegree--nd038','https://www.udacity.com/course/robotics-software-engineer--nd209','https://www.udacity.com/course/data-streaming-nanodegree--nd029','https://www.udacity.com/course/ai-for-healthcare-nanodegree--nd320','https://www.udacity.com/course/aws-cloud-architect-nanodegree--nd063','https://www.udacity.com/course/ethical-hacker-nanodegree--nd350','https://www.udacity.com/course/flying-car-nanodegree--nd787','https://www.udacity.com/course/ai-artificial-intelligence-nanodegree--nd898','https://www.udacity.com/course/ai-engineer-using-microsoft-azure--nd073','https://www.udacity.com/course/cloud-architect-using-microsoft-azure-nanodegree--nd090','https://www.udacity.com/course/intel-edge-ai-for-iot-developers-nanodegree--nd131','https://www.udacity.com/course/secure-and-private-ai--ud185','https://www.udacity.com/course/model-building-and-validation--ud919','https://www.udacity.com/course/knowledge-based-ai-cognitive-systems--ud409','https://www.udacity.com/course/artificial-intelligence-for-robotics--cs373','https://www.udacity.com/course/reinforcement-learning--ud600','https://www.udacity.com/course/cyber-physical-systems-design-analysis--ud9876','https://www.udacity.com/course/front-end-frameworks--ud894','https://www.udacity.com/course/ios-networking-with-swift--ud421','https://www.udacity.com/course/javascript-design-patterns--ud989','https://www.udacity.com/course/android-performance--ud825','https://www.udacity.com/course/xcode-debugging--ud774','https://www.udacity.com/course/gradle-for-android-and-java--ud867','https://www.udacity.com/course/javascript-promises--ud898','https://www.udacity.com/course/client-server-communication--ud897','https://www.udacity.com/course/advanced-android-app-development--ud855','https://www.udacity.com/course/web-accessibility--ud891','https://www.udacity.com/course/browser-rendering-optimization--ud860','https://www.udacity.com/course/kotlin-for-android-developers--ud888','https://www.udacity.com/course/ios-persistence-and-core-data--ud325','https://www.udacity.com/course/introduction-to-graduate-algorithms--ud401','https://www.udacity.com/course/high-performance-computer-architecture--ud007','https://www.udacity.com/course/design-of-computer-programs--cs212','https://www.udacity.com/course/es6-javascript-improved--ud356','https://www.udacity.com/course/high-performance-computing--ud281','https://www.udacity.com/course/computability-complexity-algorithms--ud061','https://www.udacity.com/course/advanced-operating-systems--ud189','https://www.udacity.com/course/applied-cryptography--cs387','https://www.udacity.com/course/how-to-make-an-ios-app--ud607','https://www.udacity.com/course/intro-to-devops--ud611']

print(len(lis))

df = pd.DataFrame(columns=['partner_course_url', 'title', 'learn_type', 'description', 'cover_image', 'embedded_video_url', 'delivery_method', 'instruction_type', 'content', 'what_will_learn', 'prerequisites', 'target_students', 'instructor|1|name', 'instructor|1|designation', 'instructor|1|instructor_bio', 'instructor|1|instructor_image', 'instructor|2|name', 'instructor|2|designation', 'instructor|2|instructor_bio', 'instructor|2|instructor_image', 'instructor|3|name', 'instructor|3|designation', 'instructor|3|instructor_bio', 'instructor|3|instructor_image', 'instructor|4|name', 'instructor|4|designation', 'instructor|4|instructor_bio', 'instructor|4|instructor_image', 'review|1|reviewer_name', 'review|1|photo',	'review|1|review_date', 'review|1|review',	'review|1|rating',	'review|2|reviewer_name',	'review|2|photo',	'review|2|review_date',	'review|2|review',	'review|2|rating', 'corporate_sponsor_logo', 'corporate_sponsor_name', 'accreditation|1|name', 'accreditation|1|logo', 'accreditation|1|description', 'total_duration', 'total_duration_unit', 'total_video_content', 'total_video_content_unit', 'recommended_effort_per_week', 'avg_session_duration_with_instructor', 'batch|1|batch_start_date', 'batch|1|batch_end_date', 'enrollment_start_date', 'enrollment_end_date', 'level', 'languages', 'short_description', 'subtitle_languages', 'accessibilities', 'availabilities', 'pricing_type', 'currency', 'regular_price', 'sale_price', 'course_financing_available', 'finance_details', 'institute', 'personalized_teaching', 'live_class', 'job_assistance', 'internship', 'learning_mediums', 'case_based_learning', 'capstone_project'])

for i in range(0,len(lis)):
    print(i, lis[i])
    driver.get(lis[i])
    partner_course_url = lis[i]

    if(i<69):
        level = "Beginner"
    elif(i<223):
        level = "Intermediate"
    else:
        level = "Advanced"

    try:
        title = driver.find_element(By.CLASS_NAME,'contentful-hero_contentHeader__-Ubsv').find_element(By.TAG_NAME,'h1').text
        delivery_method = "Online"
        languages  = "English"
        subtitle_languages = "English"
        institute = "Udacity"
        instruction_type = "Self Paced"
        learn_type = "Certification"
        accessibilities = "Desktop, Laptop"
        availabilities = "Limited Access"
        personalized_teaching = True

    except:
        title = None
        delivery_method = None
        languages = None
        learn_type = None
        subtitle_languages = None
        institute = None
        accessibilities = None
        instruction_type = None
        personalized_teaching = None
        availabilities = None
        print("title, delivery method, languages, subtitle_languages, level, instruction_type, accessibilities, institute, learn_type")

    try:
        corporate_sponsor_logo = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/main/section[3]/div/div/div/ul/li/picture/img").get_attribute('src')
        print("corporate_sponsor_logo", corporate_sponsor_logo)
    except:
        corporate_sponsor_logo = None

    try:
        features = instructor_names = driver.find_elements(By.CLASS_NAME,'advantage-banner_features__1SXHa')
        accessibilities = "Desktop, Laptop"

        if "mobile" in features.lower():
            accessibilities += ", Mobile"

    except:
        accessibilities = None

    try:
        instructor_names = driver.find_elements(By.CLASS_NAME,'degree-instructors_instructorName__2F9E_')
        try:
            instructor_1_name = instructor_names[0].text
        except:
            instructor_1_name = None
        try:
            instructor_2_name = instructor_names[1].text
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
        instructor_designation = driver.find_elements(By.CLASS_NAME,'degree-instructors_instructorTitle__riTyz')
        try:
            instructor_1_designation = instructor_designation[0].text
        except:
            instructor_1_designation = None
        try:
            instructor_2_designation = instructor_designation[1].text
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
        instructor_bios = driver.find_elements(By.CLASS_NAME,'degree-instructors_instructorBio__2obtk')
        try:
            instructor_1_bio = instructor_bios[0].text
        except:
            instructor_1_bio = None
        try:
            instructor_2_bio = instructor_bios[1].text
        except:
            instructor_2_bio = None
        try:
            instructor_3_bio = instructor_bios[2].text
        except:
            instructor_3_bio = None
        try:
            instructor_4_bio = instructor_bios[3].text
        except:
            instructor_4_bio = None
    except:
        print("Instructor bios")

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5);")
        instructor_images=[]

        try:
            for k in range(4):
                pic = driver.find_elements(By.CLASS_NAME,"degree-instructors_instructorImage__2CM9l")[k]
                driver.execute_script("arguments[0].scrollIntoView(true);",pic)
                time.sleep(1)
                #print(pic.get_attribute('src'))
                instructor_images.append(pic.get_attribute('src'))
        except:
            pass

        try:
            instructor_1_image = instructor_images[0]
        except:
            instructor_1_image = None
        try:
            instructor_2_image = instructor_images[1]
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
        pricing = driver.find_elements(By.CLASS_NAME,'_price-card_pricingTemplate__Am1WB')[-1].find_element(By.TAG_NAME,'p').find_element(By.TAG_NAME,'ins').text
        if "free" in pricing.lower() or "₹0" in pricing.lower():
            pricing_type = "Free"
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
        print("Pricing type, regular_price, sale_price")

    try:
        prerequisites = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[2]/div/div/ul/li[3]/div/h5').text
    except:
        prerequisites = None
        print("prerequisites")
    try:
        target_students = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[11]/div/div/div[2]/div/ul[1]/li[3]/div').text
    except:
        target_students = None
        print("target_students")

    try:
        review_name_1 = driver.find_elements(By.CLASS_NAME,'_card_cardStudent__3i3EG')[0].text
    except:
        review_name_1 = None
        print("review_name_1")
    try:
        review_rating_1 = driver.find_elements(By.CLASS_NAME,'rating-stars_active__1v1eF')[0].text
    except:
        review_rating_1 = None
        print("review_rating_1")

    try:
        review_1 = driver.find_elements(By.CLASS_NAME,'_card_cardReview__2Wcmp')[0].text
        btn = driver.find_elements(By.CLASS_NAME,'_card_card__1Dg4U')[0]
        driver.execute_script("arguments[0].scrollIntoView(true);", btn);
        time.sleep(1)
        btn.click()
        time.sleep(1)
        review_date_1 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div/p').text
        #print(review_1)
        #print(review_date_1)
        btn = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/button')
        btn.click()
    except:
        review_1 = None
        review_date_1 = None
        print("review_1, review_date_1")

    try:
        review_name_2 = driver.find_elements(By.CLASS_NAME,'_card_cardStudent__3i3EG')[1].text
    except:
        review_name_2 = None
        print("review_name 2")
    try:
        review_rating_2 = driver.find_elements(By.CLASS_NAME,'rating-stars_active__1v1eF')[1].text
    except:
        review_rating_2 = None
        print("review_rating_2")

    try:
        review_2 = driver.find_elements(By.CLASS_NAME,'_card_cardReview__2Wcmp')[1].text
        btn = driver.find_elements(By.CLASS_NAME,'_card_card__1Dg4U')[1]
        driver.execute_script("arguments[0].scrollIntoView(true);", btn);
        time.sleep(1)
        btn.click()
        time.sleep(1)
        review_date_2 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div/p').text
        #print(review_2)
        #print(review_date_2)
        btn = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/button')
        btn.click()
    except:
        review_2 = None
        review_date_2 = None
        print("review_2, review_date_2")

    try:
        short_description = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[1]/div/div/div/div[2]/div/div[1]/div').text
    except:
        short_description = None
        print("short_description")

    try:
        total_duration, total_duration_unit = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[2]/div/div/ul/li[1]/div/h5').text.split(" ")
    except:
         total_duration = None
         total_duration_unit = None
         print("total_duration total_duration_unit")

    try:
        recommended_effort_per_week = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[2]/div/div/ul/li[1]/div/p').text
    except:
         recommended_effort_per_week = None
         print("recommended_effort_per_week")

    try:
        time.sleep(1)
        enrollment_end_date = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[2]/div/div/ul/li[2]/div/h5').text
        time.sleep(1)
        enrollment_end_date = datetime.strptime(enrollment_end_date, '%B %d, %Y').isoformat()
    except:
        enrollment_end_date = None
        print("enrollment_end_date")

    try:
        cont = driver.find_elements(By.CLASS_NAME,'preview_partHeader__cKyuq')
        content = ""
        for i in range(len(cont)):
            content = content + "<p><strong>Module "+ str(i+1) + "</strong>" + cont[i].text + "</p>\n"
        if(len(content)>2):
            cont = cont[0:-2]
        print("content", content,"hello")
    except:
        content = None
        print("content")

    try:
        modules = driver.find_elements(By.CLASS_NAME,'preview_partHeader__cKyuq')
        what_will_learn = ""
        for j in modules:
            what_will_learn = what_will_learn + j.text + "|"
        what_will_learn = what_will_learn[0:-1]
        #what_will_learn = re.sub('(Complimentary )?Module [0-9]+: ', '',what_will_learn)
    except:
        what_will_learn = None
        print("what_will_learn")

    try:
        description = driver.find_element(By.CLASS_NAME,'hidden-md-down').text
        print(description)
    except:
        description = None
        print("description")

    try:
        program_offerings = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/main/section[6]/div/div').text
        benefits = driver.find_element(By.CLASS_NAME,'_feature_featureBody__1RqhE').text
        if "internship" in program_offerings.lower() or "internship" in benefits.lower():
            internship = True
        else:
            internship = False
        if "career" in program_offerings.lower() or "career" in benefits.lower() or "job" in program_offerings.lower() or "job" in benefits.lower():
            job_assistance = True
        else:
            job_assistance = False

        case_based_learning = False
        if " case stud" in content.lower() or " case based" in program_offerings.lower():
            case_based_learning = True

        learning_mediums = ""
        if "hands-on" in program_offerings.lower() or "hands-on" in benefits.lower():
            learning_mediums += 'Hands-On Learning, '
        if case_based_learning:
            learning_mediums += 'Case Studies, '
        if "industry" in program_offerings.lower() or "industry" in benefits.lower():
            learning_mediums += 'Industry Exposure, '
        if(len(learning_mediums)>1):
            learning_mediums = learning_mediums[:-2]

    except:
        internship = None
        case_based_learning = None
        learning_mediums = None
        job_assistance = None
        print("internship, case_based_learning, learning_mediums, job_assistance")

    try:
        capstone_project = False
        if("capstone" in content.lower() or "capstone" in program_offerings.lower()):
            capstone_project = True
    except:
        capstone_project = None
        print("capstone_project")

    try:
        course_financing_available = False
        finance_details = driver.find_elements(By.CLASS_NAME,'_price-card_detailList__3GALp')[-1].get_attribute('innerHTML')
        course_financing_available = True
    except:
        finance_details = None
        course_financing_available = None
        print("course_financing_available")

    df = df.append({'partner_course_url':partner_course_url,'title':title,'learn_type':learn_type,'description':description,'cover_image':None,'embedded_video_url':None,'delivery_method':delivery_method,'instruction_type':instruction_type,'content':content,'what_will_learn':what_will_learn,'prerequisites':prerequisites,'target_students':target_students,'instructor|1|name':instructor_1_name,'instructor|1|designation':instructor_1_designation,'instructor|1|instructor_bio':instructor_1_bio,'instructor|1|instructor_image':instructor_1_image, 'instructor|2|name':instructor_2_name, 'instructor|2|designation':instructor_2_designation,'instructor|2|instructor_bio':instructor_2_bio,'instructor|2|instructor_image':instructor_2_image, 'instructor|3|name':instructor_3_name, 'instructor|3|designation':instructor_3_designation, 'instructor|3|instructor_bio':instructor_3_bio, 'instructor|3|instructor_image':instructor_3_image, 'instructor|4|name':instructor_4_name,  'instructor|4|designation':instructor_4_designation, 'instructor|4|instructor_bio':instructor_4_bio, 'instructor|4|instructor_image':instructor_4_image, 'review|1|reviewer_name':review_name_1,'review|1|photo':None,	'review|1|review_date':review_date_1,'review|1|review':review_1,'review|1|rating':review_rating_1,	'review|2|reviewer_name':review_name_2,	'review|2|photo':None,'review|2|review_date':review_date_2,'review|2|review':review_2, 'corporate_sponsor_logo':corporate_sponsor_logo, 'corporate_sponsor_name':None, 'accreditation|1|name':None, 'accreditation|1|logo':None, 'accreditation|1|description':None, 'review|2|rating':review_rating_2, 'total_duration':total_duration, 'total_duration_unit':total_duration_unit, 'total_video_content':None, 'total_video_content_unit':None, 'recommended_effort_per_week':recommended_effort_per_week, 'avg_session_duration_with_instructor':None, 'batch|1|batch_start_date':None, 'batch|1|batch_end_date':None, 'enrollment_start_date':None, 'enrollment_end_date':enrollment_end_date, 'level':level, 'languages':languages, 'short_description':short_description, 'subtitle_languages':subtitle_languages, 'accessibilities':accessibilities, 'availabilities':availabilities, 'pricing_type':pricing_type, 'currency':currency, 'regular_price':regular_price, 'sale_price':sale_price, 'course_financing_available':course_financing_available, 'finance_details':finance_details, 'institute':institute, 'personalized_teaching':personalized_teaching, 'live_class':None,'job_assistance':job_assistance,'internship':internship,'learning_mediums':learning_mediums,'case_based_learning':case_based_learning,'capstone_project':capstone_project}, ignore_index = True)

df.to_excel("udacity-template1.xlsx")

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


    #learn_type
    #cover_image
    #embedded_video_url
    #review_date



    #11. prerequisites detailed or short?
    #learn_type nanodegree?
    #level how to find?
    #prerequisites and target_students given as paragraphs
    #no cover image
    #pricing per month?
