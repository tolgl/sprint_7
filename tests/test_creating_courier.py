from test_data import generation_login_pass_name_courier
from clients.api_client import ApiClient
from path.path_api import ApiPath


class TestCreatingCourier:

    def test_successful_creating_courier(self, fixture_del_courier):
        payload = {
            "login": generation_login_pass_name_courier()[0],
            "password": generation_login_pass_name_courier()[1],
            "name": generation_login_pass_name_courier()[2]
        }
        # добавление курьера
        api = ApiClient()
        response = api.post(path=ApiPath.path_creating_courier,
                            payload=payload)

        assert response.status_code == 201
        assert response.json()['ok'] is True

        # фикстура удаления курьера с тестовыми данными
        # fixture_del_courier(BASE_URL, payload['login'], payload['password'])

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

    def test_creating_courier_with_same_login(self, register_new_courier_and_return_login_password, fixture_del_courier):
        # логин и пароль уже зарегистрированного пользователя
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1],
            "firstName": register_new_courier_and_return_login_password[2]
        }
        # добавление курьера с этими же данными
        api = ApiClient()
        response = api.post(path=ApiPath.path_creating_courier,
                            payload=payload)

        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
        assert response.status_code == 409

        # фикстура удаления курьера с тестовыми данными
        # fixture_del_courier(BASE_URL, payload['login'], payload['password'])





        
