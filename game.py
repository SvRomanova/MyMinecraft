# напиши тут код основного вікна гри
from direct.showbase.ShowBase import ShowBase #модуль для запуску гри
from mapmanager import Mapmanager #модуль для створення мапи
from hero import Hero #модуль для створення гравця


class Game(ShowBase): #основний клас для гри
        ShowBase.__init__(self)
        self.land = Mapmanager() #створення мапи
        x, y = self.land.loadLand("land.txt") #завантаження мапи
        self.hero = Hero((x, y, 2), self.land) #створення гравця
        base.camLens.setFov(90) #встановлення кута огляду камери на сцені

game = Game() #створення обʼєкта гри
game.run() #апуск гри
