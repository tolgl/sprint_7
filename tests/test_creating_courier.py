import allure
from test_data import generation_login_pass_name_courier
from clients.api_client import ApiClient
from path.path_api import ApiPath
from conftest import register_new_courier_and_return_login_password


class TestCreatingCourier:

    @allure.title('Проверка успешного создания курьера')
    def test_successful_creating_courier(self, register_new_courier_and_return_login_password):

        assert register_new_courier_and_return_login_password[1].status_code == 201
        assert register_new_courier_and_return_login_password[1].json()['ok'] is True

    @allure.title('Проверка создания курьера без указания логина')
    def test_creating_courier_without_login(self):
        payload = {
            "password": generation_login_pass_name_courier()[1],
            "name": generation_login_pass_name_courier()[2]
        }
        # добавление курьера
        api = ApiClient()
        response = api.post(path=ApiPath.path_creating_courier,
                            payload=payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверка создания курьера без указания пароля')
    def test_creating_courier_without_password(self):
        payload = {
            "login": generation_login_pass_name_courier()[0],
            "name": generation_login_pass_name_courier()[2]
        }
        # добавление курьера
        api = ApiClient()
        response = api.post(path=ApiPath.path_creating_courier,
                            payload=payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверка создания уже зарегистрированного курьера')
    def test_creating_courier_with_same_login(self, register_new_courier_and_return_login_password):
        # логин и пароль уже зарегистрированного пользователя
        payload = {
            "login": register_new_courier_and_return_login_password[0][0],
            "password": register_new_courier_and_return_login_password[0][1],
            "firstName": register_new_courier_and_return_login_password[0][2]
        }
        # добавление курьера с этими же данными
        api = ApiClient()
        response = api.post(path=ApiPath.path_creating_courier,
                            payload=payload)

        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
        assert response.status_code == 409
