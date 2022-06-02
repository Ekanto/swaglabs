from selenium import webdriver
from importlib.resources import path
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils
from pageObjects.addToCart import AddCart
import pytest
import time
import pandas as pd
import xlrd
import time
from utilities.readProperties import ReadConfig


class Test_002_AddToCart:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    username = "standard_user"
    password = "secret_sauce"
    
    @pytest.mark.regression
    def test_addToCart(self,setup):
        
        self.driver = setup
        self.logger.info("********Test_001_login********")
        self.logger.info("*****Starting test*****")
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        self.logger.info("********Login successful********")
        self.logger.info("********Adding to cart********")
        self.addCart = AddCart(self.driver)
        self.addCart.buyBag()
        self.addCart.cart()
        self.addCart.checkout()
        self.driver.close()