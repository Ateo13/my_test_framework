from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")