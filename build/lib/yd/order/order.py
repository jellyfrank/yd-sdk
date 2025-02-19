#!/usr/bin/python3
# @Time    : 2025-02-15
# @Author  : Kevin Kong (kfx2007@163.com)

from datetime import datetime
from yd.comm import Comm


class Order(Comm):
    """Order related API"""

    def create(
        self,
        appid: str,
        orderid: str,
        backurl: str,
        sender: dict,
        receiver: dict,
        sendstarttime: str,
        **kwargs,
    ):
        """
        Create an order using the order/pushOrder endpoint.

        Parameters:
            appid (str): 合作商app-key.
            orderid (str): 合作商订单号.
            backurl (str): 运单回传地址url.
            sender (dict): 寄件人信息, e.g., {
                "name": str,
                "company": str,
                "province": str,
                "city": str,
                "county": str,
                "address": str,
                "postcode": str,
                "phone": str,
                "mobile": str
            }
            receiver (dict): 收件人信息, e.g., {
                "name": str,
                "company": str,
                "province": str,
                "city": str,
                "county": str,
                "address": str,
                "postcode": str,
                "phone": str,
                "mobile": str
            }
            sendstarttime (str): 取件开始时间 (格式: yyyy-MM-dd HH:mm:ss).
            **kwargs: Optional parameters including:
                sendendtime, weight, size, value, freight, premium, other_charges, items, backparam, special, remark.

        Returns:
            dict: API response.
        """
        payload = {
            "appid": self.appkey,
            "orderid": orderid,
            "backurl": backurl,
            "sender": sender,
            "receiver": receiver,
            "sendstarttime": sendstarttime,
        }
        payload.update(kwargs)
        endpoint = "/openapi-api/v1/order/pushOrder"
        return self.post(endpoint, payload)

    def create_label_order(
        self,
        order_serial_no: str,
        khddh: str,
        sender: dict,
        receiver: dict,
        order_type: str,
        node_id: str,
        weight: float = None,
        size: str = None,
        value: float = None,
        collection_value: float = None,
        other_charges: float = None,
        items: list = None,
        remark: str = None,
        special: str = None,
        cus_area1: str = None,
        cus_area2: str = None,
        wave_no: str = None,
        isProtectPrivacy: str = None,
        platform_source: str = None,
        mulpck: str = None,
        total: int = None,
        endmark: int = None,
        markingInfos=None,
    ) -> dict:
        """
        Create an electronic label order.

        Parameters:
            order_serial_no (str): 订单唯一序列号, 由字母、数字、下划线组成，必须保证唯一且过滤特殊符号.
            khddh (str): 大客户系统订单的订单号.
            sender (dict): 寄件人信息, e.g.,
                {
                    "name": str,         # 姓名, 必填, 长度16
                    "company": str,      # 公司, 长度32，可选
                    "province": str,     # 省份, 长度16，可选
                    "city": str,         # 市, 长度16，可选
                    "county": str,       # 区/县, 长度16，可选
                    "address": str,      # 详细地址，必须添加省市区并以半角逗号隔开, 长度125，必填
                    "phone": str,        # 固定电话, 长度16，可选
                    "mobile": str        # 手机号, 长度16，可选
                }
            receiver (dict): 收件人信息, e.g.,
                {
                    "name": str,         # 姓名, 必填, 长度16
                    "company": str,      # 公司, 长度32，可选
                    "province": str,     # 省份, 长度16，可选
                    "city": str,         # 市, 长度16，可选
                    "county": str,       # 区/县, 长度16，可选
                    "address": str,      # 详细地址，必须添加省市区并以半角逗号隔开, 长度64, 必填
                    "phone": str,        # 固定电话, 长度16，可选
                    "mobile": str        # 手机号, 长度16，可选
                }
            order_type (str): 运单类型, 固定为 "common" （对照order_type字典表）.
            node_id (str): 节点ID, 默认350.
            weight (float, optional): 物品重量（kg), 精度10,3.
            size (str, optional): 物品大小(单位米), 长度16.
            value (float, optional): 货物金额, 精度10,2.
            collection_value (float, optional): 代收货款金额, 精度10,2（仅用于cod订单，必填时传入）.
            other_charges (float, optional): 其他费用, 精度10,2.
            items (list, optional): 商品信息集合, 每个元素可以包含:
                {
                    "name": str,    # 商品名称, 长度100, 对于cod订单必填
                    "number": str   # 数量, 长度8
                }
            remark (str, optional): 订单说明, 长度32.
            special (str, optional): 商品类型保留字段，目前不用.
            cus_area1 (str, optional): 自定义显示信息1, 打印在客户自定义区域1, 换行使用\n.
            cus_area2 (str, optional): 自定义显示信息2, 打印在客户自定义区域2, 换行使用\n.
            wave_no (str, optional): 客户波次号，批量下单时此值必须相同.
            isProtectPrivacy (str, optional): 是否隐私订单, "1"表示是, "0"表示否.
            platform_source (str, optional): 平台来源, 长度24.
            multi_pack:一票多件
                mulpck (str, optional): 是否一票多件, 必填时传"1"，否则留空.
                total (int, optional): 总包裹数量, 当为最后一件时传递.
                endmark (int, optional): 结束标记, 最后一件时传 0 或 1.
            markingInfos (list, optional): 增值服务标签信息, JSON数组，若无则传null、空数组或不传.

        Returns:
            dict: API response.
        """
        payload = {
            "order_serial_no": order_serial_no,
            "khddh": khddh,
            "sender": sender,
            "receiver": receiver,
            "order_type": order_type,
            "node_id": node_id,
        }
        if weight is not None:
            payload["weight"] = weight
        if size is not None:
            payload["size"] = size
        if value is not None:
            payload["value"] = value
        if collection_value is not None:
            payload["collection_value"] = collection_value
        if other_charges is not None:
            payload["other_charges"] = other_charges
        if items is not None:
            payload["items"] = items
        if remark is not None:
            payload["remark"] = remark
        if special is not None:
            payload["special"] = special
        if cus_area1 is not None:
            payload["cus_area1"] = cus_area1
        if cus_area2 is not None:
            payload["cus_area2"] = cus_area2
        if wave_no is not None:
            payload["wave_no"] = wave_no
        if isProtectPrivacy is not None:
            payload["isProtectPrivacy"] = isProtectPrivacy
        if platform_source is not None:
            payload["platform_source"] = platform_source
        if mulpck is not None:
            payload["multi_pack"] = {
                "mulpck": mulpck,
                "total": total,
                "endmark": endmark,
            }
        if total is not None:
            payload["total"] = total
        if endmark is not None:
            payload["endmark"] = endmark
        if markingInfos is not None:
            payload["markingInfos"] = markingInfos

        data = {
            "appid": self.appkey,
            "partner_id": self.partner_id,
            "secret": self.secret,
            "orders": [payload],
        }

        endpoint = "/openapi-api/v1/accountOrder/createBmOrder"
        return self.post(endpoint, data)
    
    def cancel_label_order(self, order_serial_no: str, mailno: str) -> dict:
        """
        Cancel an electronic label order using the cancelBmOrder endpoint.

        Parameters:
            order_serial_no (str): 客户订单号，由字母、数字、下划线组成，必须保证唯一且过滤特殊符号.
            mailno (str): 运单号, 长度13.

        Returns:
            dict: API response.
        """
        orders = [{
            "order_serial_no": order_serial_no,
            "mailno": mailno,
        }]
        payload = {
            "appid": self.appkey,
            "partner_id": self.partner_id,
            "secret": self.secret,
            "orders": orders,
        }
        endpoint = "/openapi-api/v1/accountOrder/cancelBmOrder"
        return self.post(endpoint, payload)

    def cancel(self, orderid: str, backparam=None) -> dict:
        """
        Cancel an order using the order/cancelOrder endpoint.

        Parameters:
            appid (str): app_key.
            orderid (str): Order number.
            backparam (str, optional): Original return field.

        Returns:
            dict: API response.
            {'code': '0000', 'message': '请求成功', 'result': True, 'data': {'orderid': 'order123', 'backparam': None}}
        """
        payload = {"appid": self.appkey, "orderid": orderid}
        if backparam is not None:
            payload["backparam"] = backparam
        endpoint = "/openapi-api/v1/order/cancelOrder"
        return self.post(endpoint, payload)

    def rate(self, startCity: str, endCity: str, weight: str) -> dict:
        """
        Get the shipping rate based on sender and receiver provinces and weight.

        Parameters:
            startCity (str): 寄件人省份/直辖市 （一级地址）.
            endCity (str): 收件人省份/直辖市 （一级地址）.
            weight (str): 重量（kg）.

        Returns:
            dict: API response.
            {'code': '0000', 'data': 17.0, 'message': '请求成功', 'result': True, 'sub_code': None, 'sub_msg': None}
        """
        payload = {"startCity": startCity, "endCity": endCity, "weight": weight}
        endpoint = "/openapi-api/v1/order/getFreightInfo"
        return self.post(endpoint, payload)

    def get_mailno(self, count: int) -> dict:
        """
        Get the mail number using the getNoOrderTxm endpoint.

        Parameters:
            count (list): Number of mail numbers to get.

        Returns:
            dict: API response.
        """
        payload = {
            "appid": self.appkey,
            "partner_id": self.partner_id,
            "secret": self.secret,
            "orders": [
                {
                    "count": str(count),
                    "request_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "mail_type": "common",
                }
            ],
        }
        endpoint = "/openapi/outer/v1/bm/getNoOrderTxm"
        return self.post(endpoint, payload)
