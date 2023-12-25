from clients.api_client import ApiClient
from path.path_api import ApiPath
import allure
from conftest import fixture_creating_order


class TestGetOrder:

    @allure.title('Проверка получения полного списка заказа')
    def test_get_full_list_order(self):
        api = ApiClient()
        response = api.get(path=ApiPath.path_all_orders)

        assert len(response.json()['orders']) != 0

    @allure.title('Проверка получения заказа по номеру')
    def test_get_order_by_track(self, fixture_creating_order):
        get_params = {"t": fixture_creating_order(color='BLACK').json()['track']}
        api = ApiClient()
        response = api.get(path=ApiPath.path_order_by_track, get_params=get_params)

        assert response.json()['order']['track'] == get_params['t']

    @allure.title('Проверка получения заказа без указания номеру')
    def test_get_order_without_track(self):
        api = ApiClient()
        response = api.get(path=ApiPath.path_order_by_track)

        assert response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка получения заказа по несуществующему номеру')
    def test_get_order_non_existent_track(self):
        get_params = {"t": 000000}
        api = ApiClient()
        response = api.get(path=ApiPath.path_order_by_track, get_params=get_params)

        assert response.json()['message'] == 'Заказ не найден'
