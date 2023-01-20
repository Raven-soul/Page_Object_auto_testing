from .base_page import BasePage
from .locators import BasketPageLocators
import math
import time 

class BasketPage(BasePage): 
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BRODUCT_LIST), "Success message is presented, but should not be"
    
    def should_be_appeared_message(self):
        assert self.is_appeared(*BasketPageLocators.BASKET_CONTINUE_LINK), "Success message is not presented, but should be appeared"