from selenium.webdriver.common.by import By

class AddCart:
    button_bag_id = "add-to-cart-sauce-labs-backpack"
    button_cart_id = "shopping_cart_container"
    button_checkout_id = "checkout"
    
    def __init__(self,driver) -> None:
        self.driver = driver
    
    def buyBag(self):
        self.driver.find_element(By.ID,self.button_bag_id).click()
    def cart(self):
        self.driver.find_element(By.ID,self.button_cart_id).click()
    def checkout(self):
        self.driver.find_element(By.ID,self.button_checkout_id).click()
        
        
        
    