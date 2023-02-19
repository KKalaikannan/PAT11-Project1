# locators.py - File where all The HTML Locators are Kept


class OHRM_Locators:
    username_locator = 'username'
    password_locator = 'password'
    LoginButton_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    Alertbox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]'

class OHRM_PIM:

    Pim_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    AddEmployee_locator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
    FirstName_locator = "firstName" 
    SecondName_locator = "middleName" 
    LastName_locator = "lastName" 
    #EmpID_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    SaveButton_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

class OHRM_EmpDetails:

    EmployeeID_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'

    SearchButton_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'

    EditButton_locator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i'

    OtherID_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'

    LicenseNO_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input' 

    LicenseExpDate_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'

    SsnNum_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input' 

    SinNum_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input' 

    Nationality_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i' 

    Marital_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    
    DateofBirth_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input' 

    Gender_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'

    SaveButton1_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button' 

    Bloodgroup_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]/i' 

    SaveButton2_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button' 
    
    Married_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'

    B_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'

    NationalityIndian_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
  
class OHRM_DeleteEmp:

    CheckBox_locator='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span/i'
    DeleteButton_locator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button'