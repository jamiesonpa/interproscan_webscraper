import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
url = "https://www.ebi.ac.uk/interpro/"
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
driver = webdriver.Firefox(
    capabilities=cap)  # executable_path="C:\\Users\\Pierce\\Desktop\\geckodriver.exe"
driver.get(url)


with open("atrlpswithgenenames.txt") as file:
    sequences = (file.read()).split(">")

sequencetuples = []

for seq in sequences:
    seqtuplist = seq.split("\n")
    if len(seqtuplist) > 1:
        seqtuple = (seqtuplist[0], seqtuplist[1])
        sequencetuples.append(seqtuple)

print(str(len(sequencetuples)))
driver.maximize_window()

for seqtupl in sequencetuples:
    driver.execute_script("window.scrollTo(0,400)")
    element2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.notranslate.public-DraftEditor-content[role='textbox']"))).send_keys(seqtupl[1])
    advanced_options = driver.find_element_by_css_selector(
        "details[class$='css_foundation-float__columns___01 margin-bottom-medium option-style']")
    advanced_options.click()
    time.sleep(1)
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    #     (By.CLASS_NAME, "css_foundation-float__input-group-field___2c"))).send_keys(seqtupl[0])
    #     (By.CLASS_NAME, "css_foundation-float__input-group-field___2c"))).send_keys(seqtupl[0])
    titletextbox = driver.find_element_by_class_name(
        "css_foundation-float__input-group-field___2c")
    titletextbox.send_keys(seqtupl[0])
    driver.execute_script("window.scrollTo(0,1200)")
    time.sleep(1)
    submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "css_foundation-float__button-group___d7.css_foundation-float__stacked-for-small___d6 .css_foundation-float__button___9c")))
    submit_button.click()
    driver.get(url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,0)")
