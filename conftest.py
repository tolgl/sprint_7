import pytest
from test_data import generation_login_pass_name_courier, data_for_creating_order
from clients.api_client import ApiClient
from path.path_api import ApiPath


# метод регистрации и удаления нового курьера возвращает список из логина и пароля
@pytest.fixture()
def register_new_courier_and_return_login_password():

    login_pass = []
    # генерируем логин, пароль и имя курьера
    login = generation_login_pass_name_courier()[0]
    password = generation_login_pass_name_courier()[1]
    first_name = generation_login_pass_name_courier()[2]

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера
    api = ApiClient()
    response = api.post(path=ApiPath.path_creating_courier,
                        payload=payload)

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    yield [login_pass, response]

    del payload["firstName"]
    api.delete(path=f'{ApiPath.path_creating_courier}/'
                    f'{api.post(path=ApiPath.path_id_courier_login, payload=payload).json()["id"]}')
