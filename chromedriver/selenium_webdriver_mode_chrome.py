from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from secret.secret import user_agent
import time

url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')

# Disable webdriver mode

# For older ChromeDriver under version 79.0.3945.16
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

# For Chromdriver version 79.0.3945.16 or over
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    driver.get(url=url)
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

