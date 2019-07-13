#coding=utf-8
__author__ = 'Mikasa'

class CMouse(object):
    def ___init__(self):
        pass

    def sayHi(self):
        print("A mouse!")

class CDellMouse(CMouse):
    def sayHi(self):
        print("A Dell Mouse!")

class CHpMouse(CMouse):
    def sayHi(self):
        print("A HP Mouse!")


class CMouseFactory(object):
    def CreateMouse(self):
        return

class CDellMouseFactory(CMouseFactory):
    def CreateMouse(self):
        newMouse = CDellMouse()
        return newMouse

class CHpMouseFactory(CMouseFactory):
    def CreateMouse(self):
        newMouse = CHpMouse()
        return newMouse

if __name__ == '__main__':

    newFactory = CDellMouseFactory() #如果是C++则使用基类指针接收
    newMouse = newFactory.CreateMouse() #如果是C++则使用基类指针接收

    newMouse.sayHi()