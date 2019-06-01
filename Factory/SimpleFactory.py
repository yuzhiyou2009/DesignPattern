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
    def CreateMouse(self, mouseCategory):
        if mouseCategory == 0:
            newMouse = CDellMouse()
            return newMouse
        elif mouseCategory == 1:
            newMouse = CHpMouse()
            return newMouse

if __name__ == '__main__':

    newFactory = CMouseFactory()
    newMouse = newFactory.CreateMouse(1)
    newMouse.sayHi()