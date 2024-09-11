import allure

from scooter_api import ScooterApi


class TestOrderList:

    @allure.title('Проверка Отображения списка заказов')
    def test_order_list(self):
        order_list_request = ScooterApi.get_order_list()
        assert order_list_request.status_code == 200 and "orders" in order_list_request.json()
