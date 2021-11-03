from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

from config import *

import time

import login
import checkout
import bagout
import scrap

def load_menu():
    menu_list = "\nAdidas Miner Bot v0.2\n" +\
        "\n1. Login" +\
        "\n2. Bagout" +\
        "\n3. Checkout" +\
        "\n4. Scrap" +\
        "\n0. Exit\n"

    while True:        
        sel = input(menu_list)
        if sel == "1":
            login.site_login()
        elif sel == "2":
            bagout.bagout()
        elif sel == "3":
            checkout.checkout_login()
        elif sel == "4":
            scrap.scrap()
        
        elif sel == "5":
            automation_1()

        elif sel == "j":
            try:
                import webbrowser
                webbrowser.open('https://github.com/jesvijonathan')
            except:
                pass
            
        elif sel == "0":
            exit(0)

def automation_1():
    print("\nScript Execution 1.0")

def __main__():
    if menu == 1:
        load_menu()
    elif menu == 0:
        automation_1()





if __name__ == '__main__':
    __main__()