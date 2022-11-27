import pytest
from .pages.product_page import ProductPage

url_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{url_product}?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_product_name_to_be_the_same()
    page.should_price_to_be_the_same()
