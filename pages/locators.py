from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')


class BasketPageLocators():
    BASKET_LIST = (By.CSS_SELECTOR, '.basket-title')
    BASKET_TEXT = (By.CSS_SELECTOR, "[id = content_inner]>p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_IN_BASKET = (By.CSS_SELECTOR, ' .alert:nth-child(1) strong')
    NAME_IN_CATALOG = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner > p > strong')
    PRICE_IN_CATALOG = (By.CSS_SELECTOR, '.product_main p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1)')
