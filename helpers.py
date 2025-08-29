import random
from locators.main_page_locators import MainPageLocator
from selenium.webdriver.common.by import By

def get_ingredient(category: str):
    return random.choice(MainPageLocator.INGREDIENT_LOCATOR[category])

def get_order_locator(href):
    return By.XPATH, f'//a[contains(@href, "{href}")]'