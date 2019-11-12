#! /usr/bin/env python
# coding=utf-8

import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header

# 可依据需要将星花处更换为所使用的服务器、用户名等
# 第三方 SMTP 服务
mail_host = "****"  # 设置服务器
mail_user = "****"  # 用户名
mail_pass = "****"  # 口令


def SendMail(To, Title, mail_msg, From="****", Cc=None):
    """
    :param From: 发件人
    :param To: 收件人
    :param Cc: 抄送
    :param Title: 邮件标题
    :param mail_msg: 邮件内容（可以是html，或文本）
    :return:
    """
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header(From, 'utf-8')
    message['To'] = Header("; ".join(To), 'utf-8')
    if Cc is not None:
        message['Cc'] = Header("; ".join(Cc), 'utf-8')
    message['Subject'] = Header(Title, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(From, To, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"


def sendMessage(number, desc):
    r = requests.get("*****" % (number, desc))
    if r.status_code == 200:
        return "ok"
    else:
        return "failed"

