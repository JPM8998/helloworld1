import pymysql

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='test_ying', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from t_agg_gjj_h5_appy_result;")

# 获取剩余结果的第一行数据
row_1 = cursor.fetchone()
print(row_1)
# 获取剩余结果前n行数据
row_2 = cursor.fetchmany(3)
print(row_2)
# 获取剩余结果所有数据
row_3 = cursor.fetchall()
print(row_3)
conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()
