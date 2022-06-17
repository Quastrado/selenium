from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from secret.secret import gh_token, yandex_url, yandex_login, yandex_password, user_agent
import os
import time
import pickle

os.environ['GH_TOKEN'] = gh_token
url = yandex_url
options = webdriver.FirefoxOptions()
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

try:
    # driver.get(url=url)
    # time.sleep(4)
    # login_by_mail = driver.find_element(By.CLASS_NAME, 'Button2')
    # login_field = driver.find_element(By.NAME, 'login')
    # time.sleep(2)
    # login_field.clear()
    # login_field.send_keys(yandex_login)
    # login_field.send_keys(Keys.ENTER)
    # time.sleep(2)
    # password_field = driver.find_element(By.NAME, 'passwd')
    # password_field.clear()
    # time.sleep(3)
    # password_field.send_keys(yandex_password)
    # password_field.send_keys(Keys.ENTER)
    # time.sleep(7)
    # account_button = driver.find_element(By.CLASS_NAME, 'user-account')
    # account_button.click()
    # time.sleep(3)
    # exit_button = driver.find_element(By.CLASS_NAME, 'legouser__menu-item_action_exit')
    # exit_button.click()
    # time.sleep(3)
    # pickle.dump(driver.get_cookies(), open(f'{yandex_login}_cookies', 'wb'))

    # After logging in and saving cookies (Does not work in this case)

    driver.get(yandex_url)
    time.sleep(5)

    for cookie in pickle.load(open(f'{yandex_login}_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()