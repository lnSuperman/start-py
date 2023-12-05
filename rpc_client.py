import json

import requests


# res = requests.get(url="http://127.0.0.1:8003", params={
#     "a": 1,
#     "b": 1
# })
# print(res.text)


class ClientStub:
    def __init__(self, url):
        self.url = url

    def add(self, a, b):
        res = requests.get(url=self.url, params={
            "a": a,
            "b": b
        })
        return json.loads(res.text).get("result")


if __name__ == '__main__':
    c = ClientStub("http://127.0.0.1:8003")
    print(c.add(1, 1))
