import pytest
from selenium import webdriver
from urls import Urls
from data import PersonalData
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):

    if request.param == 'Chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture()
def login_driver(driver):
    login_driver = BasePage(driver)
    login_driver.switch_new_page(Urls.LOGIN_PAGE)
    login_driver.wait_hide_element(MainPageLocator.OVERLAY)
    login_driver.send_keys(MainPageLocator.EMAIL_FIELD, PersonalData.EMAIL)
    login_driver.send_keys(MainPageLocator.PASSWORD_FIELD, PersonalData.PASSWORD)
    login_driver.click_element(MainPageLocator.LOGIN_BUTTON)
    login_driver.wait_for_element(MainPageLocator.TEXT_COLLECT_BURGER)
    return driver