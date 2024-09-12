import allure
import pytest

from data import TestAuthorizationData
from scooter_api import ScooterApi


class TestCreatingOrder:

    @allure.title('Проверка оформления заказа с различным вариантом цвета')
    @pytest.mark.parametrize('colour', ['""', '"BLACK", "GREY"', 'BLACK', 'GREY'])
    def test_creating_order(self, colour):
        order_body = TestAuthorizationData.create_order_body(colour)
        order_request = ScooterApi.create_order(order_body)
        assert order_request.status_code == 201 and "track" in order_request.json()



