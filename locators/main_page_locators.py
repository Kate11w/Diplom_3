from selenium.webdriver.common.by import By

class MainPageLocator:
    OVERLAY = (By.XPATH, '//div[@class="Modal_modal__P3_V5"]/div[@class="Modal_modal_overlay__x2ZCr"]')
    TEXT_COLLECT_BURGER = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
    TEXT_ORDER_LIST = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')
    BUTTON_CONSTRUCTOR = (By.XPATH, '//a[@href="/"]/descendant::p[contains(text(), "Конструктор")]')
    BUTTON_ORDER_LIST = (By.XPATH, '//a[@href="/feed"]')
    HEAD_INGREDIENT_DETAIL = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    BUTTON_CROSS = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    BURGER_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]')
    BUTTON_CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    INGREDIENT_LOCATOR = {
        "buns": [
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')
        ],

        "souses": [
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa74"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa75"]')
        ],

        "toppings": [
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa71"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa76"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa77"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa78"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa79"]'),
            (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa7a"]')
        ]
    }