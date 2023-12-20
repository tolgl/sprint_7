import json
import requests
import random
import string
import pytest
import datetime

from config import DEFAULT_HEADERS, BASE_URL


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture()
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{BASE_URL}api/v1/courier',
                             data=json.dumps(payload),
                             headers=DEFAULT_HEADERS)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


@pytest.fixture()
def generation_login_pass_name_courier():
    login_pass = []

    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    return login_pass


@pytest.fixture()
def fixture_del_courier():
    def del_courier(url, login, password):
        payload = {
            "login": login,
            "password": password,
        }
        # получение id курьера
        response_post_id = requests.post(url=f'{url}api/v1/courier/login',
                                         data=json.dumps(payload),
                                         headers=DEFAULT_HEADERS)
        id_courier = response_post_id.json()['id']
        # удаление курьера по полученному id
        response_del = requests.delete(url=f'{url}api/v1/courier/{id_courier}')
        return response_del

    return del_courier


@pytest.fixture()
def fixture_creating_order():
    def creating_order(color):
        payload = {
            "firstName": "Test",
            "lastName": "Testov",
            "address": "Testovaya, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": datetime.date.today().strftime('%Y-%m-%d'),
            "comment": "Test comment",
            "color": [color]
        }
        response_post_order = requests.post(url=f'{BASE_URL}api/v1/orders',
                                            data=json.dumps(payload),
                                            headers=DEFAULT_HEADERS)
        return response_post_order

    return creating_order
