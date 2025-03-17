from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time 

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.find_element_and_enter_text(*LoginPageLocators.EMAIL_SHIELD, email)
        self.find_element_and_enter_text(*LoginPageLocators.PASSWORD_SHIELD, password)
        self.find_element_and_enter_text(*LoginPageLocators.PASSWORD_SHIELD_REPLAY, password)
        self.click(*LoginPageLocators.BUTTON_REGISTRATION)
        
        

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url ,  "URL не совпадает!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Формы для логина нет"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Формы для регистрации нет"