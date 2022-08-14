import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver

# result = ''
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#     print(result)

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    #global result
    link = f"https://stepik.org/lesson/{number}/step/1/"
    browser.implicitly_wait(10)
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element(By.XPATH, '//textarea').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    check_success_text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert 'Correct!' == check_success_text

    # try:
    #     assert 'Correct!' == check_success_text
    # except AssertionError:
    #     result += check_success_text
