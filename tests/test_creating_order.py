import pytest
import allure
from test_data import data_for_creating_order
from clients.api_client import ApiClient
from path.path_api import ApiPath


class TestCreatingOrder:

    @allure.title('Проверка ответа оформления заказа с указанием и без указания цвета')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ""])
    def test_status_code_creating_order(self, color):
        api = ApiClient()
        response = api.post(path=ApiPath.path_all_orders,
                            payload=data_for_creating_order(color))

        assert response.status_code == 201
        assert response.json()['track'] != ''
