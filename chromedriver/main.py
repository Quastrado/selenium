from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://www.google.com'
user_agent_url = 'http://n5m.ru/usagent.html'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get(url=user_agent_url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

