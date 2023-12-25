from clients.api_client import ApiClient
from path.path_api import ApiPath
import allure
from conftest import register_new_courier_and_return_login_password


class TestLoginCourier:

    @allure.title('Проверка успешного логина курьера в системе')
    def test_successful_login_courier(self, register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0][0],
            "password": register_new_courier_and_return_login_password[0][1]
        }

        api = ApiClient()
        response = api.post(path=ApiPath.path_id_courier_login,
                            payload=payload)

        assert response.status_code == 200

    @allure.title('Проверка логина курьера без пароля')
    def test_login_courier_without_password(self, register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0][0]
        }

        api = ApiClient()
        response = api.post(path=ApiPath.path_id_courier_login,
                            payload=payload)

        assert response.json()['message'] == 'Недостаточно данных для входа'
        assert response.status_code == 400

    @allure.title('Проверка логина курьера без логина')
    def test_login_courier_without_login(self, register_new_courier_and_return_login_password):
        payload = {
            "password": register_new_courier_and_return_login_password[0][1]
        }

        api = ApiClient()
        response = api.post(path=ApiPath.path_id_courier_login,
                            payload=payload)

        assert response.json()['message'] == 'Недостаточно данных для входа'
        assert response.status_code == 400

    @allure.title('Проверка логина курьера с несуществующим логином')
    def test_login_courier_non_existent_login(self, register_new_courier_and_return_login_password):
        payload = {
            "login": f'{register_new_courier_and_return_login_password[0][0]}_123',
            "password": register_new_courier_and_return_login_password[0][1]
        }

        api = ApiClient()
        response = api.post(path=ApiPath.path_id_courier_login,
                            payload=payload)

        assert response.json()['message'] == 'Учетная запись не найдена'
        assert response.status_code == 404

    @allure.title('Проверка логина курьера с несуществующим паролем')
    def test_login_courier_non_existent_password(self, register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0][0],
            "password": f'{register_new_courier_and_return_login_password[0][1]}_123'
        }

        api = ApiClient()
        response = api.post(path=ApiPath.path_id_courier_login,
                            payload=payload)

        assert response.json()['message'] == 'Учетная запись не найдена'
        assert response.status_code == 404
