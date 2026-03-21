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

    @allure.step("Ожидание обновления счетчика")
    def wait_for_counter_to_change(self, locator, initial_value):
        # Ждем, пока значение счетчика станет отличным от начального
        WebDriverWait(self.driver, 20).until(
            lambda d: int(d.find_element(*locator).text) > initial_value
        )
        