""""
支付结算，分佣
"""
import requests
import unittest
import ddt
import os
from setting import DATAS_ATH
from common.util import select_mysql,open_yaml,base_post_json,base_get


#@ddt.ddt
class PaymentSettlement(unittest.TestCase):

    createOrders = open_yaml("createOrder.yaml")
    createOrder = createOrders.get("createOrder")
    url = createOrder.get("url")
    method = createOrder.get("method")
    print(method)
    data = createOrder.get("data")

    def __init__(self,url,method,data):
        self.url = url
        self.method = method
        self.data = data

    def orderon(self):
        if self.method.lower() == 'post':
            rl = base_post_json(self.url, self.data)
        else:
            rl = base_get(self.url, self.data)
        rl_dict = rl.json()
        if rl_dict.get("data"):
            orderno = rl_dict.get("data").get("orderNo")
            return orderno
        else:
            return "下单失败"

    #@ddt.file_data(os.path.join(DATAS_ATH, "payment_settlement.yaml"))
    # def test_payment_settlement(self):
    #     orderno = self.orderon(self)
    #     #通过数据库查询现金分佣情况
    #     nl_user_cash_rebate_detail = select_mysql("select * from d_native_life.nl_user_cash_rebate_detail where order_no = '%s';" %(orderno))
    #     print(nl_user_cash_rebate_detail)
    #     # nl_user_cash_rebate_detail = select_mysql("select * from d_native_life.nl_user_cash_rebate_detail where order_no = '202009181046245897026'")
    #     # print(nl_user_cash_rebate_detail)
    #     #取出分佣UID、及金额
    #     if nl_user_cash_rebate_detail:
    #         for i in range(len(nl_user_cash_rebate_detail)):
    #             uid = nl_user_cash_rebate_detail[i].get("uid")
    #             rebate_amount = nl_user_cash_rebate_detail[i].get("rebate_amount")
    #             print(uid,rebate_amount)
    #     else:
    #         print("该用户下单后，无现金分佣")
    #
    #     #D豆分佣情况
    #     nl_user_ddou_rebate_detail = select_mysql("select b.* from d_native_life.nl_user_ddou_rebate_detail b where b.order_no='202009181046245897026';")
    #     print(nl_user_ddou_rebate_detail)
    #     if nl_user_ddou_rebate_detail:
    #         for i in range(len(nl_user_ddou_rebate_detail)):
    #             uid = nl_user_ddou_rebate_detail[i].get("uid")
    #             rebate_amount = nl_user_ddou_rebate_detail[i].get("rebate_amount")
    #             print(uid, rebate_amount)
    #     else:
    #         print("该用户无D豆分佣")
    #
    #
    #     #用户等级
    #     nl_user_privilege = select_mysql("select b.*  from d_native_life.nl_user_privilege b where b.uid in (2000830);")
    #     print(nl_user_privilege)



if __name__ == '__main__':
    unittest.main()