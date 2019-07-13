#coding=utf-8
__author__ = 'Mikasa'


class Strategy(object):

    def __init__(self):
        pass

    def AlgActResult(self):
        pass

'''
    这个类是Strategy模式的关键，
    也是Strategy模式和Template模式的根本区别所在。
    *Strategy通过“组合”（委托）方式实现算法（实现）的异构，
    而Template模式则采取的是继承的方式
    这两个模式的区别也是继承和组合两种实现接口重用的方式的区别
'''
class Context(object):

    def __init__(self, newStrategy):
        self.newStrategy = newStrategy
        pass

    def DoAction(self):
        self.newStrategy.AlgActResult()


class CateAStrategy(Strategy):
    def __init__(self):
        super(CateAStrategy, self).__init__()

    def AlgActResult(self):
        print("this is CateAStrategy")


class CateBStrategy(Strategy):
    def __init__(self):
        super(CateBStrategy, self).__init__()

    def AlgActResult(self):
        print("this is CateBStrategy")


if __name__ == '__main__':

    '''
      Strategy模式和Template模式实际是实现一个抽象接口的两种方式：继承和组合之间的区别。
      要实现一个抽象接口，继承是一种方式：我们将抽象接口声明在基类中，将具体的实现放在具体子类中。
      组合（委托）是另外一种方式：我们将接口的实现放在被组合对象中，将抽象接口放在组合类中。
      这两种方式各有优缺点
    '''

    #策略A与B可替换
    newStrategy = CateAStrategy()
    newContext = Context(newStrategy)
    newContext.DoAction()

    newStrategy = CateBStrategy()
    newContext = Context(newStrategy)
    newContext.DoAction()
