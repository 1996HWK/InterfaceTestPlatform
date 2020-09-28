""" 保存全局变量 """
import json


class SaveVariable(object):
    def __init__(self, string, var):
        """
        :param string: 一段josn
        """
        self.json_string = string
        self.var = var
        try:
            if self.json_string:
                """ 需要保存数据 """
                # 检查json
                result = self.__check_json()
                if result:
                    """ 保存操作 """
                    for key, value in result.items():
                        var.set(key, value)
                else:
                    print("不操作")
            else:
                """ 如果字符串为空，不保存数据 """
                # pass
                print("不操作")

        except Exception as e:
            # pass
            print("不操作", e)

    def __check_json(self):
        """
        检查json，是否存在问题
        """
        try:
            # change json
            result = json.loads(self.json_string)
            return result

        except Exception as e:
            return None


