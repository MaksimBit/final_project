from .base_page import BasePage
from .locators import BasketProduct
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    def sould_be_empty_basket_massage(self):
        assert self.is_element_present(*BasketProduct.EMPTY_BASKET), "Сообщения нет, скорее всего корзина не пуста !!!"

    def sould_be_empty_basket(self):
        assert self.is_not_element_present(*BasketProduct.PRODUCT_IS_HAVE), "Корзина не пуста, в ней есть товар !!!"

class ProductInBasket(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketProduct.BASKET_MASSAGE), "Отображается сообщение об успешном завершении, но его не должно быть"

    def should_be_success_message(self):
        assert self.is_disappeared(*BasketProduct.BASKET_MASSAGE), "Отображается сообщение об успешном завершении"

    def product_in_basket(self):
        self.basket_not_empty()
        self.same_name()
        self.same_costs()

    def basket_not_empty(self):
        assert self.is_element_present(*BasketProduct.BASKET_MASSAGE), "Корзина пуста или в ней другой товар"

    def same_costs(self):
        assert self.find_element_and_take_text(*BasketProduct.COST_PRODUCT) == self.find_element_and_take_text(*BasketProduct.COST_PRODUCT_IN_BASKET), "Стоимость товаров различна!"

    def same_name(self):
        assert self.find_element_and_take_text(*BasketProduct.NAME_PRODUCT) == self.find_element_and_take_text(*BasketProduct.NAME_PRODUCT_IN_BASKET), "Названия товаров различны!"