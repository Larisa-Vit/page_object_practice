from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn_add.click()

    def should_product_name_to_be_the_same(self):
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text
        name_in_catalog = self.browser.find_element(*ProductPageLocators.NAME_IN_CATALOG).text
        assert name_in_catalog == name_in_basket,    "Product names are different"

    def should_price_to_be_the_same(self):
        price_in_catalog = self.browser.find_element(*ProductPageLocators.PRICE_IN_CATALOG).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price_in_catalog == price_in_basket,   "Product price is not correct"



