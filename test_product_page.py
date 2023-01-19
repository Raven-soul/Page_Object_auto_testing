from .pages.product_page import ProductPage
import time 

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.ad_product_to_busket()
    page.solve_quiz_and_get_code()
    page.names_data_compare()
    page.cost_data_compare()