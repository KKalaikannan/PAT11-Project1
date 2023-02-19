from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Locators import locators
from Data import data



class OHRM_PIM:
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

    def OHRM_Add_Employee(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_PIM().Pim_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_PIM().AddEmployee_locator).click()
        self.driver.find_element(by=By.NAME, value=locators.OHRM_PIM().FirstName_locator).send_keys(data.PIM_Data().FirstName)
        self.driver.find_element(by=By.NAME, value=locators.OHRM_PIM().SecondName_locator).send_keys(data.PIM_Data().SecondName)
        self.driver.find_element(by=By.NAME, value=locators.OHRM_PIM().LastName_locator).send_keys(data.PIM_Data().LastName)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_PIM().SaveButton_locator).click()
        print("Employee Added Successfully!")
        self.driver.close()


s=OHRM_PIM()
s.login()
s.OHRM_Add_Employee()




