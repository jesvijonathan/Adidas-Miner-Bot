# Adidas-Miner-Bot
Adidas scrapping bot v0.2

So what does it do and how does it work ?

You have to enter your adidas login details in the config.py file

***There are different ways you can use the script :***

**1. Multiple Instance Checkout -**
In this method, first you will have to maunally add the desired product to your cart only once and then run the script, which then will open multiple instances to continue with the checkout and will exit once the checkout/order is placed, here login details alone are required

**2. Product mining -**
In this method, the bot will search for the desired product with its product-code/link/release-time and will add it to your cart with the desired size & options and will proceed to checkout in multiple instance if opted in config.py

**3. Adidas Scrapping -**
In this method, the script will make a list containing the details of all the products along with its details such as links/price/availability/type/etc and will store it locally, which can be later used with data analytic tools to monitor the products


***Dependencies***
•Python3
•Selenium
•Chrome v95
•Windows OS

Works on linux too, with chromium browser & driver & setting correct path inside of the main script

So i have left a function in the script to add delivery and payment info, which you will have to add it in the config file
But if you have already entered before in your adidas account (obviously) then the payment & deliver data are not required as it will be auto filled by adidas itself with 'cash on delivery' option selected by default and will proceed to place order

Polishing the script...

Regards
