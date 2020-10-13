# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：base.py
@时间：2020/9/8  16:58
@文档说明:
"""
import requests
import ddt
import unittest
from common.util import open_yaml
import pymysql
from common.mysql_adr import config


class Base(unittest.TestCase):
    # def __init__(self):
    #     pass

    def base_post(self,url,data):
        """
        封装post请求
        :param url: 请求地址
        :param data: 请求体
        :return:
        """
        headers = open_yaml("headers.yaml")
        header = headers.get("headers")
        rl = requests.post(url=url, json=data, headers=header)
        return rl

    def base_get(self,url,data):
        """
        封装get请求
        :param url:
        :param data:
        :return:
        """
        headers=open_yaml("headers.yaml")
        header=headers.get("headers")
        rl = requests.get(url=url, params=data, headers=header)
        return rl

    def nl_user_cash_rebate_detail(self,sql):
        """
        现金分佣详情
        :param sql: SQL语句
        :return:
        """
        self.db = pymysql.connect(**config)
        self.cur = self.db.cursor()
        self.sql = sql
        self.cur.execute(self.sql)
        self.data = self.cur.fetchall()
        self.db.close()
        return self.data






if __name__ == '__main__':
    unittest.main()