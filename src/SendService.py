# 发送请求类
import requests


class SendService(object):

    @staticmethod
    def send_http(url, method="get", **kwargs):
        if method == "get":
            return requests.get(url, **kwargs)
        elif method == "post":
            return requests.post(url, **kwargs)
        elif method == "put":
            return requests.post(url, **kwargs)
        elif method == "delete":
            return requests.delete(url, **kwargs)

    def get(self, url, **kwargs):
        return self.send_http(url, **kwargs)

    def post(self, url, **kwargs):
        return self.send_http(url, method="post", **kwargs)

    def put(self, url, **kwargs):
        return self.send_http(url, method="put", **kwargs)

    def delete(self, url, **kwargs):
        return self.send_http(url, method="delete", **kwargs)



