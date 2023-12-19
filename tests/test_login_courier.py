import json

import requests
from config import BASE_URL, DEFAULT_HEADERS
import pytest_check as check


class TestLoginCourier:
    path = 'api/v1/courier/login'

    def test_successful_login_courier(self, register_new_courier_and_return_login_password, del_data_courier):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }

        response = requests.post(url=BASE_URL+self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        assert response.status_code == 200

        # фикстура удаления курьера с тестовыми данными
        del_data_courier(BASE_URL, payload['login'], payload['password'])

    def test_login_courier_without_password(self, register_new_courier_and_return_login_password, del_data_courier):
        payload = {
            "login": register_new_courier_and_return_login_password[0]
        }

        response = requests.post(url=BASE_URL + self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        check.equal(response.json()['message'], 'Недостаточно данных для входа')
        check.equal(response.status_code, 400)

    def test_login_courier_without_login(self, register_new_courier_and_return_login_password, del_data_courier):
        payload = {
            "password": register_new_courier_and_return_login_password[1]
        }

        response = requests.post(url=BASE_URL + self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        check.equal(response.json()['message'], 'Недостаточно данных для входа')
        check.equal(response.status_code, 400)

    def test_login_courier_non_existent_login(self, register_new_courier_and_return_login_password, del_data_courier):
        payload = {
            "login": f'{register_new_courier_and_return_login_password[0]}_123',
            "password": register_new_courier_and_return_login_password[1]
        }

        response = requests.post(url=BASE_URL + self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        check.equal(response.json()['message'], 'Учетная запись не найдена')
        check.equal(response.status_code, 404)

    def test_login_courier_non_existent_password(self, register_new_courier_and_return_login_password, del_data_courier):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": f'{register_new_courier_and_return_login_password[1]}_123'
        }

        response = requests.post(url=BASE_URL + self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)
        print(payload)
        check.equal(response.json()['message'], 'Учетная запись не найдена')
        check.equal(response.status_code, 404)
