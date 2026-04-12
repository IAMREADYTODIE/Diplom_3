import random
import string
import allure

class UserGenerator:
    @staticmethod
    @allure.step("Генерация случайных данных для нового пользователя")
    def generate_random_user():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        email = f"{generate_random_string(8)}@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(8)

        return {
            "email": email,
            "password": password,
            "name": name
        }
    