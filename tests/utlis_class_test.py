""" 测试工具类 """
from utils.SaveVariable import SaveVariable
from src.variable import Variable

var = Variable()
SaveVariable('{"a":"111"}', var)

print(var.get("a"))
print(var.get("b"))