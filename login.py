from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

from config import *

import time


def site_login():
    print("LogIn Test -")

    driver = webdriver.Chrome("chromedriver.exe")
    
    print("-Opening Login Page")
    driver.get(login)

    print("-Entering Email")
    username = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input")))
    username.clear()
    username.send_keys(email)
    
    print("-Entering Password")
    pas = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/input")
    pas.clear()
    pas.send_keys(password)

    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[5]/div/div/label/input").click()
        print("-Remember Me Checked")
    except:
        pass
    
    print("-Logging In")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[7]/button").click()
    
    #username.send_keys(email)
    print("Loading..")

    time.sleep(5)
    print("\nDone")
    
    return driver