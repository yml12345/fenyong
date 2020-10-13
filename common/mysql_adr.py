# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：mysql_adr.py
@时间：2020/9/24  17:38
@文档说明:
"""
import pymysql
config = {
    'host':'47.56.240.97',
    'port':5506,
    'user':'ddou',
    'password':'Renmai@2020',
    'db':'dcep_share',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor
}