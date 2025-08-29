import allure
import pytest
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage

class TestOrderList:

    @allure.title('Тест увеличения счётчика "Выполнено за всё время"')
    def test_count_orders_all_time(self, login_driver):
        order_list_page = OrderListPage(login_driver)

        with allure.step("Открыть ленту заказов и получить текущее значение счётчика 'Выполнено за всё время'"):
            order_list_page.going_in_list_order()
            old_value = order_list_page.get_count_all_time()

        with allure.step("Создать новый заказ"):
            main_page = MainPage(login_driver)
            main_page.create_order()

        with allure.step("Обновить ленту заказов и получить новое значение счётчика"):
            order_list_page.going_in_list_order()
            new_value = order_list_page.get_count_all_time()

        with allure.step("Проверить, что счётчик увеличился"):
            assert old_value < new_value


    @allure.title('Тест увеличения счётчика "Выполнено за сегодня"')
    def test_count_orders_today(self, login_driver):
        order_page = OrderListPage(login_driver)

        with allure.step("Открыть ленту заказов и получить текущее значение счётчика 'Выполнено за сегодня'"):
            order_page.going_in_list_order()
            old_value = order_page.get_count_today()

        with allure.step("Создать новый заказ"):
            main_page = MainPage(login_driver)
            main_page.create_order()

        with allure.step("Обновить ленту заказов и получить новое значение счётчика"):
            order_page.going_in_list_order()
            new_value = order_page.get_count_today()

        with allure.step("Проверить, что счётчик увеличился"):
            assert old_value < new_value


    @allure.title('Тест появления номера заказа в разделе "В работе" после оформления заказа')
    def test_display_order_(self, login_driver):
        with allure.step("Создать новый заказ и получить его номер"):
            main_page = MainPage(login_driver)
            order_id = main_page.create_order()

        with allure.step("Перейти в ленту заказов и дождаться появления заказов 'В работе'"):
            order_page = OrderListPage(login_driver)
            order_page.going_in_list_order()
            order_page.wait_order_in_work()

        with allure.step("Получить список номеров заказов в работе"):
            orders_in_work = order_page.get_id_order_in_work()

        with allure.step("Проверить, что созданный заказ появился в разделе 'В работе'"):
            assert order_id in orders_in_work