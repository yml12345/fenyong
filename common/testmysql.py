# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：testmysql.py
@时间：2020/9/24  16:37
@文档说明:
"""
from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy.ext.declarative import declarative_base



password = 'Renmai@2020'
dbPath = 'mysql+pymysql://ddou:%s@47.56.240.97:5506/dcep_share'%quote_plus(password)
metadata = MetaData()
engine = create_engine(
            dbPath,
            encoding='utf8'
                        )
session_users = sessionmaker(bind=engine)
session = session_users()
dcep_users = Table('dcep_users', metadata, autoload=True, autoload_with=engine)
id = session.query(dcep_users).filter(dcep_users.id == 2001161)
print(id)
