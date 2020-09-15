# 操作excel
import xlrd
from OperationIni import OperationIni


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


if __name__ == '__main__':
    excel = Excel()
    excel.get_all_data()

