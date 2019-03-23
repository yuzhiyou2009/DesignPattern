import os

class AbstractGun():
    gunname = ""
    def shoot(self):
        print("this is gun")
        pass

class Soldier():
    gun = AbstractGun()

    def setGun(self, gun):
        self.gun = gun

    def killEnemy(self):
        self.gun.shoot()
        pass

class Handgun(AbstractGun):
    def shoot(self):
        print("this is handgun")

class Rifle(AbstractGun):
    def shoot(self):
        print("this is rifle")

class Machinegun(AbstractGun):
    def shoot(self):
        print("this is machinegun")

class Snipper(Soldier):
    def zoomDis(self):
        print("snipper look up!")

class AWP(Rifle):
    def shoot(self):
        print("this is AWP!")

if __name__ == '__main__':
    newSoldier = Soldier()
    newSoldier.setGun(AbstractGun())
    newSoldier.killEnemy()

    newSnipper = Snipper()
    newSnipper.setGun(AWP())

    newSnipper.zoomDis()
    newSnipper.killEnemy()

