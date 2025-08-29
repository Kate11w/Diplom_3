import allure
import pytest
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage

class TestOrderList:
    @allure.title('Тест увеличения счётчика "Выполнено за всё время"')
    def test_count_orders_all_time(self, login_driver):
        order_list_page = OrderListPage(login_driver)
        order_list_page.going_in_list_order()
        old_value = order_list_page.get_count_all_time()
        main_page = MainPage(login_driver)
        main_page.create_order()
        order_list_page.going_in_list_order()
        new_value = order_list_page.get_count_all_time()
        assert old_value < new_value


    @allure.title('Тест увеличения счётчика "Выполнено за сегодня"')
    def test_count_orders_today(self, login_driver):
        order_page = OrderListPage(login_driver)
        order_page.going_in_list_order()
        old_value = order_page.get_count_today()
        main_page = MainPage(login_driver)
        main_page.create_order()
        order_page.going_in_list_order()
        new_value = order_page.get_count_today()
        assert old_value < new_value


    @allure.title('Тест появления номера заказа в разделе "В работе" после оформления заказа')
    def test_display_order_(self, login_driver):
        main_page = MainPage(login_driver)
        order_id = main_page.create_order()

        order_page = OrderListPage(login_driver)
        order_page.going_in_list_order()
        order_page.wait_order_in_work()
        orders_in_work = order_page.get_id_order_in_work()
        assert order_id in orders_in_work