from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, ProductPageLocators
import time


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
       # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        # assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_basket_link(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"
        link.click()

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ELEMENT), \
        "There is items in your basket"
        assert "Your basket is empty" in self.browser.find_element(*BasePageLocators.BASKET_EMPTY). \
            get_attribute('innerHTML'), "Basket is not empty"