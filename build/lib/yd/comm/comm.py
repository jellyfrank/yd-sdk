
#!/usr/bin/python3
# @Time    : 2025-02-15
# @Author  : Kevin Kong (kfx2007@163.com)

import json
import hashlib
import requests
from datetime import datetime

URL = "https://openapi.yundaex.com"
SANDBOXURL = "https://u-openapi.yundasys.com"


class Comm(object):
    """Public request encapsulation"""
    
    def __get__(self, instance, owner):
        self.appkey = instance.appkey
        self.appsecret = instance.appsecret
        self.partner_id = instance.partner_id
        self.secret = instance.secret
        self.sandbox = instance.sandbox
        return self
    
    def get_sign(self, request_body):
        """
        Generate signature for the request.
        Signature = MD5(jsonReqBody + "_" + app_secret)
        """
        json_req_body = json.dumps(request_body)
        sign_str = f"{json_req_body}_{self.appsecret}"
        return hashlib.md5(sign_str.encode('utf-8')).hexdigest().lower()

    def get_headers(self, request_body):
        """
        Get HTTP headers with authentication parameters.
        The header includes:
        1. "app-key": the application key.
        2. "sign": 32-character lowercase MD5 signature of the request body and secret.
        """
        return {
            "Content-Type": "application/json",
            "app-key": self.appkey,
            "sign": self.get_sign(request_body),
            # "req-time": str(int(datetime.now().timestamp()))
        }

    def post(self, endpoint, request_body):
        """
        Request the specified endpoint with the given request body.
        """
        url = (SANDBOXURL if self.sandbox else URL).rstrip('/') + '/' + endpoint.lstrip('/')
        headers = self.get_headers(request_body)
        print(f"Request URL: {url}")
        print(f"Request Headers: {headers}")
        print(f"Request Body: {request_body}")
        res = requests.post(url, json=request_body, headers=headers).json()
        return res