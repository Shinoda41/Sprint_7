from faker import Faker

from data import TestAuthorizationData


class TestDataHelper:
    @staticmethod
    def modify_creating_courier_body_request(key, value):
        body = TestAuthorizationData.CREATING_COURIER_BODY.copy()
        body[key] = value

        return body

    @staticmethod
    def generate_creating_courier_body():
        fake = Faker()

        return TestDataHelper.modify_creating_courier_body_request('login', fake.name_nonbinary())