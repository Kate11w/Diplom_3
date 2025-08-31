import allure
import pytest
import helpers
from urls import Urls
from pages.main_page import MainPage


class TestCheckBasicFunction:

    @allure.title('Тест перехода по клику на "Конструктор"')
    def test_click_but_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step("Перейти на страницу логина"):
            main_page.going_page_login()

        with allure.step("Кликнуть по кнопке 'Конструктор'"):
            main_page.click_but_constructor()

        with allure.step("Дождаться загрузки главной страницы"):
            main_page.wait_load_main_page()

        with allure.step("Проверить, что URL соответствует главной странице"):
            assert main_page.get_current_url() == Urls.MAIN_PAGE


    @allure.title('Тест перехода по клику на раздел "Лента заказов"')
    def test_click_but_feed_order(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.going_main_page()

        with allure.step("Кликнуть по кнопке 'Лента заказов'"):
            main_page.click_but_feed_order()

        with allure.step("Дождаться загрузки страницы ленты заказов"):
            main_page.wait_load_page_feed_order()

        with allure.step("Проверить, что URL соответствует странице ленты заказов"):
            assert main_page.get_current_url() == Urls.FEED_PAGE


    @pytest.mark.parametrize('category', ['buns', 'souses','toppings'])
    @allure.title('Тест на появление всплывающего окна с деталями при клике по ингредиенту')
    def test_click_ingredient(self, driver, category):
        ingredient_locator = helpers.get_ingredient(category)
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.going_main_page()

        with allure.step(f"Скролл до ингредиента из категории '{category}'"):
            main_page.scroll_to_element(ingredient_locator)

        with allure.step("Кликнуть по ингредиенту"):
            main_page.click_ingredient(ingredient_locator)

        with allure.step("Проверить, что загрузилась карточка ингредиента"):
            assert main_page.wait_load_card_ingredient()

        with allure.step("Проверить, что URL содержит часть ссылки ингредиента"):
            current_url = main_page.get_url_page()
            expected_parts = Urls.INGREDIENT_LINK[category]
            assert any(part in current_url for part in expected_parts)


    @pytest.mark.parametrize('category', ['buns', 'souses','toppings'])
    @allure.title('Тест на закрытие окна ингредиента по крестику')
    def test_click_close_card_ingredient(self, driver, category):
        main_page = MainPage(driver)

        with allure.step(f"Открыть карточку ингредиента из категории '{category}'"):
            main_page.open_card_ingredient(category)

        with allure.step("Закрыть карточку ингредиента по крестику"):
            main_page.click_but_cross()

        with allure.step("Проверить, что карточка скрылась"):
            assert main_page.wait_hide_card_ingredient()


    @pytest.mark.parametrize('category', ['buns', 'souses', 'toppings'])
    @allure.title('Тест добавление ингредиента и увеличение счётчика этого ингредиента')
    def test_add_ingredient(self, driver, category):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.going_main_page()

        with allure.step(f"Выбрать случайный ингредиент из категории '{category}'"):
            ingredient_locator = main_page.choose_random_ingredient(category)

        with allure.step("Получить старое значение счётчика этого ингредиента"):
            old_count = main_page.get_count_element(ingredient_locator)

        with allure.step("Перетащить ингредиент в конструктор"):
            main_page.drag_and_drop_ingredient(ingredient_locator)

        with allure.step("Получить новое значение счётчика этого ингредиента"):
            new_count = main_page.get_count_element(ingredient_locator)

        with allure.step("Проверить, что счётчик увеличился"):
            assert old_count < new_count
