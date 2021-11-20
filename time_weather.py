from urllib.parse import urlencode, unquote
import requests
import json



url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'

params ={'serviceKey' : '0cEPs8B90DcgA/Mrsi0Fq442uST94X/hIY63Gg6ljMRx4FYn+B1vMigFHy5+TivGGXq+vYVkAPefpEyly4StWg==', 
'pageNo' : '1', 
'numOfRows' : '10', 
'dataType' : 'json', 
'dataCd' : 'ASOS',
'dateCd' : 'HR', 
'startDt' : '20211115',
'startHh' : '07',
'endDt' : '20211117',
'endHh' : '07',
'stnIds' : '108' }


response = requests.get(url, params=params)
# print(response.text)
a = json.loads(response.text)
print(a)






b = a['response']['body']['items']['item']
print(b)


tm=[]
rnum=[]
stnId=[]
stnNm=[]
ta=[]
ws=[]
wd=[]
hm=[]
pv=[]
td=[]
pa=[]
ps=[]
ssQcflg=[]
dc10Tca=[]
dc10LmcsCa=[]
vs=[]
dmstMtphNo=[]
ts=[]
m005Te=[]
m01Te=[]
m02Te=[]
m03Te=[]


for i in range(len(b)):
    c = b[i]
    tm.append(c.get('tm'))
    rnum.append(c.get('rnum'))
    stnId.append(c.get('stnId'))
    stnNm.append(c.get('stnNm'))
    ta.append(c.get('ta'))
    ws.append(c.get('ws'))
    wd.append(c.get('wd'))
    hm.append(c.get('hm'))
    pv.append(c.get('pv'))
    td.append(c.get('td'))
    pa.append(c.get('pa'))
    ps.append(c.get('ps'))
    ssQcflg.append(c.get('ssQcflg'))
    dc10Tca.append(c.get('dc10Tca'))
    dc10LmcsCa.append(c.get('dc10LmcsCa'))
    vs.append(c.get('vs'))
    dmstMtphNo.append(c.get('dmstMtphNo'))
    ts.append(c.get('ts'))
    m005Te.append(c.get('m005Te'))
    m01Te.append(c.get('m01Te'))
    m005Te.append(c.get('m005Te'))
    m02Te.append(c.get('m02Te'))
    m03Te.append(c.get('m03Te'))


print(tm)
print(rnum)
print(stnId)
# print(stnNm)
print(ta)
print(ws)
print(wd)
print(hm)
print(pv)
print(td)
print(pa)
print(ps)
print(ssQcflg)
print(dc10Tca)
print(dc10LmcsCa)
print(vs)
print(dmstMtphNo)
print(ts)
print(m005Te)
print(m01Te)
print(m02Te)
print(m03Te)

import pymysql
from pymysql.cursors import Cursor
conn=pymysql.connect(host="localhost",user="root",password="apmsetup",db="time_weather_db",charset="utf8")
print(conn)
cursor=conn.cursor(pymysql.cursors.DictCursor)

cursor.execute('use time_weather_db')

sql="""insert into tw_info(tm,rnum,stnId,ta,ws,wd,hm,pv,td,pa,ssQcflg,dc10Tca,dc10LmcsCa,vs,dmstMtphNo,ts,m005Te,m01Te,m02Te,m03Te) 
     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""


for i in range(len(tm)):
    cursor.execute(sql,((str(tm[i]),str(rnum[i]),str(stnId[i]),str(ta[i]),str(ws[i]),str(wd[i]),str(hm[i]),str(pv[i]),str(td[i]),str(pa[i]),str(ssQcflg[i]),str(dc10Tca[i]),str(dc10LmcsCa[i]),str(vs[i]),str(dmstMtphNo[i]),str(ts[i]),str(m005Te[i]),str(m01Te[i]),str(m02Te[i]),str(m03Te[i]))))

value = cursor.fetchall()
print(value)


sql2="""select *from tw_info"""
cursor.execute(sql2)
select=list(cursor.fetchall())

conn.commit()
conn.close()
print(select)
with open('data.json','w') as fp:
    json.dump(select,fp)

with open("data.json",'r') as fp:
    data=json.load(fp)
    print(data)