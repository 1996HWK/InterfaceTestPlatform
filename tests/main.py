# 执行测试用例
import pytest
from utils.OperationExcel import Excel,VarName


# 获取测试用例
excel = Excel()
case_list = excel.get_case()
varName = VarName()

# 参数化
@pytest.mark.parametrize("case_list", case_list)
def test_main(case_list):



if __name__ == "__main__":
    pytest.main(["main.py"])