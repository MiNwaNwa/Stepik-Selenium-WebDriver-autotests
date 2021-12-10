from selenium import webdriver
import math

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

val_element = browser.find_element_by_id("input_value")
v = val_element.text

res = calculate(v)

field = browser.find_element_by_id("answer")
field.send_keys(res)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

check = browser.find_element_by_id("robotCheckbox")
check.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()


button.click()