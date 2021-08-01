from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET), "Button ADD TO BASKET is not presented"
        link.click()

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

        return str(math.log(abs(12 * math.sin(int(x)))))

    def book_is_in_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).get_attribute('innerHTML')
        added_to_basket_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET).get_attribute('innerHTML')
        assert str(added_to_basket_message) in str(book_name), "Book not in basket"
        basket_amount = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT).get_attribute('innerHTML')
        book_amount = self.browser.find_element(*ProductPageLocators.BOOK_AMOUNT).get_attribute('innerHTML')
        assert book_amount in basket_amount, "Different amount"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

