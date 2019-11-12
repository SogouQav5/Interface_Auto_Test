# -*- coding: utf-8 -*-

import os
from src.common.constant import domain, get_interface_url, get_input_params
from src.common.db_manager import DBManager
from src.common.request_interface import RequestInterface

'''

测试请求接口 /api/*****

'''


class TestInterface:
    def __init__(self):
        self.method = "GET"
        self.module_name = os.path.dirname(__file__).split("/")[-1].split("\\")[-1]
        self.classname = self.__class__.__name__
        self.url = domain + get_interface_url(self.module_name, self.classname)
        self.params = get_input_params(self.module_name, self.classname)

    def test_interface(self):
        method, url, params = self.method, self.url, self.params
        response = RequestInterface(method, url, params).request_interface()
        return response.json()


# if __name__ == "__main__":


