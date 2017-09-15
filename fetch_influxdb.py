import requests
import urllib2
import json

columns_set = ['name1']
db = 'decision_engine'

sql = "select * from strategy_result where time >='2017-04-29 19:00:00' and time <='2017-04-29 20:00:00'"

url = "http://grail.wacai.info/api/query?db=decision_engine&q=" + urllib2.quote(sql)

results = json.loads(requests.get(url).text).get("results")
if results:
    series = results[0].get("series")
    if series:
        print series[0].get("name")
        print series[0].get("columns")
        for value in series[0].get("values", []):
            for column in value:
                print column, type(column) is str or type(column) is unicode