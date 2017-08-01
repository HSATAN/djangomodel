#coding=utf8

import requests

data={}
url='http://localhost:9999/testmodel/adddb'
for i in range(1,20):
    r_get=requests.get(url)
    print(r_get.cookies)
    data['name']=str(i)
    headers={'Cookie':'jjjjjjjjjjjjjjjjjjjjjjjj'}
    response=requests.post(url,data=data,headers=headers)
    print(response.status_code)