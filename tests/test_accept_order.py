import allure
from clients.api_client import ApiClient
from path.path_api import ApiPath
from conftest import register_new_courier_and_return_login_password
from test_data import data_for_creating_order


class TestGetOrder:

    @allure.title('Проверка успешного оформления заказа')
    def test_successful_accept_order(self, register_new_courier_and_return_login_password):
        api = ApiClient()
        # получаем трек номер заказа
        track_order = api.post(path=ApiPath.path_all_orders,
                               payload=data_for_creating_order(color='BLACK')).json()['track']
        get_params_track_order = {"t": track_order}
        # получаем id заказа по трек номеру
        response_get = api.get(path=ApiPath.path_order_by_track, get_params=get_params_track_order)
        id_order = response_get.json()['order']['id']

        payload = {
            "login": register_new_courier_and_return_login_password[0][0],
            "password": register_new_courier_and_return_login_password[0][1]
        }

        # получаем id курьера
        response_post = api.post(path=ApiPath.path_id_courier_login, payload=payload)
        id_courier = response_post.json()['id']

        get_params_id_courier = {"courierId": id_courier}
        # принимаем заказ со всеми полученными параметрами
        response_put = api.put(path=f'{ApiPath.path_accept_order}/{id_order}', get_params=get_params_id_courier)

        assert response_put.status_code == 200
        assert response_put.json()['ok'] is True

    @allure.title('Проверка оформления заказа без id курьера')
    def test_accept_order_without_id_courier(self):
        api = ApiClient()
        # получаем трек номер заказа
        track_order = api.post(path=ApiPath.path_all_orders,
                               payload=data_for_creating_order(color='BLACK')).json()['track']
        get_params_track_order = {"t": track_order}
        # получаем id заказа по трек номеру
        response_get = api.get(path=ApiPath.path_order_by_track, get_params=get_params_track_order)
        id_order = response_get.json()['order']['id']
        response_put = api.put(path=f'{ApiPath.path_accept_order}/{id_order}')

        assert response_put.status_code == 400
        assert response_put.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка оформления заказа без id заказа')
    def test_accept_order_without_id_order(self, register_new_courier_and_return_login_password):

        payload = {
            "login": register_new_courier_and_return_login_password[0][0],
            "password": register_new_courier_and_return_login_password[0][1]
        }
        # получаем id курьера
        api = ApiClient()
        response_post = api.post(path=ApiPath.path_id_courier_login, payload=payload)
        id_courier = response_post.json()['id']
        get_params_id_courier = {"courierId": id_courier}
        # принимаем заказ со всеми полученными параметрами
        response_put = api.put(path=ApiPath.path_accept_order, get_params=get_params_id_courier)

        assert response_put.status_code == 400
        assert response_put.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка оформления заказа с несуществующим id курьера')
    def test_accept_order_non_existent_id_courier(self):
        api = ApiClient()
        track_order = api.post(path=ApiPath.path_all_orders,
                               payload=data_for_creating_order(color='BLACK')).json()['track']
        get_params_track_order = {"t": track_order}
        # получаем id заказа по трек номеру
        response_get = api.get(path=ApiPath.path_order_by_track, get_params=get_params_track_order)
        id_order = response_get.json()['order']['id']
        # принимаем заказ с несуществующим id курьера
        get_params_id_courier = {"courierId": 000000}
        response_put = api.put(path=f'{ApiPath.path_accept_order}/{id_order}', get_params=get_params_id_courier)

        assert response_put.status_code == 404
        assert response_put.json()['message'] == 'Курьера с таким id не существует'

    @allure.title('Проверка оформления заказа с несуществующим id заказа')
    def test_accept_order_non_existent_id_order(self, register_new_courier_and_return_login_password):

        payload = {
            "login": register_new_courier_and_return_login_password[0][0],
            "password": register_new_courier_and_return_login_password[0][1]
        }
        # получаем id курьера
        api = ApiClient()
        response_post = api.post(path=ApiPath.path_id_courier_login, payload=payload)
        id_courier = response_post.json()['id']
        get_params_id_courier = {"courierId": id_courier}
        # принимаем заказ со всеми полученными параметрами
        response_put = api.put(path=f'{ApiPath.path_accept_order}/000000', get_params=get_params_id_courier)

        assert response_put.status_code == 404
        assert response_put.json()['message'] == 'Заказа с таким id не существует'
