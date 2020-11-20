# 执行测试用例
import json
import pytest
from utils.OperationExcel import Excel,VarName
from utils.OperationIni import OperationIni
from src.SendService import SendService


# 获取测试用例
excel = Excel()
case_list = excel.get_case()
varName = VarName()

# 生成请求
http = SendService()

# 读取配置
config = OperationIni()

# 参数化
@pytest.mark.parametrize("case_list", case_list)
def test_main(case_list):
    requests_url = config.test_url + case_list[varName.URl]
    requests_headers = case_list[varName.Header] if case_list[varName.Header] else None
    requests_data = case_list[varName.Data] if case_list[varName.Data] else None

    if case_list[varName.Method].lower == "get":
        response = http.get(

        )
    elif case_list[varName.Method].lower == "post":
        response = http.post(
            
        )

    

if __name__ == "__main__":
    pytest.main(["main.py","-f"])