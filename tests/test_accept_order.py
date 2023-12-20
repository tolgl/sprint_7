import json
import requests
from config import BASE_URL, DEFAULT_HEADERS
import pytest_check as check


class TestGetOrder:
    path_accept_order = 'api/v1/orders/accept'
    path_by_track = 'api/v1/orders/track'
    path_post_id_courier_login = 'api/v1/courier/login'

    def test_successful_accept_order(self, fixture_creating_order, register_new_courier_and_return_login_password, fixture_del_courier):
        # получаем трек номер заказа
        track_order = fixture_creating_order(color='BLACK').json()['track']
        get_params_track_order = {"t": track_order}
        # получаем id заказа по трек номеру
        response_get_order_by_track = requests.get(url=BASE_URL+self.path_by_track, params=get_params_track_order)
        id_order = response_get_order_by_track.json()['order']['id']

        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }
        # получаем id курьера
        response_post_id_courier = requests.post(url=BASE_URL + self.path_post_id_courier_login,
                                                 data=json.dumps(payload),
                                                 headers=DEFAULT_HEADERS)
        id_courier = response_post_id_courier.json()['id']
        get_params_id_courier = {"courierId": id_courier}
        # принимаем заказ со всеми полученными параметрами
        response_put = requests.put(url=f'{BASE_URL}{self.path_accept_order}/{id_order}', params=get_params_id_courier)

        check.equal(response_put.status_code, 200)
        check.equal(response_put.json()['ok'], True)
        # фикстура удаления курьера
        fixture_del_courier(BASE_URL, payload['login'], payload['password'])

    def test_accept_order_without_id_courier(self, fixture_creating_order):
        # получаем трек номер заказа
        track_order = fixture_creating_order(color='BLACK').json()['track']
        get_params_track_order = {"t": track_order}
        # получаем id заказа по трек номеру
        response_get_order_by_track = requests.get(url=BASE_URL + self.path_by_track, params=get_params_track_order)
        id_order = response_get_order_by_track.json()['order']['id']
        response_put = requests.put(url=f'{BASE_URL}{self.path_accept_order}/{id_order}')

        check.equal(response_put.status_code, 400)
        check.equal(response_put.json()['message'], 'Недостаточно данных для поиска')

    def test_accept_order_without_id_order(self, register_new_courier_and_return_login_password):

        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }
        # получаем id курьера
        response_post_id_courier = requests.post(url=BASE_URL + self.path_post_id_courier_login,
                                                 data=json.dumps(payload),
                                                 headers=DEFAULT_HEADERS)
        id_courier = response_post_id_courier.json()['id']
        get_params_id_courier = {"courierId": id_courier}
        # принимаем заказ со всеми полученными параметрами
        response_put = requests.put(url=f'{BASE_URL}{self.path_accept_order}', params=get_params_id_courier)
        print(response_put.url)
        check.equal(response_put.status_code, 400)
        check.equal(response_put.json()['message'], 'Недостаточно данных для поиска')

    def test_accept_order_non_existent_id_courier(self, fixture_creating_order):
        # получаем трек номер заказа
        track_order = fixture_creating_order(color='BLACK').json()['track']
        get_params_track_order = {"t": track_order}
        # получаем id заказа по трек номеру
        response_get_order_by_track = requests.get(url=BASE_URL + self.path_by_track, params=get_params_track_order)
        id_order = response_get_order_by_track.json()['order']['id']
        get_params_id_courier = {"courierId": 000000}
        response_put = requests.put(url=f'{BASE_URL}{self.path_accept_order}/{id_order}',
                                    params=get_params_id_courier)

        check.equal(response_put.status_code, 404)
        check.equal(response_put.json()['message'], 'Курьера с таким id не существует')

    def test_accept_order_non_existent_id_order(self, register_new_courier_and_return_login_password):

        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }
        # получаем id курьера
        response_post_id_courier = requests.post(url=BASE_URL + self.path_post_id_courier_login,
                                                 data=json.dumps(payload),
                                                 headers=DEFAULT_HEADERS)
        id_courier = response_post_id_courier.json()['id']
        get_params_id_courier = {"courierId": id_courier}
        # принимаем заказ со всеми полученными параметрами
        response_put = requests.put(url=f'{BASE_URL}{self.path_accept_order}/000000', params=get_params_id_courier)

        check.equal(response_put.status_code, 404)
        check.equal(response_put.json()['message'], 'Заказа с таким id не существует')
