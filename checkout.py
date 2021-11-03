from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from bagout import bagout

from config import *

import time


def checkout():
    
    driver = webdriver.Chrome("chromedriver.exe")

    print("Moving to Cart..")

    link = "https://www.adidas.co.in/cart"
    driver.get(link)
    
    time.sleep(3)
    
    print("Checking Out..")

    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/aside/div[2]/div[1]/div/div[3]/div/button/span").click()
    
    checkout_pay(driver)


def checkout_pay(driver=None):
    
    time.sleep(7)
    
    print("-Scrolling to Bottom")

    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print("-Agree to Terms")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/main/div[6]/div[1]/div/div/label/input").click()
    
    print("-Proceeding")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/main/div[7]/button").click()
    
    time.sleep(5)

    print("-Payment")
    
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cash on Delivery']"))).click() 
    print("-Cash On Delivery")

    time.sleep(1)
    
    # Remove the below comment to proceed placing an order | Disabled for safety purpose
    #wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Place Order']"))).click()
    print("-Placing Order")

    print("\nDone")


def checkout_login():
    print("CheckOut Test-")

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(bagout_link)

    print("-Running Pre Bagout")
    print("Just a Sec..")
    try:
        fsize = "//span[text()='" + str(size) + "']"
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, fsize))).click()
    except Exception as e:
        print(e)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add To Bag']"))).click()
    time.sleep(5)
    

    print("-Moving to Cart")
    link = "https://www.adidas.co.in/cart"
    driver.get(link)
    
    time.sleep(3)
    
    print("-Checking Out")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/aside/div[2]/div[1]/div/div[3]/div/button/span").click()
    
    print("-Filling In Login Details")
    
    username = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/aside/div[1]/div/div/form/div[2]/div/div[1]/input")))
    print("-Entering Email")
    username.clear()
    username.send_keys(email)

    pas =  driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/aside/div[1]/div/div/form/div[3]/div[2]/div[1]/input")
    print("-Entering Password")
    pas.clear()
    pas.send_keys(password)

    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/aside/div[1]/div/div/form/div[7]/button/span"))).click()
    print("-Logging In")

    time.sleep(5)

    print("-Delivery Info From Account")
    checkout_pay(driver)