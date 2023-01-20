from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
import time 
import pytest

def email_gen():
    return str(time.time()) + "@fakemail.org"

def pass_gen():
    return str(time.time())

class TestUserAddToBasketFromProductPage ():
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

    