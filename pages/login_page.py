from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_address.send_keys(email)
        password_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_1)
        password_1.send_keys(password)
        password_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_2)
        password_2.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()
