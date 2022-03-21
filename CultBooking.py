from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.set_page_load_timeout(10)
driver.get("https://palmeria.cultbooking.com/booking-test/")

today = datetime.today()
print(today)

iframe = driver.find_element(by=By.CLASS_NAME, value='chbecm-booking-engine')
driver.switch_to.frame(iframe)
search_button = driver.find_element(by=By.XPATH, value='//*[@id="searchBox"]/div/input')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(search_button)).click()

driver.switch_to.default_content()
dataLayer = driver.execute_script("return dataLayer")
event = dataLayer[5]['event']

try:
    if event == 'cult_roomsList':
        print('Data is being sent Correctly from Child Frame to Parent Frame')

except:
    print('Google Tag not working properly')

driver.quit()