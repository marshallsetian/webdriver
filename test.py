#!/usr/bin/env python3

from selenium import webdriver
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("http://twitter.com")
time.sleep(30)
driver.quit()
print("Testing has been completed")
