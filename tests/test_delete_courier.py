import allure
from test_data import generation_login_pass_name_courier
from clients.api_client import ApiClient
from path.path_api import ApiPath


class TestDeleteCourier:

    @allure.title('Проверка успешного удаления курьера')
    def test_successful_delete_courier(self):
        payload = {
            "login": generation_login_pass_name_courier()[0],
            "password": generation_login_pass_name_courier()[1]
        }
        api = ApiClient()
        # создаем курьера
        api.post(path=ApiPath.path_creating_courier,
                 payload=payload)
        # получаем id курьера
        id_courier = api.post(path=ApiPath.path_id_courier_login, payload=payload).json()["id"]
        # удаляем курьера
        response_del = api.delete(path=f'{ApiPath.path_creating_courier}/{id_courier}')

        assert response_del.status_code == 200
        assert response_del.json()['ok'] is True

    @allure.title('Проверка удаления курьера без указания id')
    def test_delete_courier_without_id(self):
        payload = {
            "login": generation_login_pass_name_courier()[0],
            "password": generation_login_pass_name_courier()[1]
        }
        api = ApiClient()
        # создаем курьера
        api.post(path=ApiPath.path_creating_courier,
                 payload=payload)
        # удаляем курьера
        response_del = api.delete(path=ApiPath.path_creating_courier)

        assert response_del.json()['message'] == 'Недостаточно данных для удаления курьера'

    @allure.title('Проверка удаления курьера с несуществующим id')
    def test_delete_courier_non_existent_id(self):
        payload = {
            "login": generation_login_pass_name_courier()[0],
            "password": generation_login_pass_name_courier()[1]
        }
        api = ApiClient()
        # создаем курьера
        api.post(path=ApiPath.path_creating_courier,
                 payload=payload)
        # удаляем курьера
        response_del = api.delete(path=f'{ApiPath.path_creating_courier}/000000')

        assert response_del.json()['message'] == 'Курьера с таким id нет.'
