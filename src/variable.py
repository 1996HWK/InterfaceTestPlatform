# 存储环境变量
class Variable(object):

    def get(self, value):
        """ 获取全局值 """
        return getattr(self, value, None)

    def set(self, key, value):
        """ 设置全局变量 """
        setattr(self, key, value)









