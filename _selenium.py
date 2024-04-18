# Google Chrome	123.0.6312.123 (공식 빌드) (64비트) (cohort: Stable)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options = chrome_options) # "./chromedriver.exe"

browser.get("https://www.shopbalmain.com/index/order/index.html")
print("browser.get")

time.sleep(2)

id_elem = browser.find_element(By.NAME, "username")
pw_elem = browser.find_element(By.NAME, "password")
id_elem.send_keys("kipid")
pw_elem.send_keys("combascarekl12")
browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/form/b/b/button").click() # Log-in button
print("Log-in")

time.sleep(5)

browser.find_element(By.XPATH, "/html/body/div[4]/ul/li[2]/a").click() # Starting
print("Starting at the below!")
time.sleep(2)

prev_counting = "Starting (0/0)"
for i in range(45):
  while True:
    time.sleep(0.5)
    counting = browser.find_element(By.XPATH, "/html/body/section/div[2]/div[1]/p")
    if prev_counting != counting.text:
      prev_counting = counting.text
      print(f"{counting.text = }")
      browser.find_element(By.XPATH, "/html/body/section/div[2]/div[1]/a").click() # Starting click
      break
  submiting = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/form")))
  print(f"{submiting.text = }")
  time.sleep(0.5)
  submiting.submit()