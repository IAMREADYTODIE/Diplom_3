import pytest
import allure
import requests
from selenium import webdriver
from data import Urls
from helpers import UserGenerator

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    _driver = None
    
    try:
        if browser_name == "chrome":
            with allure.step("Запуск браузера Chrome"):
                _driver = webdriver.Chrome()
        elif browser_name == "firefox":
            with allure.step("Запуск браузера Firefox"):
                _driver = webdriver.Firefox()
                
        _driver.maximize_window()
        yield _driver
    finally:
        if _driver:
            with allure.step("Закрытие браузера"):
                _driver.quit()

@pytest.fixture
def create_user_api():
    payload = UserGenerator.generate_random_user()
    response = requests.post(Urls.API_REGISTER, json=payload)
    data = response.json()
    token = data.get("accessToken")
    
    user_data = {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "token": token
    }
    
    yield user_data
    
    if token:
        requests.delete(Urls.API_USER, headers={"Authorization": token})
        