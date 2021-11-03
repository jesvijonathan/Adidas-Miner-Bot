from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

from config import *

import time


def bagout():

    print("Bagout Test -")
    driver = webdriver.Chrome("chromedriver.exe")

    #bagout_link = input("Enter Product Link : ")

    print("-Locating Product")
    driver.get(bagout_link)

    print("-Selecting Options")

    try:
        fsize = "//span[text()='" + str(size) + "']"
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, fsize))).click()
    except Exception as e:
        print(e, "!Size " + str(size) + " not available !")

    print("-Adding To Cart")
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add To Bag']"))).click()
    
    print("-Working On It")
    time.sleep(5)
    print("\nDone")

    return driver