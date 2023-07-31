from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

SERVICE_PATH = "C:\Program Files (x86)\chromedriver.exe"
service = Service(SERVICE_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    english_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'langSelect-EN'))
    )
    english_button.click()
finally:
    print("Took too long to load")
    driver.quit()

try:
    cookie_accept_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Got it!'))
    )
    print(english_button)
    cookie_accept_button.click()
except:
    print("Took too long to load")
    driver.quit()

def clickr(click_per_session):
    cookie = driver.find_element(By.ID, 'wrapper').find_element(By.ID, 'game').find_element(By.ID, 'sectionLeft').find_element(By.ID, 'cookieAnchor').find_element(By.ID, 'bigCookie')

    while True:
        for _ in range(click_per_session):
            cookie.click()

        one_or_both_list = ['one', 'both']
        one_or_both_choice = random.choice(one_or_both_list)
        if one_or_both_choice == 'one':
            p_u = random.randint(0,1)
            if p_u == 0:
                available_products = driver.find_element(By.ID, 'wrapper').find_element(By.ID, 'game').find_element(By.ID, 'sectionRight').find_element(By.ID, 'store').find_element(By.ID, 'products').find_elements(By.CLASS_NAME, 'enabled')
                if len(available_products) > 0:
                    product = random.choice(available_products)
                    product.click()
            else:
                available_upgrades = driver.find_element(By.ID, 'wrapper').find_element(By.ID, 'game').find_element(By.ID, 'sectionRight').find_element(By.ID, 'store').find_element(By.ID, 'upgrades').find_elements(By.CLASS_NAME, 'enabled')
                if len(available_upgrades) > 0:
                    upgrade = random.choice(available_upgrades)
                    upgrade.click()
        else:
            available_products = driver.find_element(By.ID, 'wrapper').find_element(By.ID, 'game').find_element(By.ID, 'sectionRight').find_element(By.ID, 'store').find_element(By.ID, 'products').find_elements(By.CLASS_NAME, 'enabled')
            if len(available_products) > 0:
                product = random.choice(available_products)
                product.click()

            available_upgrades = driver.find_element(By.ID, 'wrapper').find_element(By.ID, 'game').find_element(By.ID, 'sectionRight').find_element(By.ID, 'store').find_element(By.ID, 'upgrades').find_elements(By.CLASS_NAME, 'enabled')
            if len(available_upgrades) > 0:
                upgrade = random.choice(available_upgrades)
                upgrade.click()

clickr(100)