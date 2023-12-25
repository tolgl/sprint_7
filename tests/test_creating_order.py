import pytest
import allure
from conftest import fixture_creating_order


class TestCreatingOrder:

    @allure.title('Проверка ответа оформления заказа с указанием и без указания цвета')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ""])
    def test_status_code_creating_order(self, color, fixture_creating_order):

        assert fixture_creating_order(color).status_code == 201
        assert fixture_creating_order(color).json()['track'] != ''
