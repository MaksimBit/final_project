from .base_page import BasePage
from .locators import BasketProduct
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    def sould_be_empty_basket_massage(self):
        assert self.is_element_present(*BasketProduct.EMPTY_BASKET), "Сообщения нет, скорее всего корзина не пуста !!!"

    def sould_be_empty_basket(self):
        assert self.is_not_element_present(*BasketProduct.PRODUCT_IS_HAVE), "Корзина не пуста, в ней есть товар !!!"

