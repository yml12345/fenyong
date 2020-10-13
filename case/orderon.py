"""
@作者：cloveryml
@文件名：orderon.py
@时间：2020/9/30  17:25
@文档说明:
"""

from case.base import Base
import ddt
import os
from setting import DATAS_PATH
import unittest

@ddt.ddt
class OrderOn(Base):

    @ddt.file_data(os.path.join(DATAS_PATH,"payment_settlement.yaml"))
    def test_orderno(self,**case):
        url = case.get("url")
        method = case.get("method")
        data = case.get("data")

        if method.lower() == 'post':
            rl = self.base_post(url,data)
        else:
            rl = self.base_get(url,data)
        rl_dict = rl.json()
        print(rl_dict)
        # if rl_dict.get("data"):
        #     orderno = rl_dict.get("data").get("orderNo")
        #     return orderno
        # else:
        #     return "下单失败"


if __name__ == '__main__':
    unittest.main()