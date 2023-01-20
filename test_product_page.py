from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time 
import pytest

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_success_message()
    page.should_be_appeared_message()