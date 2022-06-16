from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get(url='https://www.youtube.com')
    input_element = driver.find_element(By.XPATH, '//input[@id="search"]')
    time.sleep(3)
    input_element.send_keys('запрос')
    time.sleep(3)
    search_button = driver.find_element(By.XPATH, '//button[@id="search-icon-legacy"]')
    search_button.click()
    time.sleep(3)
    driver.get(url='https://ru.wikipedia.org/')
    wiki_search = driver.find_element(By.CLASS_NAME, 'vector-search-box-input').send_keys('Польша')
    # search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'searchButton')))
    time.sleep(3)
    search_button = driver.find_element(By.CLASS_NAME, 'searchButton').click()
    time.sleep(3)
    driver.get(url='https://www.google.com')
    google_search = driver.find_element(By.CSS_SELECTOR, '#input')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()