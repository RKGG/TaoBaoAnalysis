__author__ = "* * treaser 2018 * * "

import taobao
import time


mytaobao = taobao.TaoBao("YourTaoBaoAccount", "YourPassword", "Firefox")
mysql = taobao.MySqlDBStore("YourDatabaseAccount", "YourDatabasePassword")   # root, password

bought_dates = []
item_names = []
bought_prices = []

if mytaobao.login_by_hand(2) == 0:  # 2 means try 2 times
    time.sleep(1)
    data = mytaobao.perform(bought_dates, item_names, bought_prices)
    # mysql.login()
    # mysql.store(bought_dates, item_names, bought_prices)
    store = taobao.Store()
    store.txtstore(data)
    store.excelstore(data)
else:
    print("failed.")

