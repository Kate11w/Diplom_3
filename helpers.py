import random
from locators.main_page_locators import MainPageLocator


def get_ingredient(category: str):
    return random.choice(MainPageLocator.INGREDIENT_LOCATOR[category])
