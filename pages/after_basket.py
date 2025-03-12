from .base_page import BasePage
from .locators import BasketProduct
from selenium.webdriver.common.by import By
 

class ProductInBasket(BasePage):

    def product_in_basket(self):
        self.basket_not_empty()
        self.same_name()
        self.same_costs()

    def testing(self):
        print()

    def basket_not_empty(self):
        print(self.is_element_present(*BasketProduct.BASKET_MASSAGE))
        
        assert self.is_element_present(*BasketProduct.BASKET_MASSAGE), "Корзина пуста или в ней другой товар"

    def same_costs(self):
        assert self.find_element_and_take_text(*BasketProduct.COST_PRODUCT) == self.find_element_and_take_text(*BasketProduct.COST_PRODUCT_IN_BASKET), "Стоимость товаров различна!"

    def same_name(self):
        assert self.find_element_and_take_text(*BasketProduct.NAME_PRODUCT) == self.find_element_and_take_text(*BasketProduct.NAME_PRODUCT_IN_BASKET), "Названия товаров различны!"