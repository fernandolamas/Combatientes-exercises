import unittest

from combatientes import Atacante, Victima, Arma, Armadura


class TestCombatientes(unittest.TestCase):

    def test01LosPuniosHacen2DeDanio(self):
        atacante = Atacante()
        victima = Victima()
        danio = atacante.usar_arma(arma=Arma.punios)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 18)

    def test02MultiplesAtaquesVanBajandoMasVida(self):
        atacante = Atacante()
        victima = Victima()
        danio = atacante.usar_arma(arma=Arma.punios)

        atacante.hacer_danio(danio=danio, Victima=victima)
        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 16)

    def test03UnHachaHace10DeDanio(self):
        atacante = Atacante()
        victima = Victima()
        danio = atacante.usar_arma(arma=Arma.hacha)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 10)

    def test04UnEspadaHace8DeDanio(self):
        atacante = Atacante()
        victima = Victima()
        danio = atacante.usar_arma(arma=Arma.espada)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 12)

    def test05UnaArmaduraDeCueroAbsorve2DeDanio(self):
        atacante = Atacante()
        victima = Victima()
        danio = atacante.usar_arma(arma=Arma.martillo)
        danio = victima.usar_armadura(armadura=Armadura.cuero, danio=danio)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 14)

    def test06UnaArmaduraDeMetalAbsorve2DeDanio(self):
        atacante = Atacante()
        victima = Victima()
        danio = atacante.usar_arma(arma=Arma.martillo)
        danio = victima.usar_armadura(armadura=Armadura.metal, danio=danio)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 18)

    def test07UnaArmaduraReduceElDanioInflingidoACero(self):
        atacante = Atacante()
        victima = Victima()

        danio = victima.usar_armadura(armadura=Armadura.metal, danio=0)

        atacante.hacer_danio(danio=danio, Victima=victima)
        self.assertTrue(victima.no_esta_herido())

    def test08UnMartilloHace8DeDanio(self):
        atacante = Atacante()
        victima = Victima()

        danio = atacante.usar_arma(arma=Arma.martillo)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 12)

    def test09UnaDagaHace4DeDanio(self):
        atacante = Atacante()
        victima = Victima()

        danio = atacante.usar_arma(arma=Arma.daga)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 16)


    def test09UnaLanzaHace8DeDanio(self):
        atacante = Atacante()
        victima = Victima()

        danio = atacante.usar_arma(arma=Arma.lanza)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 12)

    def test09UnPaloHace6DeDanio(self):
        atacante = Atacante()
        victima = Victima()

        danio = atacante.usar_arma(arma=Arma.palo)

        atacante.hacer_danio(danio=danio, Victima=victima)

        self.assertTrue(victima.vida_restante() == 14)