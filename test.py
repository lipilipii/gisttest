from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

#command Format : python test.py File1 File2
username = sys.argv[1]
password = sys.argv[2]

def LoginGithub(username,password):
    elem = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/a[2]")
    elem[0].click()
    elem2 = driver.find_element_by_id("login_field")
    elem2.send_keys(username)
    elem3 = driver.find_element_by_id("password")
    elem3.send_keys(password)
    elem3.send_keys(Keys.ENTER)
    elemx = driver.find_element_by_xpath('//*[@id="js-flash-container"]/div/div')
    if elemx:
        return False
    else:
        print "Login github : PASSED"
        print "Go to gist page : PASSED"
        pass

def AddNewGist():
    elem4 = driver.find_elements_by_xpath('//*[@id="user-links"]/li[1]/a')
    elem4[0].click()
    elem5 = driver.find_element_by_name("gist[contents][][name]")
    elem5.send_keys('Hello.txt')
    elem6 = driver.find_element_by_class_name('CodeMirror-code')
    elem6.send_keys('Hello World')
    elem7 = driver.find_element_by_name("gist[public]")
    elem7.click()
    print "Add new gist : PASSED"

def EditGist():
    elem8 = driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[1]/a')
    elem8.click()
    elem9 = driver.find_element_by_class_name('CodeMirror-code')
    elem9.send_keys('Edited')
    elem9.send_keys(Keys.ENTER)
    elem10 = driver.find_element_by_xpath("//button[contains(.,'Update public gist')]")
    elem10.click()
    print "Edit gist : PASSED"

def DeleteGist():
    elem11 = driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[2]/form/button')
    elem11.click()
    obj = driver.switch_to.alert
    obj.accept()
    print "Delete gist : PASSED"

def ViewGist():
    elem12 = driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[2]/nav/a')
    if elem12:
        print "View all gist : PASSED"

driver = webdriver.Chrome()
driver.get("http://gist.github.com")
if LoginGithub(username,password):
    AddNewGist()
    EditGist()
    DeleteGist()
    ViewGist()
else:
    print "Login to Github : FAILED"
driver.close()