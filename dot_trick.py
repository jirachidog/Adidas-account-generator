import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import math
import csv
# profile_customer_firstname
# profile_customer_lastname
# profile_customer_minagecheck
# profile_customer_email
# profile_login_password
# profile_login_newpasswordconfirm
# dwfrm_profile_customer_agreeterms
# submit1
def dot_trick(username):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@gmail.com")
    return emails
ar=sys.argv
emails = dot_trick(ar[1])
#emails=['apple.fsakhrot@gmail.com']
fname='Alex'
lname='k'
passw='abcde123'
data=[];
print (emails)
chop = webdriver.ChromeOptions()
#chromedriver = "/usr/bin/chromedriver"
#chromedriver = "/usr/local/bin/chromdriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
#chop.add_argument('--proxy-server=%s' % PROXY)
chop.add_argument('--disable-gpu')
chop.add_argument('--disable-impl-side-painting')
chop.add_argument('--disable-gpu-sandbox')
chop.add_argument('--disable-accelerated-2d-canvas')
chop.add_argument('--disable-accelerated-jpeg-decoding')
chop.add_argument('--no-sandbox')
chop.add_argument('--test-type=ui')
driver = webdriver.Chrome(chrome_options = chop)

for email in emails : 
   driver.get('https://cp.adidas.com/web/eCom/en_US/loadcreateaccount')
   time.sleep(2)
   driver.execute_script("document.getElementById('profile_customer_firstname').value='"+fname+"';")
   driver.execute_script("document.getElementById('profile_customer_lastname').value='"+lname+"';")
   driver.execute_script("document.getElementById('profile_customer_email').value='"+email+"';")
   driver.execute_script("document.getElementById('profile_login_password').value='"+passw+"';")
   driver.execute_script("document.getElementById('profile_login_newpasswordconfirm').value='"+passw+"';")
   driver.execute_script("document.getElementById('profile_customer_minagecheck').click()")
   driver.execute_script("document.getElementById('dwfrm_profile_customer_agreeterms').click();")
   driver.find_element_by_id("submit1").click()
   time.sleep(3)
   driver.delete_all_cookies() 
   data.append(email+':'+passw)
   time.sleep(3)
   driver.delete_all_cookies()
   if len(data)==int(ar[2]): 
     break

    


myfile = open(ar[3],'w')
wr = csv.writer(myfile, delimiter=';')
wr.writerows([data])
myfile.close()
driver.quit()
