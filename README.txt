Login your taobao account and then do some analysis for yourself, like how much have spent this month, or list the items your have bought up till now.
===General Statement===
This is a spider for www.taobao.com.
It can log in with your account/password and then do some data scraping work for you, like analyze how much have you spent this month or list things you have bought online up till now.
It can be useful for somebody like myself who always shop online.

===LIBRARY IT INVOLVES===
It is achieved by Python3 with Selenium3, if you would like to store these data into a database, you can also use or rewrite MysqlStore class inside.

===HOW TO USE===
Substitue in main_spider.py
mytaobao = taobao.TaoBao("YourTaoBaoAccount", "YourPassword")
With your only account and password and run this script.

===ABOUT VERSION===
Current Version : 1.0

Version  1.0: 
[=Login part=]
Normal log in function. Can not handle slide bar of www.taoao.com.(Because slide bar of www.taoao.com is really different from normal ones, it can seemingly detect whether you are a robot or human.)
[=Data store part=]
Not supported yet.
[=Data analysis part=]
Not supported yet. This version only shows you the data it gets. Data analysis functions like data visualization may be added in the next version.
