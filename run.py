# 执行测试用例
import json
import pytest_html
import pytest
from utils.OperationExcel import Excel,VarName
from utils.OperationIni import OperationIni
from src.SendService import SendService
from src.variable import Variable


# 变量类
var = Variable()

# 获取测试用例
excel = Excel()
case_list = excel.get_case(var)

varName = VarName()

# 生成请求
http = SendService()

# 读取配置
config = OperationIni()

# 请求返回值
res = None

# 测试用例title
test_title = [title[VarName.Title] for title in case_list]


def send_res(data):
    """ 发送请求 """
    global res
    requests_url = config.test_url + data[varName.URl]
    requests_headers = data[varName.Header] if data[varName.Header] else None
    requests_data = data[varName.Data] if data[varName.Data] else None
    if data[varName.Method].lower() == "get":
        res = http.get(
            url=requests_url,
            params=requests_data,
            headers=requests_headers

        )
    elif data[varName.Method].lower() == "post":
        res = http.post(
            url=requests_url,
            data=requests_data,
            headers=requests_headers
        )
        
    return res


def assertion(data, response):
    """ 断言"""
    if data[varName.ContentAssertion]:
        data_json = json.loads(data[varName.ContentAssertion])
        response_json = response.json()
        for key in data_json.keys():
            if data_json[key] != response_json[key]:
                return False
        return True

    else:
        return response.status_code == data[varName.StatusAssertion]

# 执行测试用例
@pytest.mark.parametrize("case_", case_list, ids=test_title)
def test_main(case_):
    response = send_res(case_)
    assert assertion(case_, response) == True
