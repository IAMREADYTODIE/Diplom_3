import allure
from pages.constructor_page import ConstructorPage
from data import Urls

@allure.feature("Ингредиенты")
class TestIngredient:

    @allure.title("Появление всплывающего окна с деталями при клике на ингредиент")
    def test_ingredient_modal_open(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_url(Urls.BASE_URL)
        constructor_page.click_ingredient()
        assert constructor_page.is_modal_displayed()

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_ingredient_modal_close(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_url(Urls.BASE_URL)
        constructor_page.click_ingredient()
        constructor_page.close_modal()
        assert constructor_page.is_modal_closed()

    @allure.title("Увеличение счетчика при добавлении ингредиента в заказ")
    def test_ingredient_counter_increases(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_url(Urls.BASE_URL)
        constructor_page.add_ingredient_to_basket()
        # Булки добавляются парой (верхняя и нижняя), поэтому ожидаем "2"
        assert constructor_page.get_ingredient_counter() == "2"