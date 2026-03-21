import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    @allure.step("Авторизация пользователя: {email}")
    def login(self, email, password):
        self.set_text(LoginLocators.EMAIL_INPUT, email)
        self.set_text(LoginLocators.PASSWORD_INPUT, password)
        self.click_element_js(LoginLocators.LOGIN_BTN)
        