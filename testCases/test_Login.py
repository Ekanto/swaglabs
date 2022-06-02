from selenium import webdriver
from importlib.resources import path
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils
import pytest
import time
import pandas as pd
import xlrd
import time
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = ".//TestData/LoginData.xlsx"
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_title(self,setup):
        self.logger.info("*****Test_001_Login*****")
        self.logger.info("*****Starting test*****")
        self.logger.info("*****Verifiying title*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("*****Title test passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login_page_title.png")
            self.driver.close()
            self.logger.error("*****Title test failed*****")
            assert False
            
            
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.logger.info("********Test_001_login********")
        self.logger.info("*****Starting test*****")
        self.logger.info("*****Verifiying Log in credentials*****")
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.file = pd.ExcelFile(self.path)
        self.df = self.file.parse("Sheet1")
        self.dim = self.df.shape
        self.row = self.dim[0]
        
        lst_status=[]
        
        for i in range(2,self.row+2):
            self.username = XLUtils.readData(self.path,'Sheet1',i,1)
            self.password = XLUtils.readData(self.path,'Sheet1',i,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',i,3)
            self.login.setUserName(self.username)
            print(self.username)
            self.login.setPassword(self.password)
            self.login.clickLogin()
            cur_url = self.driver.current_url
            act_title = self.driver.title
            exp_title = "Swag Labs"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Pass")
                    self.login.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Fail")
                    # self.login.clickLogout()
                    lst_status.append("Pass")
            elif act_title!=exp_title:
                if self.exp == "Pass":
                    self.logger.info("Fail")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Pass")
                    lst_status.append("Pass")
            
        if "Fail" not in lst_status:
            self.logger.info("All test cases executed successfully")
            self.driver.close()
            assert True
        else:
            self.logger.info("Test case execution failed")
            self.driver.close()
            assert False
        
        