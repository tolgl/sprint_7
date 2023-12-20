import json
import requests
import datetime
from config import BASE_URL, DEFAULT_HEADERS


class TestGetOrder:
    path_all_orders = 'api/v1/orders'
    path_by_track = 'api/v1/orders/track'

    def test_get_list_order_without_courier(self):
        response = requests.get(url=BASE_URL+self.path_all_orders)

        assert len(response.json()['orders']) != 0

    def test_get_order_by_track(self, fixture_creating_order):
        get_params = {"t": fixture_creating_order(color='BLACK').json()['track']}
        response_get_order_by_track = requests.get(url=BASE_URL+self.path_by_track, params=get_params)

        assert response_get_order_by_track.json()['order']['track'] == get_params['t']

    def test_get_order_without_track(self):
        response = requests.get(url=BASE_URL + self.path_by_track)

        assert response.json()['message'] == 'Недостаточно данных для поиска'

    def test_get_order_non_existent_track(self):
        get_params = {"t": 000000}
        response = requests.get(url=BASE_URL + self.path_by_track, params=get_params)

        assert response.json()['message'] == 'Заказ не найден'
