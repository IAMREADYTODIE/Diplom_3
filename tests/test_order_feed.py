import allure
import pytest
import time
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from data import Urls
from locators.feed_locators import FeedLocators

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Увеличение счетчиков при создании нового заказа")
    @pytest.mark.parametrize("counter_type", ["total", "today"])
    def test_order_counters_increase(self, driver, create_user_api, counter_type):
        constructor_page = ConstructorPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)

        feed_page.open_url(Urls.FEED_PAGE)
        initial_count = feed_page.get_total_orders() if counter_type == "total" else feed_page.get_today_orders()
        target_locator = FeedLocators.TOTAL_ORDERS if counter_type == "total" else FeedLocators.TODAY_ORDERS

        login_page.open_url(Urls.LOGIN_PAGE)
        login_page.login(create_user_api["email"], create_user_api["password"])
        constructor_page.add_ingredient_to_basket()
        constructor_page.click_place_order()
        constructor_page.get_order_number()
        constructor_page.close_modal()

        constructor_page.click_order_feed()
        feed_page.wait_for_counter_to_change(target_locator, initial_count)
        
        new_count = feed_page.get_total_orders() if counter_type == "total" else feed_page.get_today_orders()
        assert new_count > initial_count

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_work_section(self, driver, create_user_api):
        constructor_page = ConstructorPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)

        login_page.open_url(Urls.LOGIN_PAGE)
        login_page.login(create_user_api["email"], create_user_api["password"])
        constructor_page.add_ingredient_to_basket()
        constructor_page.click_place_order()
        
        # Получаем реальный номер заказа
        order_number = constructor_page.get_order_number()
        constructor_page.close_modal()

        # Переходим в ленту
        constructor_page.click_order_feed()
        
        # Умное ожидание появления номера в списке "В работе"
        from selenium.webdriver.support.wait import WebDriverWait
        WebDriverWait(driver, 30).until(
            lambda d: any(order_number in order for order in feed_page.get_orders_in_progress()),
            message=f"Заказ {order_number} не появился в списке 'В работе' за 30 секунд"
        )
        
        orders_in_progress = feed_page.get_orders_in_progress()
        assert any(order_number in order for order in orders_in_progress)