# Курс Selenium (https://stepik.org/lesson/181384/step/8?unit=156009), раздел 2.4, задание 2

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
action = ActionChains(driver)

try:
    driver.get(link)
    button = driver.find_element(By.ID, 'book')
    price = WebDriverWait(driver, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button.click()
    submit = driver.find_element(By.ID, 'solve')
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit)
    x = driver.find_element(By.ID, 'input_value').text
    value = str(math.log(abs(12 * math.sin(int(x)))))
    in_put = driver.find_element(By.ID, 'answer')
    in_put.send_keys(value)
    submit.click()
except NoSuchElementException:
    print('Element not found')
finally:
    alert_obj = driver.switch_to.alert
    msg = alert_obj.text
    print(msg)
    driver.quit()
