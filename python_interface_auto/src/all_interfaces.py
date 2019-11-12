# coding=utf-8

import time
import unittest
import HTMLTestRunner
import sys
import os
import requests
import ExSendEmail

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

ROOT = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "..")
PATH = ROOT + "/src"
REPORT_PATH = ROOT + "/report/"


def send_email(receiver, file_name, cc=None):
    tmp = str(upload_result(file_name))
    mail_body = '<p><a href = ' + tmp + '>' + tmp + '</a></p>'
    f = open(file_name, 'rb')
    mail_body += f.read()
    f.close()
    ExSendEmail.SendMail(To=receiver, Title="接口自动化测试报告", mail_msg=mail_body, Cc=cc)


def upload_result(file_name):
    url = 'http://******/se_auto_report/uploadreport.php'
    report_file_name = file_name.split('/')
    files = {'file': (report_file_name[-1], open(file_name, 'rb'))}
    req = requests.post(url, files=files)
    return req.text


def suit():
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(PATH, pattern='run_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
            # print test_unit
    return test_unit


if __name__ == "__main__":
    # 生成测试报告
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    filename = REPORT_PATH + "mallInterfaceTest_" + timestamp + ".html"
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试', description=u'用例执行情况：')

    tmp = str(runner.run(suit()))
    fp.close()

    # 发送邮件

    receivers = ["******"]
    cc = ["******"]

    send_email(receivers, filename, cc)
