# -*- coding: utf-8 -*-

import os
import pymysql

hive_sql = """
beeline -u jdbc:hive2://hw-node5:10000 -n yarn -p yarn --showHeader=false --outputformat=csv2  -e "
SELECT * from gmall_ads.ads_gmv_increased_daily;
"
"""

result = os.popen(hive_sql)
'''
values = [x[:-1].split(',') for x in result]

db = pymysql.connect('IP地址', '用户名', '密码', '库名')

cursor = db.cursor()  # 创建一个游标对象

mysql_sql = "insert into 库名.表名(col2, col2, col3, col4) values {}".format(
    ",".join('("{}", "{}", {}, "{}")'.format(x[0], x[1], x[2], x[3]) for x in values))
cursor.execute(mysql_sql)
db.commit()

res = cursor.fetchall()
print(res)
db.close()
'''