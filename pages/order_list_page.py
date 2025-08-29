import allure
from urls import Urls
from locators.main_page_locators import MainPageLocator
from locators.order_list_page_locators import OrderListLocator

from pages.base_page import BasePage

class OrderListPage(BasePage):

    @allure.step('Переход на страницу "Лента заказов"')
    def going_in_list_order(self):
        self.switch_new_page(Urls.FEED_PAGE)

    @allure.step('Подождать появления номера заказа в разделе "В работе"')
    def wait_order_in_work(self):
        return self.wait_change_element(OrderListLocator.ORDER_IN_WORK_1, 'Все текущие заказы готовы!')

    @allure.step('Получить количества заказов за все время')
    def get_count_orders(self, locator):
        count_orders = self.wait_for_element(locator)
        return count_orders.text

    @allure.step('Получение списка заказов из раздела "В работе"')
    def get_id_order_in_work(self):
        elements = self.wait_load_all_elements(OrderListLocator.ORDER_IN_WORK)
        orders_in_work = [element.text.lstrip('0') for element in elements]
        return orders_in_work

    @allure.step('Получить значение счётчика "Выполнено за всё время"')
    def get_count_all_time(self):
        return self.get_count_orders(OrderListLocator.COUNT_ORDERS_ALL_TIME)

    @allure.step('Получить значение счётчика "Выполнено за сегодня"')
    def get_count_today(self):
        return self.get_count_orders(OrderListLocator.COUNT_ORDERS_TODAY)

    @allure.step('Подождать загрузки карточки заказа')
    def wait_load_order_card(self):
        return self.wait_for_element(OrderListLocator.ORDER_CARD)

    @allure.step('Подождать загрузки страницы ленты заказов')
    def wait_load_page_feed_order(self):
        self.wait_for_element(MainPageLocator.TEXT_ORDER_LIST)

    @allure.step('Получить текущего URL страницы')
    def get_url_page(self):
        return self.switch_new_page()