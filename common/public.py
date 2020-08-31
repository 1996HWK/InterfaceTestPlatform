# 返回文件路径
import os


def file_abs_path(*file_name):
    """
       返回文件绝对路径
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), *file_name)


    

