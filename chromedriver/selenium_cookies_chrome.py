from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from secret.secret import gh_url, gh_login, gh_password, user_agent
import time
import pickle

url = gh_url

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    # driver.get(url=url)
    # time.sleep(5)
    # login_field = driver.find_element(By.ID, 'login_field')
    # time.sleep(2)
    # login_field.clear()
    # login_field.send_keys(gh_login)
    # password_field = driver.find_element(By.ID, 'password')
    # password_field.clear()
    # password_field.send_keys(gh_password)
    # password_field.send_keys(Keys.ENTER)
    # time.sleep(5)
    # pickle.dump(driver.get_cookies(), open(f'{gh_login}_cookies', 'wb'))

    # After logging in and saving cookies (Does not work in this case)

    driver.get(gh_url)
    time.sleep(5)

    for cookie in pickle.load(open(f'{gh_login}_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

