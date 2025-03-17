from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LINK_REGISTER = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    EMAIL_SHIELD = (By.CSS_SELECTOR, "input[type='email'][name='registration-email']")
    PASSWORD_SHIELD = (By.CSS_SELECTOR, "input[type='password'][name='registration-password1']")
    PASSWORD_SHIELD_REPLAY = (By.CSS_SELECTOR, "input[type='password'][name='registration-password2']")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR,"button[name='registration_submit']")


class BasketProduct():
    BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_MASSAGE = (By.CSS_SELECTOR, "div.alertinner")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div h1")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div[id='messages'] div div strong")
    COST_PRODUCT = (By.CSS_SELECTOR, "p[class='price_color']")
    COST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alert-safe p strong")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div p")
    PRODUCT_IS_HAVE = (By.CSS_SELECTOR,"h2[class='col-sm-6 h3']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    MAIN_BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    
    

 
