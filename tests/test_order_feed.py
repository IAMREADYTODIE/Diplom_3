import allure
import pytest
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from data import Urls
from locators.feed_locators import FeedLocators

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Увеличение счетчика 'Выполнено за все время' при создании заказа")
    def test_total_counter_increases(self, driver, create_user_api):
        constructor_page = ConstructorPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)

        feed_page.open_url(Urls.FEED_PAGE)
        initial_count = feed_page.get_total_orders()

        login_page.open_url(Urls.LOGIN_PAGE)
        login_page.login(create_user_api["email"], create_user_api["password"])
        constructor_page.add_ingredient_to_basket()
        constructor_page.click_place_order()
        constructor_page.get_order_number()
        constructor_page.close_modal()

        constructor_page.click_order_feed()
        feed_page.wait_for_total_counter_to_change(initial_count)
        
        assert feed_page.get_total_orders() > initial_count

    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании заказа")
    def test_today_counter_increases(self, driver, create_user_api):
        constructor_page = ConstructorPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)

        feed_page.open_url(Urls.FEED_PAGE)
        initial_count = feed_page.get_today_orders()

        login_page.open_url(Urls.LOGIN_PAGE)
        login_page.login(create_user_api["email"], create_user_api["password"])
        constructor_page.add_ingredient_to_basket()
        constructor_page.click_place_order()
        constructor_page.get_order_number()
        constructor_page.close_modal()

        constructor_page.click_order_feed()
        feed_page.wait_for_today_counter_to_change(initial_count)
        
        assert feed_page.get_today_orders() > initial_count

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_work_section(self, driver, create_user_api):
        constructor_page = ConstructorPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)

        login_page.open_url(Urls.LOGIN_PAGE)
        login_page.login(create_user_api["email"], create_user_api["password"])
        constructor_page.add_ingredient_to_basket()
        constructor_page.click_place_order()
        
        order_number = constructor_page.get_order_number()
        constructor_page.close_modal()

        constructor_page.click_order_feed()
        feed_page.wait_for_order_in_work(order_number)
        
        assert any(order_number in order for order in feed_page.get_orders_in_progress())