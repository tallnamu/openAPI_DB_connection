from urllib.parse import urlencode, unquote
import requests
import json


url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'


queryString = "?" + urlencode(
   {
  "ServiceKey": unquote("0cEPs8B90DcgA%2FMrsi0Fq442uST94X%2FhIY63Gg6ljMRx4FYn%2BB1vMigFHy5%2BTivGGXq%2BvYVkAPefpEyly4StWg%3D%3D"),
  "base_date": "20210819", #기준날짜
  "base_time": "0500", #기준시간
  "nx": 96,
  "ny": 75,
  "numOfRows": "10",
  "pageNo": 1,
  "dataType": "JSON"
}
)

queryURL = url + queryString
response = requests.get(queryURL)
a = json.loads(response.text)
print(type(a))
print(a)




b = a['response']['body']['items']['item']
print(b)


baseDate = []
baseTime = []
category = []
fcstDate = []
fcstTime = []
fcstValue = []
nx = []
ny = []

for i in range(len(b)):
    c = b[i]
    baseDate.append(c.get('baseDate'))
    baseTime.append(c.get('baseTime'))
    category.append(c.get('category'))
    fcstDate.append(c.get('fcstDate'))
    fcstTime.append(c.get('fcstTime'))
    fcstValue.append(c.get('fcstValue'))
    nx.append(c.get('nx'))
    ny.append(c.get('ny'))


print(baseDate)
print(baseTime)
print(category)
print(fcstDate)
print(fcstTime)
print(fcstValue)
print(nx)
print(ny)




import pymysql
from pymysql.cursors import Cursor
#DB connect
conn=pymysql.connect(host="localhost",user="root",password="apmsetup",db="weather_db",charset="utf8")
print(conn)
cursor=conn.cursor(pymysql.cursors.DictCursor)

cursor.execute('use weather_db')

sql="""insert into weather_api(basedate,basetime,category,fcstdate,fcsttime,fcstvalue,nx,ny) 
    values (%s,%s,%s,%s,%s,%s,%s,%s)"""


for i in range(len(baseDate)):
    cursor.execute(sql,(str(baseDate[i]),str(baseTime[i]),str(category[i]),str(fcstDate[i]),str(fcstTime[i]),str(fcstValue[i]),str(nx[i]),str(ny[i])))

value = cursor.fetchall()
print(value)


conn.commit()
conn.close()
