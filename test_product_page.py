from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
import time 
import pytest

def email_gen():
    return str(time.time()) + "@fakemail.org"

def pass_gen():
    return str(time.time())

@pytest.mark.guest_add_good_to_basket
class TestUserAddToBasketFromProductPage ():
    @pytest.mark.need_review
    @pytest.mark.parametrize('test_site', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4", "promo=offer5", "promo=offer6", pytest.param("promo=offer7", marks=pytest.mark.xfail), "promo=offer8", "promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, test_site):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{test_site}"
        page = ProductPage(browser, link)   
        page.ad_product_to_busket()
        page.solve_quiz_and_get_code()
        page.names_data_compare()
        page.cost_data_compare()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_not_be_success_message()
        page.should_be_appeared_message()
    
@pytest.mark.login_guest
class TestLoginFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.registered_guest_add_good
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()    
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email_gen(), pass_gen())
        login_page.should_be_authorized_user()
        yield browser
   
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   
        page.open()                         
        page.ad_product_to_busket()
        page.solve_quiz_and_get_code()
        page.names_data_compare()
        page.cost_data_compare()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   
        page.open()                         
        page.should_not_be_success_message()

    