from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")


    num1_elem = browser.find_element_by_id("num1")
    num1 = num1_elem.text
    print(num1)

    num2_elem = browser.find_element_by_id("num2")
    num2 = num2_elem.text
    print(num2)

    sum = int(num1) + int(num2)

    s=str(sum)

    print(sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

    button = browser.find_element_by_class_name("btn")
    button.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

