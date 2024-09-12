
import requests

import urls


class ScooterApi:

    @staticmethod
    def creating_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=body)

    @staticmethod
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    def get_order_list():
        return requests.get(urls.BASE_URL + urls.ORDER_LIST_ENDPOINT)
