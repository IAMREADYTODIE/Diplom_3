from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    LOGIN_BTN = (By.XPATH, ".//button[text()='Войти']")
    