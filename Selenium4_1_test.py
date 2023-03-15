# Курс Selenium (https://stepik.org/lesson/228249/step/8?unit=200781), раздел 2.2, задание 3

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os


def get_file_path(file_name):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_dir, file_name)
    return path


driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
action = ActionChains(driver)
file_path = get_file_path('file.txt')

try:
    driver.get(link)
    f_n = driver.find_element(By.NAME, 'firstname')
    f_n.send_keys('Name')
    l_n = driver.find_element(By.NAME, 'lastname')
    l_n.send_keys('Lastname')
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('mail@mail.ru')
    add_file = driver.find_element(By.NAME, 'file')
    add_file.send_keys(file_path)
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()
except NoSuchElementException:
    print('Element not found')
finally:
    alert_obj = driver.switch_to.alert
    msg = alert_obj.text
    print(msg)
    driver.quit()
