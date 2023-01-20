from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest
import time 

@pytest.mark.login_guest
class TestLoginFromMainPage():    
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        # реализация теста
        return 10

    def test_guest_should_see_login_link(self, browser):
        # реализация теста
        return 10
