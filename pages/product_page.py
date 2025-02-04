from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_added_thing_in_basket(self):
        self.add_to_basket()
        self.should_be_thing_in_basket()
        self.should_be_same_price()

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        button_add_to_basket.click()

    def return_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.MAIN_BOOK_NAME)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def should_be_thing_in_basket(self, book_name):
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME)
        assert book_name == alert_book_name.text, "book name is {}, but alert book name is {}".format(book_name, alert_book_name.text)
        # main_book_name = self.browser.find_element(*ProductPageLocators.MAIN_BOOK_NAME)
        #assert main_book_name.text == alert_book_name.text, "book name is {}, but alert book name is {}".format(main_book_name.text, alert_book_name.text)

    def should_be_same_price(self, book_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == book_price, "basket prise is {}, but book price is {}".format(basket_price.text, book_price)
        # book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        # assert basket_price.text == book_price.text, "basket prise is {}, but book price is {}".format(basket_price.text, book_price.text)