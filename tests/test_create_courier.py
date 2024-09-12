import allure

from data import TestAuthorizationData, ResponseText
from helper import TestDataHelper
from scooter_api import ScooterApi


class TestCreateCourier:

    @allure.title('Проверка успешной регистрации')
    def test_successful_creating_courier(self):
        creating_courier_request = (ScooterApi.creating_courier
                                    (TestDataHelper.generate_creating_courier_body()))
        assert creating_courier_request.status_code == 201 and creating_courier_request.text == ResponseText.CREATING_SUCCESS

    @allure.title('Проверка регистрации уже существующего пользователя')
    def test_creating_courier_same_data(self):
        creating_courier_request = (ScooterApi.creating_courier
                                    (TestAuthorizationData.CREATING_COURIER_BODY))
        assert (creating_courier_request.status_code == 409 and
                creating_courier_request.json()['message'] == ResponseText.USED_LOGIN)

    @allure.title('Проверка регистрации без наличия всех обязательных полей')
    def test_creating_courier_without_password_(self):
        creating_courier_request = (ScooterApi.creating_courier
                                    (TestAuthorizationData.COURIER_NOT_FULL_DATA))
        assert (creating_courier_request.status_code == 400 and
                creating_courier_request.json()['message'] == ResponseText.MISSING_REQUIRED_FIELD)
