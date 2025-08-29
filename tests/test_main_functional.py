import allure
import pytest
import helpers
from urls import Urls
from pages.main_page import MainPage


class TestCheckBasicFunction:
    @allure.title('Тест перехода по клику на "Конструктор"')
    def test_click_but_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.going_page_login()
        main_page.click_but_constructor()
        main_page.wait_load_main_page()
        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title('Тест перехода по клику на раздел "Лента заказов"')
    def test_click_but_feed_order(self, driver):
        main_page = MainPage(driver)
        main_page.going_main_page()
        main_page.click_but_feed_order()
        main_page.wait_load_page_feed_order()
        assert main_page.get_current_url() == Urls.FEED_PAGE

    @pytest.mark.parametrize('category', ['buns', 'souses','toppings']) # не работает
    @allure.title('Тест на появление всплывающего окна с деталями при клике по ингредиенту')
    def test_click_ingredient(self, driver, category):
        ingredient_locator = helpers.get_ingredient(category)
        main_page = MainPage(driver)
        main_page.going_main_page()
        main_page.scroll_to_element(ingredient_locator)
        main_page.click_ingredient(ingredient_locator)
        assert main_page.wait_load_card_ingredient()
        current_url = main_page.get_url_page()
        expected_parts = Urls.INGREDIENT_LINK[category]
        assert any(part in current_url for part in expected_parts)

    @pytest.mark.parametrize('category', ['buns', 'souses','toppings'])
    @allure.title('Тест на закрытие окна ингредиента по крестику')
    def test_click_close_card_ingredient(self, driver, category):
        main_page = MainPage(driver)
        main_page.open_card_ingredient(category)
        main_page.click_but_cross()
        assert main_page.wait_hide_card_ingredient()

    @pytest.mark.parametrize('category', ['buns', 'souses', 'toppings'])
    @allure.title('Тест добавление ингредиента и увеличение счётчика этого ингредиента')
    def test_add_ingredient(self, driver, category):
        main_page = MainPage(driver)
        main_page.going_main_page()
        ingredient_locator = main_page.choose_random_ingredient(category)
        old_count = main_page.get_count_element(ingredient_locator)
        main_page.drag_and_drop_ingredient(ingredient_locator)
        new_count = main_page.get_count_element(ingredient_locator)
        assert old_count < new_count

