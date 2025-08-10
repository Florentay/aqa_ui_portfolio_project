# import requests
from api_python.api_methods.base_case import BaseCase
from api_python.api_methods.assertions import Assertions
from api_python.api_methods.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        # response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_have_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        # response2 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        response2 = MyRequests.post('/user/login', data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = 'Changed name'
        # response3 = requests.put(
        #     f'https://playground.learnqa.ru/api/user/{user_id}',
        #     headers={'x-csrf-token': token},
        #     cookies={'auth_sid': auth_sid},
        #     data={'firstName': new_name}
        # )

        response3 = MyRequests.put(
            f'/user/{user_id}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={'firstName': new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        # response4 = requests.get(
        #     f'https://playground.learnqa.ru/api/user/{user_id}',
        #     headers={'x-csrf-token': token},
        #     cookies={'auth_sid': auth_sid}
        # )

        response4 = MyRequests.get(
            f'/user/{user_id}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        # print(response4.json())

        Assertions.assert_json_value_by_name(
            response4,
            'firstName',
            new_name,
            'wrong name of the user after edit'
        )
