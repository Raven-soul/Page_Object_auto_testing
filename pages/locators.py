from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    AD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME_STATE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_RESULT = (By.XPATH, "//div[@class='alertinner ']/strong")
    COST_PRODUCT = (By.XPATH, "//p[@class='price_color']")
    COST_BASKET = (By.CSS_SELECTOR, "div.alert-info div.alertinner p")