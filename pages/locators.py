from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LINK_REGISTER = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class BasketProduct():
    BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_MASSAGE = (By.CSS_SELECTOR, "div.alertinner")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div h1")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div[id='messages'] div div strong")
    COST_PRODUCT = (By.CSS_SELECTOR, "p[class='price_color']")
    COST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alert-safe p strong")
    

 
