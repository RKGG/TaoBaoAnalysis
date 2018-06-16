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
Current Version : 1.2


Version  1.0: 
[=Login part=]
Normal log in function. Can not handle slide bar of www.taoao.com (Because the slide bar of www.taoao.com is infamously different from normal ones, it can seemingly detect whether you are a robot or human.)
[=Data store part=]
Not supported yet.
[=Data analysis part=]
Not supported yet. This version only shows you the data it gets. Data analysis functions like data visualization may be added in the next version.


Version 1.1:
[=Data store part=]
Implement data store via MySql, but you need first create a TABLE in mysql like:
mysql> create table taobaoanalysis(
    -> id int NOT NULL AUTO_INCREMENT,
    -> bought_date char(20) NOT NULL,
    -> item_names char(50),
    -> bought_prices char(10),
    -> primary key(id)
    -> )character set = utf8;
After the program ran, you can use " SELECT * FROM taobaoanalysis; " in mysql command line to see the result.

Next Version May Improve:
1. Set the waiting time more proper in class TaoBao.
2. More safer mysql operation, check data before store in case of redundancies.
3. Support for more file format store, like .txt, .excel ...


Version 1.2:
[=Login part=]
Cut down some unnecessary waiting time.
[=Data store part=]
Implement data store via txt and excel, you can use like:
    store = taobao.Store()
    store.txtstore(data)
    store.excelstore(data)
Next Version May Improve:
1. More safer mysql operation, check data before store in case of redundancies.
2. Support for your whole account data analysis.
3. Variable pass improvement.

Version 1.3:
Facing fatal problem:
When use Selenium open Taobao login page, the server of taobao will recognize me as a robot even ifI just use Selenium
Webdriver to open the login website(www.login.taobao.com) and type the username and password by my hand and slide the
slide bar by hand. Which means the moment I open the website via Python Selenium program, the taobao server recognizes me
as a spider and want to block me no matter latter operations are done by true human or robot. It actually didn't detect
whether I am a robot or human by slide bar or other.
