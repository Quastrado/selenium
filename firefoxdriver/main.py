from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import os
import time

os.environ['GH_TOKEN'] = "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"
url = 'https://www.vk.com'
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get(url=url)
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()