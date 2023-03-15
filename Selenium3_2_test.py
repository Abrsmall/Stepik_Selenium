from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
import math

link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
action = ActionChains(browser)


try:
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    answ = str(math.log(abs(12 * math.sin(int(x)))))
    input_v = browser.find_element(By.ID, 'answer')
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    robots_rule = browser.find_element(By.ID, 'robotsRule')

    input_v.send_keys(answ)
    checkbox.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robots_rule.click()
    button.click()
except NoSuchElementException:
    print('Element not found')
finally:
    alert_obj = browser.switch_to.alert
    msg = alert_obj.text
    print(msg)
    browser.quit()
