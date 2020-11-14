# 操作配置文件
import os
import configparser
from common.public import file_abs_path


class OperationIni(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(file_abs_path("config", "config.ini"), "utf-8")

    @staticmethod
    def check_value(result):
        " 检查value"
        if not result:
            raise Exception("测试用例路径为空")
        else:
            return result

    @property
    def test_case_path(self):
        "返回测试用例文件路径"
        file_path = self.config.get("DEFAULT", "Test_Case")
        if self.check_value(file_path):
            return file_abs_path("data", file_path)
        else:
            return None
        
    @property
    def test_url(self):
        """ 返回测试地址 """
        test_url_path = self.config.get("DEFAULT", "Test_Url")
        return test_url_path



        





    

