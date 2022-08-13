from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
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