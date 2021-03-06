from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div [id='content_inner'] > p")
    BASKET_ELEMENT = (By.CSS_SELECTOR, "basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "[name=registration-email]")
    PASSWORD_FORM1 = (By.CSS_SELECTOR, "[name=registration-password1]")
    PASSWORD_FORM2 = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div h1")
    ADDED_TO_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong[1]")
    BASKET_AMOUNT = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    BOOK_AMOUNT = (By.CSS_SELECTOR, "div > p.price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")