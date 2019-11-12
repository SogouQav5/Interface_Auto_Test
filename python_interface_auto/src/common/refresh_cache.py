# -*- coding: utf-8 -*-

import logging
import requests


class RefreshCache:
    def __init__(self):
        self.refresh_all_sku_url = "***"
        self.refresh_all_product_url = "***"
        self.refresh_single_url = "***"
        self.cookie = "***"

    def refresh_all_product_sku_cache(self):
        headers = {'cookie': self.cookie}
        response = requests.post(self.refresh_all_sku_url, headers=headers)
        logging.info("refresh_all_product_cache")
        logging.info(response.url)
        logging.info(response.content)

    def refresh_all_product_list(self):
        headers = {'cookie': self.cookie}
        response = requests.post(self.refresh_all_product_url, headers=headers)
        logging.info("refresh_all_product_list")
        logging.info(response.url)
        logging.info(response.content)

    def refresh_single_product_sku_cache(self, product_id):
        headers = {'cookie': self.cookie}
        params = {'productId': str(product_id)}
        response = requests.post(self.refresh_single_url, params=params, headers=headers)
        logging.info("refresh_single_product_sku_cache")
        logging.info(response.url)
        logging.info(response.content)

