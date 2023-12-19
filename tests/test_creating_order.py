import json
import pytest
import requests
import datetime
from config import BASE_URL, DEFAULT_HEADERS
import pytest_check as check


class TestCreatingOrder:
    path = 'api/v1/orders'

    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], [""]])
    def test_creating_order(self, color):
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

        response = requests.post(url=BASE_URL+self.path,
                                 data=json.dumps(payload),
                                 headers=DEFAULT_HEADERS)

        check.equal(response.status_code, 201)
        check.is_not(response.json()['track'], '')

    def test_get_list_order_without_courier(self):
        response = requests.get(url=BASE_URL+self.path)

        assert len(response.json()['orders']) != 0

