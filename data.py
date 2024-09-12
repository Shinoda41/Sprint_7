

class TestAuthorizationData:
    CREATING_COURIER_BODY = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }

    COURIER_NOT_FULL_DATA = {
        "login": "ninja",
        "password": ""
    }

    LOGIN_COURIER_BODY = {
        "login": "ninjo",
        "password": "1234"
    }

    WRONG_PASSWORD_COURIER_BODY = {
        "login": "ninjo",
        "password": "1230"
    }

    COURIER_ID = 382461

    @staticmethod
    def create_order_body(colour):
        order_data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                colour
            ]
        }
        return order_data


class ResponseText:
    CREATING_SUCCESS = '{"ok":true}'
    USED_LOGIN = "Этот логин уже используется. Попробуйте другой."
    MISSING_REQUIRED_FIELD = "Недостаточно данных для создания учетной записи"
    USER_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    MISSING_REQUIRED_FIELD_LOGIN = "Недостаточно данных для входа"



