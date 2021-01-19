# 执行测试用例
import json
import pytest
from utils.OperationExcel import Excel,VarName
from utils.OperationIni import OperationIni
from utils.SaveVariable import SaveVariable
from src.SendService import SendService
from src.variable import Variable


# 变量类
var = Variable()

# 获取测试用例
excel = Excel()
case_list = excel.get_case()

varName = VarName()

# 生成请求
http = SendService()

# 读取配置
config = OperationIni()

# 保存全局变量
save = SaveVariable()

# 请求返回值
res = None

# 测试用例title
test_title = [title[VarName.Title] for title in case_list]


def send_res(data, var_obj):
    """ 发送请求 """
    global res
    requests_url = config.test_url + data[varName.URl]
    requests_headers = excel.processor(data[varName.Header] if data[varName.Header] else None, var_obj)
    requests_data = excel.processor(data[varName.Data] if data[varName.Data] else None, var_obj)
    if data[varName.Method].lower() == "get":
        res = http.get(
            url=requests_url,
            params=requests_data,
            headers=requests_headers

        )
    elif data[varName.Method].lower() == "post":
        res = http.post(
            url=requests_url,
            json=requests_data,
            headers=requests_headers
        )
    return res


def assertion(data, response):
    """ 断言"""
    if data[varName.ContentAssertion]:
        data_json = json.loads(data[varName.ContentAssertion])
        response_json = response.json()
        print("接口返回结果:", response_json)
        for key in data_json.keys():
            if data_json[key] != response_json[key]:
                return False
        return True

    else:
        return response.status_code == data[varName.StatusAssertion]

# 执行测试用例
@pytest.mark.parametrize("case_", case_list, ids=test_title)
def test_main(case_):
    response = send_res(case_, var)
    # 保存变量
    if case_[varName.SaveDate]:
        save.save(response.json(), var, case_[varName.SaveDate])
    
    assert assertion(case_, response) == True


if __name__ == "__main__":
    pytest.main(["run.py","-f", "--html", "./report/report.html"])