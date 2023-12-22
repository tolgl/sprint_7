from clients.api_client import ApiClient
from path.path_api import ApiPath


class TestGetOrder:

    def test_get_list_order_without_courier(self):
        api = ApiClient()
        response = api.get(path=ApiPath.path_all_orders)

        assert len(response.json()['orders']) != 0

    def test_get_order_by_track(self, fixture_creating_order):
        get_params = {"t": fixture_creating_order(color='BLACK').json()['track']}
        api = ApiClient()
        response = api.get(path=ApiPath.path_order_by_track, get_params=get_params)

        assert response.json()['order']['track'] == get_params['t']

    def test_get_order_without_track(self):
        api = ApiClient()
        response = api.get(path=ApiPath.path_order_by_track)

        assert response.json()['message'] == 'Недостаточно данных для поиска'

    def test_get_order_non_existent_track(self):
        get_params = {"t": 000000}
        api = ApiClient()
        response = api.get(path=ApiPath.path_order_by_track, get_params=get_params)

        assert response.json()['message'] == 'Заказ не найден'
