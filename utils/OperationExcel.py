# 操作excel
import json
import xlrd
from utils.OperationIni import OperationIni
from src.variable import Variable


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
        table = self.data.sheet_by_index(0)
        title = table.row_values(0)
        test_case = [table.row_values(i) for i in range(1, table.nrows)]
        test_all_case = []
        for value in test_case:
            test_all_case.append(dict(zip(title, value)))
        return test_all_case

    def get_case(self, obj):
        """ 返回执行的测试用例 """
        data = self.get_all_data()
        test_all = []
        for d in data:
            if d[VarName.Run].lower() == 'true':
                test_all.append(self.__processor(d, obj))
        return test_all

    def __processor(self, data, obj):
        """ 处理请求头和 请求内容"""
        new_data = dict(data)
        for key in dict(data).keys():
            if key in (VarName.Header, VarName.Data):
                if dict(data)[key]:     # 不为空
                    son = json.loads(dict(data)[key])
                    for ddt, ddt_value in json.loads(dict(data)[key]).items():
                        if '$'in ddt_value:
                           son[ddt] = obj.get(str(ddt_value[1:]))
                    new_data[key] = son
        return new_data
