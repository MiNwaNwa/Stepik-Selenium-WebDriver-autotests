from selenium import webdriver
import time
import math

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")


    checkbox = browser.find_element_by_id("robotsRule")
    x = checkbox.get_attribute("checked")
    print("x = ", x)
    assert x is not None, "People radio is not selected by default"

    checkbox.click()

    checkbox = browser.find_element_by_id("robotsRule")
    x = checkbox.get_attribute("checked")
    print("x = ", x)
    assert x is not None, "People radio is not selected by default"


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

