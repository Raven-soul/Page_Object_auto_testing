from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket_page(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_BRODUCT_LIST), "Success message is presented, but should not be"
    
    def should_be_appeared_message(self):
        assert self.is_appeared(*MainPageLocators.BASKET_CONTINUE_LINK), "Success message is not presented, but should be appeared"