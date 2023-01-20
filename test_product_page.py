from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time 
import pytest

class TestUserAddToBasketFromProductPage ():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        email = str(time.time()) + "@fakemail.org"

    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   
        page.open()                         
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)   
        page.open()                         
        page.ad_product_to_busket()
        page.solve_quiz_and_get_code()
        page.names_data_compare()
        page.cost_data_compare()