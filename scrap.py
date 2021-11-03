from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

from config import *

import time


def scrap():
    print("Scrap Test -")

    driver = webdriver.Chrome("chromedriver.exe")
    
    print("-Opening Target Page")
    driver.get(scrap_link)

    
    print("-Loading")
    time.sleep(5)

    print("-Collecting")
    elems = driver.find_elements_by_xpath("//a[@href]")
    
    print("-Cleaning\n")

    clean_elem = []
    
    for elem in elems:   
        x = elem.get_attribute("href")
        
        if "html" in x:
            print(x)
            clean_elem.append(x)

    time.sleep(1)
    print("\nDone")