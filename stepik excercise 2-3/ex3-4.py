import time
import math
from selenium import webdriver

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button1 = browser.find_element_by_css_selector(".btn")
button1.click()



alert = browser.switch_to.alert
alert.dismiss()

button1 = browser.find_element_by_css_selector(".btn")
button1.click()



alert = browser.switch_to.alert
alert.accept()

val_el = browser.find_element_by_css_selector("#input_value")
v = val_el.text

res = calculate(v)

inp = browser.find_element_by_css_selector("#answer")
inp.send_keys(res)



button2 = browser.find_element_by_class_name("btn")
button2.click()

