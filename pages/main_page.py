import allure
import helpers
from urls import Urls
from locators.order_list_page_locators import OrderListLocator
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку "Конструктор"')
    def click_but_constructor(self):
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_element(MainPageLocator.BUTTON_CONSTRUCTOR)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_but_feed_order(self):
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_element(MainPageLocator.BUTTON_ORDER_LIST)

    @allure.step('Клик на крестик в карточке ингредиента')
    def click_but_cross(self):
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_element(MainPageLocator.BUTTON_CROSS)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_but_create_order(self):
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_element(MainPageLocator.BUTTON_CREATE_ORDER)

    @allure.step('Клик на булочку/ингредиент')
    def click_ingredient(self, locator):
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_element(locator)

    @allure.step('Переход на страницу авторизации')
    def going_page_login(self):
        self.switch_new_page(Urls.LOGIN_PAGE)

    @allure.step('Переход на главную страницу')
    def going_main_page(self):
        self.switch_new_page(Urls.MAIN_PAGE)

    @allure.step('Подождать загрузки главной страницы')
    def wait_load_main_page(self):
        self.wait_for_element(MainPageLocator.TEXT_COLLECT_BURGER)

    @allure.step('Подождать загрузки карточки ингредиента')
    def wait_load_card_ingredient(self):
        return self.wait_for_element(MainPageLocator.HEAD_INGREDIENT_DETAIL)

    @allure.step("Ожидание появления номера заказа после оформления")
    def wait_load_order_card(self):
        self.wait_change_element(OrderListLocator.ORDER_ID_AFTER_PURCHASE, "9999")
        return self.get_text(OrderListLocator.ORDER_ID_AFTER_PURCHASE)

    @allure.step('Подождать загрузки страницы "Лента заказов"')
    def wait_load_page_feed_order(self):
        self.wait_for_element(MainPageLocator.TEXT_ORDER_LIST)

    @allure.step('Подождать скрытия карточки ингредиента')
    def wait_hide_card_ingredient(self):
        return self.wait_hide_element(MainPageLocator.HEAD_INGREDIENT_DETAIL)

    @allure.step('Получить текущий URL страницы')
    def get_url_page(self):
        return self.get_current_url()

    @allure.step('Открытие карточки ингредиента')
    def open_card_ingredient(self, category):
        locator = helpers.get_ingredient(category)
        self.going_main_page()
        self.scroll_to_element(locator)
        self.click_ingredient(locator)
        self.wait_load_card_ingredient()

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_and_drop_ingredient(self, locator):
        source = self.find_element(locator)
        target = self.find_element(MainPageLocator.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(source, target)

    @allure.step('Получить количество добавленных ингредиентов')
    def get_count_element(self, locator):
        return self.get_text(locator)

    @allure.step('Получить локатор случайного ингредиента')
    def choose_random_ingredient(self, category):
        return helpers.get_ingredient(category)

    @allure.step('Собрать бургер')
    def add_ingredient_in_burger(self):
        for category in ['buns', 'souses', 'toppings']:
            locator = self.choose_random_ingredient(category)
            self.drag_and_drop_ingredient(locator)

    @allure.step('Создать заказ')
    def create_order(self):
        self.going_main_page()
        self.add_ingredient_in_burger()
        self.click_but_create_order()
        return self.wait_load_order_card()
