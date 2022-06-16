from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent
from secret.secret import gh_token
import os
import time

os.environ['GH_TOKEN'] = gh_token
url = 'https://www.vk.com'
user_agent_url = 'http://n5m.ru/usagent.html'
options = webdriver.FirefoxOptions()
user_agent = UserAgent()
options.set_preference('general.useragent.override', user_agent.random)
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

try:
    driver.get(url=user_agent_url)
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()