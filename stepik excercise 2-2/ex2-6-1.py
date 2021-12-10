from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
browser.find_element_by_tag_name('body').send_keys(Keys.END)