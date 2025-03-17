from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.after_basket import ProductInBasket
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest
import time

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])



#def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()
#    after_add_page = ProductInBasket(browser, browser.current_url)
#    after_add_page.product_in_basket()

#@pytest.mark.xfail
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_basket()
#   after_add_page = ProductInBasket(browser, browser.current_url)
#    after_add_page.should_not_be_success_message()



# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     after_add_page = ProductInBasket(browser, browser.current_url)
#     after_add_page.should_be_success_message()


# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.sould_be_empty_basket_massage()
#     basket_page.sould_be_empty_basket()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open() 
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.sould_be_empty_basket_massage()
#     basket_page.sould_be_empty_basket()



@pytest.mark.user_quest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email = str(time.time()) + "@mail.ru", password="qwerty2015")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        after_add_page = ProductInBasket(browser, browser.current_url)
        after_add_page.product_in_basket()  
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        after_add_page = ProductInBasket(browser, browser.current_url)
        after_add_page.should_not_be_success_message()

     


    


    