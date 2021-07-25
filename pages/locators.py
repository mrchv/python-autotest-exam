from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div h1")
    ADDED_TO_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong[1]")
    BASKET_AMOUNT = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    BOOK_AMOUNT = (By.CSS_SELECTOR, "div > p.price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")