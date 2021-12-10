from selenium import webdriver
import time
import math

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calculate(x)
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    radiobutton = browser.find_element_by_css_selector("[for='robotCheckbox']")
    radiobutton.click()

    checkbox = browser.find_element_by_id("robotsRule")
    checkbox.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

