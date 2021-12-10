import time
import math
from selenium import webdriver

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

but = browser.find_element_by_class_name("trollface")
but.click()

w = browser.window_handles[1]
browser.switch_to.window(w)

val = browser.find_element_by_css_selector("#input_value")
v = val.text

res = calculate(v)

inp = browser.find_element_by_id("answer")
inp.send_keys(res)

btn = browser.find_element_by_css_selector(".btn")
btn.click()