from enum import Enum


class Combatiente():
    _vida = 20
    def vida_restante(self):
        return self._vida

class Arma(Enum):
    punios = 2
    hacha = 10
    espada = 8
    martillo = 8
    daga = 4
    lanza = 8
    palo = 6


class Armadura(Enum):
    cuero = 2
    metal = 6


class Atacante(Combatiente):

    def hacer_danio(self, danio, Victima):
        Victima._vida = Victima._vida - danio
        return Victima._vida

    def usar_arma(self, arma):
        return arma.value
    
class Victima(Combatiente):

    def usar_armadura(self, armadura, danio):
        if(danio > 0):
            danio = danio - armadura.value
        return danio

    def no_esta_herido(self):
        if(self.vida_restante() == 20):
            return True