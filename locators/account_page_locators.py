from selenium.webdriver.common.by import By

class AccountPageLocator:
    TEXT_CHANGE_DATA = (By.XPATH, '//p[contains(text(), "В этом разделе вы можете изменить свои персональные данные")]')
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[contains(text(), "История заказов")]')
    BUT_EXIT = (By.XPATH, '//button[contains(text(), "Выход")]')
    ACTIVE_BUT_HISTORY = (By.XPATH, '//a[contains(@class, "Account_link_active__2opc9") and contains(text(), "История заказов")]')
    LAST_ORDER_IN_HISTORY = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][last()]/a[@class="OrderHistory_link__1iNby"]')
    BUT_FORGOT_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')
    BUT_LOGIN = (By.XPATH,'//button[contains(text(), "Войти")]')
    FIELD_EMAIL = (By.XPATH, '//input[@name="name"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@name="Пароль"]')