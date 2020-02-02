from .base_page import BasePage
from .locators import ProductPageLocators
import pytest
class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_not_be_success_message()
        self.should_be_add_basket_button()
        self.should_add_product_into_basket()
        self.solve_quiz_and_get_code()
        self.should_be_price_info()
        self.should_be_book_price_value()
        self.basket_price_equal_product_price()
        self.should_be_book_name_value()
        self.should_be_book_name_info()
        self.info_message_contains_product_name()
        self.should_disapeared_message()


    @pytest.mark.xfail
    def basket_price_equal_product_price(self):
        assert self.get_text(*ProductPageLocators.PRICE_LABEL) == self.get_text(*ProductPageLocators.PRICE_MESSAGE), "Product name in message doesn't equal product name"

    def info_message_contains_product_name(self):
        assert self.get_text(*ProductPageLocators.PRODUCT_NAME_LABEL) == self.get_text(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "Price in basket doesn't equal product price"

    def should_add_product_into_basket(self):
        assert self.button_click(*ProductPageLocators.ADD_BASKET_BUTTON), "Add_basket_button is not presented"

    def should_be_add_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Add_basket_button is not presented"

    def should_be_price_info(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), "Book price message is not presented"

    def should_be_book_name_info(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "Book name message is not presented"

    def should_be_book_price_value(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_LABEL), "Book price value is not presented"

    def should_be_book_name_value(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_LABEL), "Book name value is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    @pytest.mark.xfail
    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message disapeared"


