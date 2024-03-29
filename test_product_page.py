import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

url_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "qwerty"
        login_page.register_new_user(email=email, password=password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = url_product
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [0])  # , 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    def test_user_can_add_product_to_basket(self, browser, link):
        link = f"{url_product}?promo=offer{link}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_product_name_to_be_the_same()
        page.should_price_to_be_the_same()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_product_name_to_be_the_same()
    page.should_price_to_be_the_same()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = url_product
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = url_product
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_list()
    basket_page.should_be_empty_basket_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = url_product
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = url_product
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = url_product
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
