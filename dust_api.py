from urllib.parse import urlencode, unquote
import requests
import json
# from jsonbender import bend, S
# from jsonbender.list_ops import ForallBend
# import pandas as pd


url = ' http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst'

params ={'serviceKey' : '0cEPs8B90DcgA%2FMrsi0Fq442uST94X%2FhIY63Gg6ljMRx4FYn%2BB1vMigFHy5%2BTivGGXq%2BvYVkAPefpEyly4StWg%3D%3D',
'serviceKey' : '0cEPs8B90DcgA/Mrsi0Fq442uST94X/hIY63Gg6ljMRx4FYn+B1vMigFHy5+TivGGXq+vYVkAPefpEyly4StWg==',
  'dataType' : 'json', 
  'numOfRows' : '10', 
  'pageNo' : '1',
   'regld' : '11B10101', 
   'tmFc':'202111180600'
    }


response = requests.get(url, params=params)
# print(response.text)
a = json.loads(response.text)
print(a)


# queryURL = url + queryString
# response = requests.get(queryURL)
# print(type(a))




b = a['response']['body']['items']
print(b)


frcstFourDt = []
frcstThreeDt = []
frcstTwoCn = []
gwthcnd = []
frcstTwoDt = []
frcstFourCn = []
frcstThreeCn = []
frcstOneDt = []
frcstOneCn = []
presnatnDt = []


for i in range(len(b)):
    c = b[i]
    frcstFourDt.append(c.get('frcstFourDt'))
    frcstThreeDt.append(c.get('frcstThreeDt'))
    frcstTwoCn.append(c.get('frcstTwoCn'))
    gwthcnd.append(c.get('gwthcnd'))
    frcstTwoDt.append(c.get('frcstTwoDt'))
    frcstFourCn.append(c.get('frcstFourCn'))
    frcstThreeCn.append(c.get('frcstThreeCn'))
    frcstOneDt.append(c.get('frcstOneDt'))
    frcstOneCn.append(c.get('frcstOneDt'))
    presnatnDt.append(c.get('presnatnDt'))


print(frcstFourDt)
print(frcstThreeDt)
print(frcstTwoCn)
print(gwthcnd)
print(frcstTwoDt)
print(frcstFourCn)
print(frcstThreeCn)
print(frcstOneDt)
print(frcstOneCn)
print(presnatnDt)

import pymysql
from pymysql.cursors import Cursor
#DB connect
conn=pymysql.connect(host="localhost",user="root",password="apmsetup",db="weather_db",charset="utf8")
print(conn)
cursor=conn.cursor(pymysql.cursors.DictCursor)

cursor.execute('use dust_db')

sql="""insert into dust_info(frcstFourDt,frcstThreeDt,frcstTwoCn,gwthcnd,frcstTwoDt,frcstFourCn,frcstThreeCn,frcstOneDt,frcstOneCn,presnatnDt) 
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""


for i in range(len(frcstTwoCn)):
    cursor.execute(sql,(str(frcstFourDt[i]),str(frcstThreeDt[i]),str(frcstTwoCn[i]),str(gwthcnd[i]),str(frcstTwoDt[i]),str(frcstFourCn[i]),str(frcstThreeCn[i]),str(frcstOneDt[i]),str(frcstOneCn[i]),str(presnatnDt[i])))

value = cursor.fetchall()
print(value)



conn.commit()
conn.close()

