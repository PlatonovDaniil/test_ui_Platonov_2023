from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL='https://www.saucedemo.com/'
LOGIN='standard_user'
PASSWORD='secret_sauce'

def geting_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options= chrome_options)
    driver.implicitly_wait(10)
    return driver

def get_element_by_its_id(driver,locator):
    return driver.find_element(By.ID, locator)

def element_click(driver,locator):
    element = get_element_by_its_id(driver,locator)
    element.click()

def element_send_keys(driver,locator,text):
    element = get_element_by_its_id(driver,locator)
    element.send_keys(text)
def open_login_page():
    element_click(driver,'user-name')
def login(driver,login,password):
        element_send_keys(driver,'user-name',login)
        element_send_keys(driver,'password',password)
        element_click(driver,'login-button')

driver =geting_driver()
driver.get(URL)
element_click(driver,'user-name')
open_login_page()
login(driver,LOGIN,PASSWORD)
driver.quit()