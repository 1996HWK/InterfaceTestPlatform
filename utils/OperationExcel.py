# 操作excel
import xlrd
from utils.OperationIni import OperationIni


class VarName(object):
    Module = "模块"
    Title = "测试标题"
    Run = "执行"
    URl = "请求地址"
    Method = "请求方法"
    Header = "请求头"
    Data = "请求内容"
    ContentAssertion = "内容断言"
    StatusAssertion = "状态码"
    SaveDate = "保存数据"


class Excel(object):

    def __init__(self):
        self.data = self._get_data()

    @staticmethod
    def _get_data():
        data = xlrd.open_workbook(OperationIni().test_case_path)
        return data

    def get_all_data(self):
        """ 返回所有的数据 """
        table = self.data.sheet_by_name("Sheet1")
        title = table.row_values(0)
        test_case = [table.row_values(i) for i in range(1, table.nrows)]
        test_all_case = []
        for value in test_case:
            test_all_case.append(dict(zip(title, value)))
        return test_all_case

    def get_case(self):
        """ 返回执行的测试用例 """
        data = self.get_all_data()
        test_all = []
        for d in data:
            if d[VarName.Run] == "turn":
                test_all.append(d)

        return test_all



