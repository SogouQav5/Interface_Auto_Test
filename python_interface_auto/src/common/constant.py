# -*- coding: utf-8 -*-

import os
import logging
import requests
import xml.dom.minidom as xd


domain = "http://***"

root_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "../..")
default_data_dir = root_dir + "/datafile"
input_param_file_dir = "input"

logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=root_dir + '/logs/output.log',
                    filemode='w')


def get_cookie(uname, pwd):
    method = "POST"
    url = "https://***"
    params = {
        "username": str(uname),
        "password": str(pwd),
        "xd": "http://***",
        "client_id": "***"
    }
    cookie = ""
    sess = requests.session()
    response = sess.request(method=method, url=url, params=params)
    cookies = response.cookies
    for i in cookies:
        cookie += str(i).split(" ")[1] + "; "
    logging.info(cookie)
    return cookie


username = ***
password = ***
user_id = ***  # user_id与get_cookie使用的username对应
cart_id = ***  # cart_id与user_id对应

my_cookie = get_cookie(username, password)


# 根据module_name和classname获取接口请求url
def get_interface_url(module_name, classname):
    filename = default_data_dir + "/interface.xml"
    doc = xd.parse(filename)
    root = doc.getElementsByTagName("data")
    if root and len(root) > 0:
        url_list = root[0].getElementsByTagName(module_name)
        for url in url_list:
            tmp = url.getElementsByTagName(classname)[0]
            interface_url = tmp.childNodes[0].data.encode("utf-8")
            return interface_url


# 根据module_name和classname获取接口输入参数
def get_input_params(module_name, classname):
    keys, values = [], []
    fire_dir = default_data_dir + "/" + input_param_file_dir + "/" + module_name
    doc = xd.parse(fire_dir + "/" + classname + ".xml")
    root = doc.getElementsByTagName(classname)
    if root and len(root) > 0:
        param_list = root[0].childNodes
        for param in param_list:
            if not param.nodeName == "#text":
                keys.append(param.nodeName.encode("utf-8"))
        for key in keys:
            try:
                values.append(doc.getElementsByTagName(key)[0].childNodes[0].data.encode("utf-8"))
            except:
                values.append("")
    return dict(zip(keys, values))


# if __name__ == "__main__":