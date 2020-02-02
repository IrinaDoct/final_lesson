from .base_page import BasePage
from .locators import BasketPageLocators
import pytest


class BasketPage(BasePage):

    def should_be_empty_basket_text(self):
        assert  self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT) , "Text 'empty basket' is not presented "

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMERY), "Login link is not presented"


