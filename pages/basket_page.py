from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_link(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"
        link.click()

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ELEMENT), \
        "There is items in your basket"

    def there_is_sign_your_basket_is_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*BasePageLocators.BASKET_EMPTY). \
            get_attribute('innerHTML'), "There is not sign 'Your basket is empty'"