#!/usr/bin/python3
# @Time    : 2025-02-15
# @Author  : Kevin Kong (kfx2007@163.com)

from yd.comm import Comm


class Label(Comm):
    """Label related API"""

    def print(self, orders: list):
        """
        Print the order parameters.

        参数:
            partner_id(String, 长度:30, 必填) - 韵达白马账号（合作网点提供，转发白马接口需使用）
            secret    (String, 长度:30, 必填) - 韵达白马账号的联调密码（合作网点提供，转发白马接口需使用）
            orders    (List,  必填)         - 订单详情(一批次只能传一个运单号)
        Returns:
            dict: API response.
            {'code': '0000', 'data': [{'mailno': '312008348025313', 'pdfInfo': 'xxxxx'}], 'message': '请求成功', 'result': True, 'sub_code': None, 'sub_msg': None}
        """
        payload = {
            "appid": self.appkey,
            "partner_id": self.partner_id,
            "secret": self.secret,
            "orders": [{"mailno": order} for order in orders],
        }
        endpoint = "/openapi/outer/v1/bm/getPdfInfo"
        return self.post(endpoint, payload)
