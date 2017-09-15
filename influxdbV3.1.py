import requests
import urllib
import json
import sys
import datetime
import os
import shutil

# if len(sys.argv) != 6:
#    print "param error: "+str(sys.argv)
#    print "The correct parameters should be:db_name tb_name start_date end_date columns[col1,col2..] "
#    sys.exit(1)


database_name = 'decision_engine'
table_name = 'strategy_result'
start_date = '2017-09-15'
end_date = '2017-09-15'
columns = '*'
full_table_name = database_name + '.' + table_name


def daterange(start_date, end_date):
    dates = []
    dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    date = start_date[:]
    while date <= end_date:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def get_data_dir(tmp_dir, tmp_date):
    current_dir = tmp_dir + '/' + tmp_date
    if os.path.exists(current_dir):
        shutil.rmtree(current_dir)
    os.makedirs(current_dir)
    for hour in range(0, 24):
        get_hour_file(current_dir, hour, tmp_date)


def get_hour_file(dir, hour, date):
    file_name = dir + '/' + str(hour) + '.csv'
    if hour==23 :
       date1=datetime.datetime.strptime(date, '%Y-%m-%d')+datetime.timedelta(1)
       date2=date1.strftime('%Y-%m-%d')
       sql= "select " + columns + " from " + table_name + " where time>= '" + str(date) + " " + str(hour) + ":00:00' and time< '" + str(date2)+" 0:00:00'"
    else:
       sql = "select " + columns + " from " + table_name + " where time>= '" + str(date) + " " + str(hour) + ":00:00' and time< '" + str(date) + " " + str(hour+1) + ":00:00'"
    print(sql)
    url = "http://grail.wacai.info/api/query?db=" + database_name + "&q=" + urllib.parse.quote(sql)
    results = json.loads(requests.get(url).text).get("results")
    print(results)
    with open(file_name, 'w') as f:
        print("Name of the file: " + file_name)
        if results:
            series = results[0].get("series")
            if series:
                for row in series[0].get("values", []):
                    data = json.dumps(row)
                    data = data.strip().strip('[]')
                    data = data.replace('"', '')
                    f.write(data)
                    f.write('\n')
    f.close()


tmp_dir = '/Users/jasonying/tmp/' + full_table_name
for tmp_date in daterange(start_date, end_date):
    get_data_dir(tmp_dir, tmp_date)
    print(tmp_date + " success!")
