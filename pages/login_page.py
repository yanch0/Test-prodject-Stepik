import time
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert "login" in str(self.browser.current_url), "Cant find this word"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element_by_name("registration-email").send_keys(email)
        password = "123456jojot"
        self.browser.find_element_by_name("registration-password1").send_keys(password)
        self.browser.find_element_by_name("registration-password2").send_keys(password)
        self.browser.find_element_by_name("registration_submit").click()


