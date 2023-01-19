from .pages.product_page import ProductPage
import time 
import pytest

@pytest.mark.parametrize('test_site', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4", "promo=offer5", "promo=offer6", pytest.param("promo=offer7", marks=pytest.mark.xfail), "promo=offer8", "promo=offer9"])
def test_guest_can_go_to_login_page(browser, test_site):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{test_site}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.ad_product_to_busket()
    page.solve_quiz_and_get_code()
    page.names_data_compare()
    page.cost_data_compare()