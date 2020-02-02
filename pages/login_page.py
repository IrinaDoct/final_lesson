from more_itertools.more import seekable

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, f'Wrong login url {url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_email_line(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Email line is not presented"

    def should_be_password_line(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Email line is not presented"

    def should_be_repeat_registration_password_line(self):
        assert self.is_element_present(*LoginPageLocators.REPEATE_REGISTRATION_PASSWORD), "Repeate registration password line is not presented"

    def should_be_registration_password_line(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration password line is not presented"

    def should_be_registration_email_line(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email line is not presented"

    def should_be_register_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button line is not presented"


    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.should_be_registration_email_line()
        self.should_be_registration_password_line()
        self.should_be_repeat_registration_password_line()
        self.should_be_registration_email_line()
        self.set_text(*LoginPageLocators.REGISTRATION_EMAIL, email)
        self.set_text(*LoginPageLocators.REGISTRATION_PASSWORD, password)
        self.set_text(*LoginPageLocators.REPEATE_REGISTRATION_PASSWORD, password)
        self.button_click(*LoginPageLocators.REGISTER_BUTTON)
