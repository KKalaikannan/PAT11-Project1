# app.py - The main executable file

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Locators import locators
from Data import data


class OHRM:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    def __init__(self):
        self.driver.get(data.OHRM_Data().url)
        self.driver.maximize_window()

    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.OHRM_Locators().username_locator).send_keys(data.OHRM_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.OHRM_Locators().password_locator).send_keys(data.OHRM_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_Locators().LoginButton_locator).click()
        print("Login was successful!")
        self.driver.close()

    def Invalid_login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.OHRM_Locators().username_locator).send_keys(data.OHRM_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.OHRM_Locators().password_locator).send_keys(data.OHRM_Data().Invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_Locators().Alertbox_locator).getText()
        print("Invalid credentials")
        self.driver.close()

s=OHRM()
s.login()
s.Invalid_login()



