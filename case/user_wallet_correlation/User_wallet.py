# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：User_wallet.py
@时间：2020/9/7  15:23
@文档说明:
"""
""""
用户钱包查询
"""
import requests
import unittest
import ddt
import os
from setting import DATAS_ATH
from case.base import Base
from common.util import set_res_data

@ddt.ddt
class UserWallet(Base):

    @ddt.file_data(os.path.join(DATAS_ATH, "user_wallet.yaml"))
    def test_user_wallet(self,**case):
        url = case.get("url")
        method = case.get("method")
        data = case.get("data")
        asql = case.get("asql")
        print(type(asql))

        if method.lower() == 'post':
            rl = self.base_post(url,data)
        else:
            rl = self.base_get(url,data)
        respl = set_res_data(rl.text)
        print(respl)

        #断言
        for i in asql:
            self.assertIn(i,respl)






if __name__ == '__main__':
    unittest.main()