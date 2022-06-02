from selenium.webdriver.common.by import By
import time

class LoginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_sidebar_xpath = "//button[@id='react-burger-menu-btn']"
    button_logout_id = "logout_sidebar_link"
    
    def __init__(self,driver) -> None:
        self.driver = driver
    
    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
    
    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear() 
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.ID,self.button_login_id).click()
    def clickLogout(self):
        self.driver.find_element(By.XPATH,self. button_sidebar_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID,self. button_logout_id).click()
        
        