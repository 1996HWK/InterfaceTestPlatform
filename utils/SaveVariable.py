""" 保存全局变量 """


class SaveVariable(object):
    def __init__(self):
        pass

    def save(self, string, var, save_dict):
        """
        :param string: 接口返回值
        :param var:保存变量类实例
        :param save_dict:需要保存的数据
        """
        response_data = string
        var = var
        save_dict = eval(save_dict)
        try:
            if save_dict:
                """ 保存数据 """
                for key, value in save_dict.items():
                    var.set(key, eval(value))
            else:
                """ 如果字符串为空，不保存数据 """
                pass
        except Exception as e:
            pass
