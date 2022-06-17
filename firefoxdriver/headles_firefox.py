from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from secret.secret import gh_token, yandex_url, yandex_login, yandex_password, user_agent
import os
import time

os.environ['GH_TOKEN'] = gh_token
url = yandex_url
options = webdriver.FirefoxOptions()

# headless mode
options.headless = True

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

try:
    driver.get(url=url)
    print('open page')
    time.sleep(4)
    login_by_mail = driver.find_element(By.CLASS_NAME, 'Button2')
    login_field = driver.find_element(By.NAME, 'login')
    print('authentication')
    time.sleep(2)
    login_field.clear()
    login_field.send_keys(yandex_login)
    login_field.send_keys(Keys.ENTER)
    time.sleep(2)
    print('login')
    password_field = driver.find_element(By.NAME, 'passwd')
    password_field.clear()
    print('password')
    time.sleep(3)
    password_field.send_keys(yandex_password)
    password_field.send_keys(Keys.ENTER)
    time.sleep(7)
    print('log out')
    account_button = driver.find_element(By.CLASS_NAME, 'user-account')
    account_button.click()
    time.sleep(3)
    exit_button = driver.find_element(By.CLASS_NAME, 'legouser__menu-item_action_exit')
    exit_button.click()
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()