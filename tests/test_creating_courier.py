import json
import requests
from config import BASE_URL, DEFAULT_HEADERS
import pytest_check as check


class TestCreatingCourier:
    path = 'api/v1/courier'

    def test_successful_creating_courier(self, generation_login_pass_name_courier, del_data_courier):
        payload = {
            "login": generation_login_pass_name_courier[0],
            "password": generation_login_pass_name_courier[1],
            "name": generation_login_pass_name_courier[2]
        }
        # добавление курьера
        response = requests.post(url=BASE_URL + self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        check.equal(response.status_code, 201)
        check.equal(response.json()['ok'], True)

        # фикстура удаления курьера с тестовыми данными
        del_data_courier(BASE_URL, payload['login'], payload['password'])

    def test_creating_courier_without_login(self, generation_login_pass_name_courier, del_data_courier):
        payload = {
            "password": generation_login_pass_name_courier[1],
            "name": generation_login_pass_name_courier[2]
        }
        # добавление курьера
        response = requests.post(url=BASE_URL + self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        check.equal(response.status_code, 400)
        check.equal(response.json()['message'], 'Недостаточно данных для создания учетной записи')

    def test_creating_courier_without_password(self, generation_login_pass_name_courier, del_data_courier):
        payload = {
            "login": generation_login_pass_name_courier[0],
            "name": generation_login_pass_name_courier[2]
        }
        # добавление курьера
        response = requests.post(url=BASE_URL + self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        check.equal(response.status_code, 400)
        check.equal(response.json()['message'], 'Недостаточно данных для создания учетной записи')

    def test_creating_courier_with_same_login(self, register_new_courier_and_return_login_password, del_data_courier):
        # логин и пароль уже зарегистрированного пользователя
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1],
            "firstName": register_new_courier_and_return_login_password[2]
        }
        # добавление курьера с этими же данными
        response_post = requests.post(url=BASE_URL + self.path,
                                      data=json.dumps(payload),
                                      headers=DEFAULT_HEADERS)

        check.equal(response_post.json()['message'], 'Этот логин уже используется. Попробуйте другой.')
        check.equal(response_post.status_code, 409)

        # фикстура удаления курьера с тестовыми данными
        del_data_courier(BASE_URL, payload['login'], payload['password'])





        
