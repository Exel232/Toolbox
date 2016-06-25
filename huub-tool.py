from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

## virtualdisplay so we dont get annoying messages
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()

def elemInsert(element, text):
    element.clear()
    element.send_keys(text)
    return

driver = webdriver.Chrome()
driver.get("https://www.ub.hu-berlin.de/de")
assert "Berlin" in driver.title
username = driver.find_element_by_name("bor_id")
password = driver.find_element_by_name("bor_verification")
pw = getpass(prompt="Insert your HU Password: ")
elemInsert(username, "HUCH02207120")
elemInsert(password, pw)
password.send_keys(Keys.RETURN)
assert "PRIMUS" in driver.title
kontoLink = driver.find_element_by_link_text('Mein Konto')
kontoLink.click()
ddObjList = []
ddObjList = driver.find_elements_by_css_selector("[id^='dueDate']")
print("Due dates for your HU Books")
for r in ddObjList:
    print(r.text)
# check if we want to prolong lend times
lendCheck = input("Increase time [y/n]: ")
if lendCheck == "y":
    lendButton = driver.find_element_by_link_text("Alle verlängern")
    lendButton.click()
    driver.implicitly_wait(1)
    lendResponse = driver.find_element_by_id('EXLMyAccountFeedbacMsg')
    time.sleep(1)
    print(lendResponse.text)
driver.close()
display.stop()
