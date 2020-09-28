""" 测试公共方法 """
import public
import json
from src.variable import Variable


var = Variable()
var.set("cookies","dasdasdadasdasdasdadsadsadsa")
var.set("cookies","1111")
print(var.get("cookies"))

# string = '{"cookies":"$cookies","1":"$a"}'
# print(public.create_req_string(var=var, string=string))