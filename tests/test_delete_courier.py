import json
import requests
from config import BASE_URL, DEFAULT_HEADERS


class TestDeleteCourier:
    path_delete = 'api/v1/courier'

    def test_successful_delete_courier(self, register_new_courier_and_return_login_password, fixture_del_courier):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }
        assert fixture_del_courier(url=BASE_URL, login=payload['login'], password=payload['password']).json()['ok'] is True

    def test_delete_courier_without_id(self):
        response_del = requests.delete(url=BASE_URL + self.path_delete)

        assert response_del.json()['message'] == 'Недостаточно данных для удаления курьера'

    def test_delete_courier_non_existent_id(self):
        response_del = requests.delete(url=f'{BASE_URL}{self.path_delete}/000000')

        assert response_del.json()['message'] == 'Курьера с таким id нет.'
