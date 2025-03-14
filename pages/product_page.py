from .base_page import BasePage
from .locators import BasketProduct
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    
    def add_to_basket(self):
        login_link = self.browser.find_element(*BasketProduct.BASKET_LINK)
        login_link.click()
    







