# -*- coding: utf-8 -*-

import unittest
import logging
from src.test.test_interface import TestInterface


class TESTInterface(unittest.TestCase):
    ''' 测试接口 '''

    def setUp(self):
        # print "\n================================================"
        # print "*** Start ***"
        pass

    def tearDown(self):
        # print
        pass

    def test_test_interface_without_params(self):
        ''' 测试case：缺少请求参数，校验返回码正确性 '''
        logging.info("test_test_interface_without_params")
        gpi = TestInterface()
        params = {}
        response = gpi.test_interface(params)['code']
        # print response
        self.assertEquals(response, 404, msg="返回码错误, code = " + str(response))