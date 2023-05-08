from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 60)
driver.get('https://www.creamcrackers.nl/')
wait.until(EC.url_to_be('https://www.creamcrackers.nl/'))

#login to the page
sign_in=driver.find_element(By.CLASS_NAME, "btn btn-light-overlay show-login")
sign_in.click()
