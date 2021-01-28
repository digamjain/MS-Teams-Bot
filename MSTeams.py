from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
wd = webdriver.Chrome(options=chrome_options)

stat = "..."
now = datetime.datetime.now()

def open():
    wd.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=060f4ab0-9d36-42d3-948e-4cc1f3da5e4d&&client-request-id=ffa75cbc-3cdd-4da9-923b-3a1c9cfeee91&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=433d4ab0-91d9-4b6a-9f8d-38e9e425cfa7&domain_hint=")
    #Enter Login ID
    wd.find_element_by_name("loginfmt").send_keys("LoginIdGoesHere@outlook.com")
    Next = wd.find_element_by_id("idSIButton9")
    Next.click()
    WebDriverWait(wd,15).until(lambda wd: wd.find_element_by_id("lightbox"))
    wd.implicitly_wait(5)
    #Enter Password
    wd.find_element_by_name("passwd").send_keys("PasswordGoesHere")
    wd.implicitly_wait(5)
    Next = wd.find_element_by_id("idSIButton9").click()

"""for filename in os.listdir('./LogIn'):
    if not filename.endswith(".py"):
        handle = open(os.path.join('LogIn',filename))
        file = handle.read()
        for i in file.splitlines():
            chkd = i.split("->")
            chkt = chkd[1].split("=")
            if (now.strftime("%A").casefold() == chkd[0].casefold()) and
                run()
            else:
                stat = "No Class at this time""""
def run():
    try:
        open()
        WebDriverWait(wd,100,poll_frequency=10, ignored_exceptions=[NoSuchElementException]).until(lambda wd: wd.find_element_by_class_name("active-rail"))
    except:
        wd.close()
        wd = webdriver.Chrome(options=chrome_options)
        open()

    Next = wd.find_element_by_xpath("//*[@title='5CSE4 - Python']").click()

    def goto_class():
        Next = wd.find_element_by_xpath("//*[@title='Join call with video']").click()
        Next = wd.find_element_by_xpath("//*[@title='Turn camera off']").click()
        Next = wd.find_element_by_xpath("//*[@title='Mute microphone']").click()
        Next = wd.find_element_by_class_name("button-col").click()

    hour,min=19,15

    try:
        WebDriverWait(wd,100,poll_frequency=20, ignored_exceptions=[NoSuchElementException]).until(lambda wd: wd.find_element_by_xpath("//*[@button-disabled='ctrl.disableJoinButton']"))
        goto_class()
        while(True):
            t=time.localtime()
            if (t.tm_hour>hour) or (t.tm_hour==hour and t.tm_min>=min):
                break

    except:
        try:
            wd.close()
            open()
            WebDriverWait(wd,100,poll_frequency=10, ignored_exceptions=[NoSuchElementException]).until(lambda wd: wd.find_element_by_class_name("active-rail"))
            Next = wd.find_element_by_xpath("//*[@title='5CSE4 - Python']").click()
            WebDriverWait(wd,100,poll_frequency=20, ignored_exceptions=[NoSuchElementException]).until(lambda wd: wd.find_element_by_xpath("//*[@button-disabled='ctrl.disableJoinButton']"))
            goto_class()
            while(True):
                t=time.localtime()
                if (t.tm_hour>hour) or (t.tm_hour==hour and t.tm_min>=min):
                    stat = "Class Ended"
                    break
            stat = "In Class"
        except:
            stat = "Class cancelled"
    wd.quit()

def status():
    return stat
