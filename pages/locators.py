from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BUCKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    MESSAGE_NAME = (By.CSS_SELECTOR, "div.alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group > a')


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
