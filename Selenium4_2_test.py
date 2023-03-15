# Курс Selenium (https://stepik.org/lesson/184253/step/4?unit=158843), раздел 2.3, задание 2

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
action = ActionChains(driver)

try:
    driver.get(link)
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    alert_obj = driver.switch_to.alert
    alert_obj.accept()
    x = driver.find_element(By.ID, 'input_value').text
    value = str(math.log(abs(12 * math.sin(int(x)))))
    answ = driver.find_element(By.ID, 'answer')
    answ.send_keys(value)
    submit = driver.find_element(By.CSS_SELECTOR, 'button')
    submit.click()
except NoSuchElementException:
    print('Element not found')
finally:
    alert_obj = driver.switch_to.alert
    msg = alert_obj.text
    print(msg)
    driver.quit()
