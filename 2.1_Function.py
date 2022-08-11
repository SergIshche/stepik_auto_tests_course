from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    check = browser.find_element(By.ID, 'robotCheckbox').click()

    radio = browser.find_element(By.ID, 'robotsRule').click()

    button = browser.find_element(By.CSS_SELECTOR, "button").click()

    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()