from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import time

url = 'https://www.google.com'
user_agent_url = 'http://n5m.ru/usagent.html'
options = webdriver.ChromeOptions()
user_agent = UserAgent()
options.add_argument(f'user-agent={user_agent.random}')
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    driver.get(url=user_agent_url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

