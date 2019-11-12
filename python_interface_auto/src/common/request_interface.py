# -*- coding: utf-8 -*-

import logging
import requests
from src.common.constant import my_cookie


class RequestInterface:
    def __init__(self, method, url, params):
        self.method = method
        self.url = url
        self.params = params
        self.cookie = my_cookie

    def request_interface(self, need_login=1, cookie=None):
        """
        封装请求接口的方法，提供请求方法、url和入参
        :param need_login: 默认为1，表示需要cookie，取其他值请求接口时只带传入的个性化cookie
        :param cookie: 个性化定制cookie，默认为None
        :return: 接口返回
        """
        if need_login == 1:
            if cookie is None:
                login_cookie = self.cookie
            else:
                login_cookie = cookie
        else:
            login_cookie = cookie

        headers = {'cookie': login_cookie}
        response = requests.request(self.method, self.url, headers=headers, params=self.params)
        logging.info(response.url)
        logging.info(response.content)
        return response

    def request_interface_without_cookie(self):
        """
        封装请求接口的方法，提供请求方法、url和入参  不传cookie情况
        :return:
        """
        headers = {'cookie': None}
        response = requests.request(self.method, self.url, headers=headers, params=self.params)
        logging.info(response.url)
        logging.info(response.content)
        return response
