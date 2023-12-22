import pytest


class TestCreatingOrder:

    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ""])
    def test_status_code_creating_order(self, color, fixture_creating_order):

        assert fixture_creating_order(color).status_code == 201

    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ""])
    def test_response_creating_order(self, color, fixture_creating_order):

        assert fixture_creating_order(color).json()['track'] != ''
