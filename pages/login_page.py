from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "login missing in search string"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        emailLine = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        pass1Line = self.browser.find_element(*LoginPageLocators.PASS1_INPUT)
        pass2Line = self.browser.find_element(*LoginPageLocators.PASS2_INPUT)

        emailLine.send_keys(email)
        pass1Line.send_keys(password)
        pass2Line.send_keys(password)

        self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON).click()
