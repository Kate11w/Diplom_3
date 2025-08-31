from selenium.webdriver.common.by import By

class OrderListLocator:
    ORDER_CARD = (By.XPATH, '//p[text()="Выполнен"]/ancestor::section[contains(@class, "Modal_modal_opened__3ISw4")]')
    COUNT_ORDERS_ALL_TIME = (By.XPATH, '//p[contains(text(), "Выполнено за все время")]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    COUNT_ORDERS_TODAY = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    ORDER_ID_AFTER_PURCHASE = (By.XPATH, '//p[contains(text(), "идентификатор заказа")]/preceding-sibling::h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    ORDER_IN_WORK = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]')
    ORDER_IN_WORK_1 = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]')
