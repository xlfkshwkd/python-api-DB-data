import requests
import json
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
service_key="J5/Thyhm4DvmlWk5EqTakaX7ebIJRjlo7NGylmQ2DeA8qutXiaW6K2mlk9yKXgZMm+IeKw/Ft9QQEZ7U
svP3lg=="
params ={'serviceKey' : service_key,
'pageNo' : '1',
'numOfRows' : '1000',
'dataType' : 'JSON',
'base_date' : '20220501',
'base_time' : '1200',
'nx' : '68',
'ny' : '101' }
res = requests.get(url, params=params)
print(res.text)
print(res.status_code, type(res.text),res.url)
print("===== response json data start =====")
print(res)
print("===== response json data end =====")
print()
r_dict = json.loads(res.text)
r_response = r_dict.get("response")
r_body = r_response.get("body")
r_items = r_body.get("items")
r_item = r_items.get("item")
result = {}
for item in r_item:
if(item.get("category") == "T1H"):
result = item
break
print("===== response dictionary(python object) data start =====")
print(result)
print("===== response dictionary(python object) end =====")
print()
JSON