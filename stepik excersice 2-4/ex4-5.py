import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
browser.find_elements_by_id("button")