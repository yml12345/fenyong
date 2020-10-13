# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：util.py
@时间：2020/9/7  17:34
@文档说明:
"""
import yaml
import os
from setting import DATAS_PATH
import pymysql
from common.mysql_adr import config
import requests


def set_res_data(res):
    '''
    处理响应结果，替换":"（有数据的情况）和":（key的值为空串）为=号
    :param res:
    :return:
    '''
    if res:
        return res.lower().replace('":"', '=').replace('":', '=')

def select_mysql(sql):
    """
    mysql数据库
    :param sql:
    :return:
    """
    db = pymysql.connect(**config)
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    db.close()
    return data

def open_yaml(fail):
    failname = os.path.join(DATAS_PATH,fail)
    with open(failname,'r',encoding='utf-8') as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        return data

print(open_yaml("headers.yaml"))


def base_post_json(url, data):
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


def base_get(url, data):
    """
    封装get请求
    :param url:
    :param data:
    :return:
    """
    headers = open_yaml("headers.yaml")
    header = headers.get("headers")
    rl = requests.get(url=url, params=data, headers=header)
    return rl


def base_post_data(url, data):
    """
    封装post请求
    :param url: 请求地址
    :param data: 请求体
    :return:
    """
    headers = open_yaml("headers.yaml")
    header = headers.get("headers")
    rl = requests.post(url=url, data=data, headers=header)
    return rl



