from selenium import webdriver
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

first = browser.find_element_by_css_selector("[placeholder=\"Enter first name\"]")
first.send_keys("Po")

second = browser.find_element_by_css_selector("[placeholder=\"Enter last name\"]")
second.send_keys("Ke")

third = browser.find_element_by_css_selector("[placeholder=\"Enter email\"]")
third.send_keys("Mon")

file = os.path.abspath(os.path.dirname(__file__))
txt = os.path.join(file, "pikachu.txt")
print(txt)

snd = browser.find_element_by_id("file")
snd.send_keys(txt)

btn = browser.find_element_by_css_selector(".btn")
btn.click()
