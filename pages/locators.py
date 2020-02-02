from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")

class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "div.content p")
    BASKET_SUMMERY = (By.CSS_SELECTOR, "form.basket_summary")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators ():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_LABEL = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRODUCT_NAME_LABEL = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div.alert-success strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
