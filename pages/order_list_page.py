import allure
from urls import Urls
from locators.main_page_locators import MainPageLocator
from locators.order_list_page_locators import OrderListLocator
from pages.base_page import BasePage


class OrderListPage(BasePage):

    @allure.step('Переход на страницу "Лента заказов"')
    def going_in_list_order(self):
        self.switch_new_page(Urls.FEED_PAGE)

    @allure.step('Подождать появления заказа в разделе "В работе"')
    def wait_order_in_work(self):
        return self.wait_change_element(
            OrderListLocator.ORDER_IN_WORK_1, 'Все текущие заказы готовы!'
        )

    @allure.step('Получить количество заказов по локатору')
    def get_count_orders(self, locator):
        return self.get_text(locator)

    @allure.step('Получить список заказов из раздела "В работе"')
    def get_id_order_in_work(self):
        elements = self.wait_load_all_elements(OrderListLocator.ORDER_IN_WORK)
        return [element.text.lstrip('0') for element in elements]

    @allure.step('Получить значение счётчика "Выполнено за всё время"')
    def get_count_all_time(self):
        return self.get_count_orders(OrderListLocator.COUNT_ORDERS_ALL_TIME)

    @allure.step('Получить значение счётчика "Выполнено за сегодня"')
    def get_count_today(self):
        return self.get_count_orders(OrderListLocator.COUNT_ORDERS_TODAY)

    @allure.step('Подождать загрузки карточки заказа')
    def wait_load_order_card(self):
        return self.wait_for_element(OrderListLocator.ORDER_CARD)

    @allure.step('Подождать загрузки страницы "Лента заказов"')
    def wait_load_page_feed_order(self):
        self.wait_for_element(MainPageLocator.TEXT_ORDER_LIST)

    @allure.step('Получить текущий URL страницы')
    def get_url_page(self):
        return self.get_current_url()
