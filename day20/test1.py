# coding:utf-8
import json

dic = {1: 'a', 2: 'b'}
f = open('fff','w',encoding='utf-8')
json.dump(dic,f)
f.close()
