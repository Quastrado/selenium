from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from secret.secret import gh_token, user_agent
import os
import time

os.environ['GH_TOKEN'] = gh_token
url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', user_agent)

# Disable webdriver mode
options.set_preference('dom.webdriver.enabled', False)

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

try:
    driver.get(url=url)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()