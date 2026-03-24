import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):
    @allure.step("Получение счетчика 'Выполнено за все время'")
    def get_total_orders(self):
        return int(self.get_text(FeedLocators.TOTAL_ORDERS))

    @allure.step("Получение счетчика 'Выполнено за сегодня'")
    def get_today_orders(self):
        return int(self.get_text(FeedLocators.TODAY_ORDERS))

    @allure.step("Получение списка номеров заказов 'В работе'")
    def get_orders_in_progress(self):
        self.wait_for_visibility(FeedLocators.ORDERS_IN_PROGRESS)
        elements = self.find_elements(FeedLocators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]

    @allure.step("Ожидание обновления счетчика 'Всего'")
    def wait_for_total_counter_to_change(self, initial_value):
        WebDriverWait(self.driver, 20).until(
            lambda d: int(d.find_element(*FeedLocators.TOTAL_ORDERS).text) > initial_value
        )

    @allure.step("Ожидание обновления счетчика 'Сегодня'")
    def wait_for_today_counter_to_change(self, initial_value):
        WebDriverWait(self.driver, 20).until(
            lambda d: int(d.find_element(*FeedLocators.TODAY_ORDERS).text) > initial_value
        )

    @allure.step("Ожидание появления номера заказа в разделе 'В работе'")
    def wait_for_order_in_work(self, order_number):
        WebDriverWait(self.driver, 30).until(
            lambda d: any(order_number in order for order in self.get_orders_in_progress())
        )