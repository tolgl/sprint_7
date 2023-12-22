import random
import string
import datetime


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


def data_for_creating_order(color):
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

    return payload


