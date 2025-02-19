#!/usr/bin/python3
# @Time    : 2025-02-15
# @Author  : Kevin Kong (kfx2007@163.com)

from cProfile import label
from re import S
from yd.comm import Comm
from yd.order import Order, Label

class YD(object):
    """YunDa SDK"""

    def __init__(self, appkey, appsecret, partner_id=None,secret=None ,sandbox=False):
        """
        Initialization method
        """
        self.appkey = appkey
        self.appsecret = appsecret
        self.sandbox = sandbox
        self.partner_id = partner_id
        self.secret = secret

    comm = Comm()
    order = Order()
    label = Label()