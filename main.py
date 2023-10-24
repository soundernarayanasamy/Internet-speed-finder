import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USER_NAME = REPLACE YOUR USER_NAME
PASSWORD = REPLACE YOUR PASSWORD
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)
driver.get("https://www.speedtest.net/")
time.sleep(2)
continue_button = driver.find_element(By.ID, value="onetrust-accept-btn-handler")
continue_button.click()

time.sleep(2)
go = driver.find_element(By.CLASS_NAME, "start-text")
go.click()

time.sleep(59)

upload = driver.find_element(By.CLASS_NAME, "upload-speed")
download = driver.find_element(By.CLASS_NAME, "download-speed")
up = str(upload.text)
down = str(download.text)
driver.close()

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_option)
driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
time.sleep(3)
user_name = driver.find_element(By.CSS_SELECTOR, value='input')
user_name.click()
user_name.send_keys(USER_NAME)

next_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
next_button.click()

time.sleep(2)
password = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.click()
password.send_keys(PASSWORD)
time.sleep(3)
login_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
login_button.click()

time.sleep(10)

post_but = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
post_but.click()
time.sleep(5)
but = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
but.click()
but.send_keys(f"Hey Internet Provider, My Upload speed is {up} and Download speed is {down}.")
time.sleep(5)

utton = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div')
utton.click()
