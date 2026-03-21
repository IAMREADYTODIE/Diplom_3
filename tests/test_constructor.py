import allure
from pages.constructor_page import ConstructorPage
from data import Urls

@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor_navigation(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_url(Urls.FEED_PAGE)
        constructor_page.click_constructor()
        assert driver.current_url == Urls.BASE_URL + "/"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_click_order_feed_navigation(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_url(Urls.BASE_URL)
        constructor_page.click_order_feed()
        assert driver.current_url == Urls.FEED_PAGE