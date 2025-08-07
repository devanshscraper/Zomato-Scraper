from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import random
import pickle
def random_time(num1=200, num2=300):
    time.sleep(random.randrange(num1, num2) / 100)

driver = uc.Chrome()
url = "https://www.zomato.com/india"
driver.get(url)

input()
with open("Cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)
driver.quit()

