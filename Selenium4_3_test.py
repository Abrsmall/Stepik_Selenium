# Курс Selenium (https://stepik.org/lesson/184253/step/6?unit=158843), раздел 2.3, задание 3

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
action = ActionChains(driver)
driver.implicitly_wait(3)

try:
    driver.get(link)
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    first_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x = driver.find_element(By.ID, 'input_value').text
    value = str(math.log(abs(12 * math.sin(int(x)))))
    in_put = driver.find_element(By.ID, 'answer')
    in_put.send_keys(value)
    submit = driver.find_element(By.CSS_SELECTOR, 'button')
    submit.click()
except NoSuchElementException:
    print('Element not found')
finally:
    alert_obj = driver.switch_to.alert
    msg = alert_obj.text
    print(msg)
    driver.quit()
