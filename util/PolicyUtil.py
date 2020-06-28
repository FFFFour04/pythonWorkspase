
# 获取股票数据公共方法
# 不同路径引入，需要在路径下有__init__.py的空文件
class PolicyUtil:

    def __init__(self,name):
        self.name = name

    def getDog(self):
        print('run test:'+self.name)