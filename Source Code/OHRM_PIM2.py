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
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_PIM().Pim_locator).click()
        print("Login was successful!")

    def OHRM_Edit_Emp_Details(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().EmployeeID_locator).send_keys(data.Personal_Data().Employee_ID)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().SearchButton_locator).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().OtherID_locator).send_keys(data.Personal_Data().Other_ID)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().LicenseNO_locator).send_keys(data.Personal_Data().License_Number)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().LicenseExpDate_locator).send_keys(data.Personal_Data().License_ExpiryDate)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().SsnNum_locator).send_keys(data.Personal_Data().Ssn_Number)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().SinNum_locator).send_keys(data.Personal_Data().Sin_Number)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().Nationality_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().NationalityIndian_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().Marital_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().Married_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().DateofBirth_locator).send_keys(data.Personal_Data().DateofBirth)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().Gender_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().SaveButton1_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().Bloodgroup_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().B_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().SaveButton2_locator).click()
        print("Employee Details Added Sucessfully!")
        self.driver.close()

    def OHRM_Delete_Employee(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().EmployeeID_locator).send_keys(data.Personal_Data().Emp_ID)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_EmpDetails().SearchButton_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_DeleteEmp().CheckBox_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.OHRM_DeleteEmp().CheckBox_locator).click()
        print("Employee Details Deleted!")


s=OHRM_PIM()
s.login()
#s.OHRM_Edit_Emp_Details()
s.OHRM_Delete_Employee()