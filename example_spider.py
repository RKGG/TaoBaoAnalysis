__author__ = "* * treaser 2018 * * "

import taobao
import time


mytaobao = taobao.TaoBao("YourTaoBaoAccount", "YourPassword")
mysql = taobao.MySqlDBStore("YourDatabaseAccount","YourDatabasePassword")   # root, password

bought_dates = []
item_names = []
bought_prices = []
if mytaobao.login(2) == 0:
    time.sleep(2)
    mytaobao.perform(bought_dates, item_names, bought_prices)
    mysql.login()
else:
    print("failed.")

