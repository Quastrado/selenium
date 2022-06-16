from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent
import os
import time

os.environ['GH_TOKEN'] = "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"
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