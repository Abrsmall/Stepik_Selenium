from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
action = ActionChains(browser)

try:
    browser.get(link)
    num_1 = int(browser.find_element(By.ID, "num1").text)    # get_attribute('valuex')
    num_2 = int(browser.find_element(By.ID, "num2").text)
    summary = num_1 + num_2
    select = Select(browser.find_element(By.ID, 'dropdown'))
    # time.sleep(2)
    select.select_by_visible_text(str(summary))
    element = browser.find_element(By.TAG_NAME, "button")
    element.click()
except NoSuchElementException:
    print('Hello world')
finally:
    alert_obj = browser.switch_to.alert
    msg = alert_obj.text
    print(msg)
    browser.quit()
