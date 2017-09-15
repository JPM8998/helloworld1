import pymysql
from pathlib import Path

database_name = 'decision_engine'
table_name = 'strategy_result'
full_table_name = database_name + '.' + table_name
tmp_dir = '/Users/jasonying/tmp/' + full_table_name

# 1.
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='test_ying',
                       charset="utf8")  # db：库名,注意字符集

cursor = conn.cursor()

sql2 = '''drop table if exists yunsong0913;
        create  table yunsong0913
        (
          id           int primary key not null auto_increment comment '自增主键',
          time         varchar(30) comment '时间',
          commitId     varchar(30) comment '提交ID',
          costTime     varchar(30) comment '花费时间',
          errorcode    varchar(30) comment '错误代码',
          reason       varchar(30) comment '原因',
          status       varchar(30) comment '状态',
          strategycode varchar(30) comment '战略代码',
          uid          varchar(30) comment '挖财uid',
          uuid         varchar(30) comment '挖财uuid',
          index idx_time(time)
        ) comment    'influxdb数据表'; '''
print("sql2: " + sql2)
result2 = cursor.execute(sql2)
print(result2)

result2_all = cursor.fetchall()
print(result2_all)
conn.commit()

# 2.
path = Path(tmp_dir)
all_txt_file = list(path.glob('**/*.txt'))
write_file_name = '/Users/jasonying/tmp/load_data.txt'
for txt_file in all_txt_file:
    with open(txt_file, 'r') as f:
        txt_result = f.read()
    with open(write_file_name, 'w') as w:
        w.write(txt_result)
        w.write('\n')

    print(str(txt_file) + " success!")

cursor.close()
conn.close()
