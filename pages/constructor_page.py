import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators

class ConstructorPage(BasePage):
    @allure.step("Клик на 'Конструктор'")
    def click_constructor(self):
        self.click_element_js(ConstructorLocators.CONSTRUCTOR_BTN)

    @allure.step("Клик на 'Лента заказов'")
    def click_order_feed(self):
        self.click_element_js(ConstructorLocators.ORDER_FEED_BTN)

    @allure.step("Клик на ингредиент (булка)")
    def click_ingredient(self):
        self.click_element_js(ConstructorLocators.BUN_ITEM)

    @allure.step("Проверка видимости модального окна")
    def is_modal_displayed(self):
        return self.wait_for_visibility(ConstructorLocators.MODAL).is_displayed()

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click_element_js(ConstructorLocators.MODAL_CLOSE_BTN)

    @allure.step("Проверка закрытия модального окна")
    def is_modal_closed(self):
        return self.wait_for_invisibility(ConstructorLocators.MODAL)

    @allure.step("Добавление ингредиента в корзину")
    def add_ingredient_to_basket(self):
        self.drag_and_drop(ConstructorLocators.BUN_ITEM, ConstructorLocators.BASKET)

    @allure.step("Получение счетчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text(ConstructorLocators.BUN_COUNTER)

    @allure.step("Клик 'Оформить заказ'")
    def click_place_order(self):
        self.click_element_js(ConstructorLocators.ORDER_BTN)

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number(self):
        # 1. Ждем, когда само поле с номером станет видимым
        element = self.wait_for_visibility(ConstructorLocators.ORDER_NUMBER_MODAL)
        
        # 2. Ждем, когда в поле появится реальный номер (не 9999 и не пустота)
        # Увеличиваем таймаут до 30 секунд, так как бэкенд реально медленный
        WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element(*ConstructorLocators.ORDER_NUMBER_MODAL).text not in ["9999", "0", ""]
        )
        
        raw_number = element.text
        # Форматируем в 6 знаков с нулями впереди
        return raw_number.strip().zfill(6)