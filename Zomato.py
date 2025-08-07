import selenium.common
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import random
import pickle
import pyttsx3
import sys
from selenium.webdriver import ActionChains

engine = pyttsx3.init()
def random_time(num1=200, num2=300):
    time.sleep(random.randrange(num1, num2) / 100)
def speak(data):
    engine.say(data)
    engine.runAndWait()
def inp(name_string):
    while True:
        a = input(f"Enter {name_string} name: ")
        if (a!=""):
            try:
                a = int(a)
            except:
                return a
                break
            else:
                print("Please dont enter a number")
        else:
            print("Please enter a valid string")

city = inp("City")
name_of_rest = inp("Restaurent")


driver = webdriver.Chrome()
url = "https://www.zomato.com/india"




wait = WebDriverWait(driver, 10)
driver.get(url)
random_time(500, 600)
with open("Cookies.pkl", "rb") as file:
    cookie = pickle.load(file)
#https://www.zomato.com/ahmedabad/restaurants
#https://www.zomato.com/india/ahmedabad/restaurants
for i in cookie:
    driver.add_cookie(i)

random_time(300, 400)

driver.get(f"https://www.zomato.com/{city.lower()}/restaurants")
random_time()

search = wait.until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Search for restaurant, cuisine or a dish']")))
search.click()
search.send_keys(name_of_rest)
random_time()
near_restaurent = driver.find_element(By.XPATH, "//img[@alt = 'Restaurant Image']")
random_time(800, 1200)
near_restaurent.click()
random_time(400, 500)
try:
    pizzas = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), '₹')]")))
except selenium.common.TimeoutException:
    print("Sir no order is being shown in this restuarent")
    sys.exit()

print("Len: ", len(pizzas))
data = []
file_no = 1
while True:
    try:
        with open(f"Data_{name_of_rest}_{file_no}.csv", "w", newline="", encoding="utf-8") as file12:
            writer = csv.writer(file12)
            writer.writerow(["Url: ", driver.current_url])
            writer.writerow(["Name", "Price", "Desciption"])
            for i in range(0, len(pizzas) - 1):
                try:
                    name = pizzas[i].find_element(By.XPATH, "./parent::div/preceding-sibling::h4")
                    paragraph = name.find_element(By.XPATH, "./parent::div/parent::div/following-sibling::p")
                    try:
                        paragraph.find_element(By.XPATH, "./child::span").click()
                    except Exception as a:
                        pass
                    print(name.text)
                    data.append(name.text)
                    print(pizzas[i].text)
                    data.append(pizzas[i].text.replace("₹", "") + " rupee")
                    print("Description:", paragraph.text)
                    data.append(paragraph.text)
                    writer.writerow(data)
                    data = []
                except Exception as e:
                    print(e)
                    speak("Sir error")
                    input()
    except PermissionError as error:
        file_no += 1
    else:
        break
print(driver.current_url)
driver.quit()