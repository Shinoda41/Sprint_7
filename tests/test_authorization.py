import allure

from data import TestAuthorizationData, ResponseText
from scooter_api import ScooterApi


class TestAuthorization:
    @allure.title('Проверка успешной авторизации')
    def test_success_login(self):
        login_request = ScooterApi.login(TestAuthorizationData.LOGIN_COURIER_BODY)
        assert (login_request.status_code == 200 and
                login_request.json()['id'] == TestAuthorizationData.COURIER_ID)

    @allure.title('Проверка авторизации с неверными данными')
    def test_wrong_data_login(self):
        login_request = ScooterApi.login(TestAuthorizationData.WRONG_PASSWORD_COURIER_BODY)
        assert (login_request.status_code == 404 and
                login_request.json()['message'] == ResponseText.USER_ACCOUNT_NOT_FOUND)

    @allure.title('Проверка авторизации без  наличия всех обязательных полей ')
    def test_missing_field_login(self):
        login_request = ScooterApi.login(TestAuthorizationData.COURIER_NOT_FULL_DATA)
        assert (login_request.status_code == 400 and
                login_request.json()['message'] == ResponseText.MISSING_REQUIRED_FIELD_LOGIN)

