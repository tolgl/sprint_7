import json
import requests
from config import BASE_URL, DEFAULT_HEADERS


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = DEFAULT_HEADERS

    def post(self, path, payload):
        response_post = requests.post(url=self.base_url + path,
                                      headers=self.headers,
                                      data=json.dumps(payload))
        return response_post

    def get(self, path, get_params=None):
        response_get = requests.get(url=self.base_url + path,
                                    params=get_params)

        return response_get

    def put(self, path, get_params=None):
        response_put = requests.put(url=self.base_url + path,
                                    params=get_params)

        return response_put

    def delete(self, path):
        response_del = requests.delete(url=self.base_url + path)

        return response_del
