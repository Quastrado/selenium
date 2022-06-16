from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from secret.secret import gh_url, gh_login, gh_password, user_agent
import time

url = gh_url

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    driver.get(url=url)
    time.sleep(5)
    login_field = driver.find_element(By.ID, 'login_field')
    time.sleep(2)
    login_field.clear()
    login_field.send_keys(gh_login)
    password_field = driver.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(gh_password)
    password_field.send_keys(Keys.ENTER)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

