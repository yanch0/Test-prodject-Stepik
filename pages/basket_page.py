from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_IS_NOT_EMPTY), "Success message is presented, but should not be"