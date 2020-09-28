# 返回文件路径
import os
import json


def file_abs_path(*file_name):
    """ 返回文件绝对路径  """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), *file_name)


def create_req_string(var, string):
    """ 生成新的请求内容 """
    json_string = json.loads(string)
    key_list = []
    for key, value in json_string.items():
        if "$" in value:
            key_list.append(key)
    value_list = [var.get(json_string[key].split("$")[1]) for key in key_list]
    dict_ = dict(zip(key_list, value_list))
    # update json
    json_string.update(dict_)
    return json_string
    

