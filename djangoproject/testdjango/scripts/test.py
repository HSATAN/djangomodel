#coding=utf8

import requests

data={}
url='http://localhost:9999/testmodel/adddb'
for i in range(1,3):
    response=requests.post(url,data={'name':'你好'})
    print(response.status_code)