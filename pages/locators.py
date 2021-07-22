from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, ".btn-lg")
    MAIN_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, ".basket-items")