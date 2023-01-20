from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time 

class ProductPage(BasePage): 
    def ad_product_to_busket(self):
        login_link = self.browser.find_element(*ProductPageLocators.AD_BUTTON)
        login_link.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def names_data_compare(self):
        time.sleep(2)
        resultName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_RESULT)
        stateName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_STATE)

        assert resultName.text == stateName.text, "Names don't match"

    def cost_data_compare(self):
        costProd = self.browser.find_element(*ProductPageLocators.COST_PRODUCT)
        costBask = self.browser.find_element(*ProductPageLocators.COST_BASKET)
        assert costProd.text in costBask.text, f"Costs don't match = {costBask.text};"

    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"