__author__ = "* * treaser 2018 * * "

import taobao
import time


mytaobao = taobao.TaoBao("YourTaoBaoAccount", "YourPassword")
bought_dates = []
item_names = []
bought_prices = []
if mytaobao.login(2) == 0:
    time.sleep(2)
    mytaobao.go_to_and_do(bought_dates, item_names, bought_prices)
else:
    print("failed.")

