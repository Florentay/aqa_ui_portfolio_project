from datetime import datetime

import allure
from api_python.api_methods.base_case import BaseCase
from api_python.api_methods.assertions import Assertions
from api_python.api_methods.my_requests import MyRequests


class TestUserRegister(BaseCase):
    # def setup(self):
    #     base_part = 'learnqa'
    #     domain = 'example.com'
    #     random_part = datetime.now().strftime("%d%m%Y%H%M%S")
    #     self.email = f'{base_part}{random_part}@{domain}'

    @allure.title("Успешная регистрация")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': self.email
        # }

        # response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        response = MyRequests.post('/user/', data=data)
        # print(response.status_code)
        # print(response.text)

        # assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_have_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': email
        # }

        # response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        response = MyRequests.post('/user/', data=data)

        # print(response.status_code)
        # print(response.content)
        # print(response.text)

        # assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 400)

        # assert response.content == f"Users with email {email} already exists", f"Unexpected response content {response.content}"
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

# python3 -m pytest -s(для того чтобы вывести значение принт) api_python/tests/test_user_register.py -k(отдельный тест для запуска)  test_create_user_successfully
