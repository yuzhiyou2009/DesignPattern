#coding=utf-8

class CDriver(object):
    def ___init__(self):
        pass

    def drive(self, CCar):
        CCar.run()
        pass
    
class CCar(object):
    def __init__(self):
        self.carSize = 0
        pass
    
    def run(self):
        print("this is a car")
        pass
    
class CBenz(CCar):
    def __init__(self):
        pass
    
    def run(self):
        #self.run()
        print("this is a Benz car")

class CHonda(CCar):
    def __init__(self):
        pass

    def run(self):
        #self.run()
        print("this is a Honda car")

if __name__ == '__main__':
    newDriver = CDriver()

    newDriver.drive(CHonda())