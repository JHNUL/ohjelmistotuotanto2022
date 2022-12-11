from kps import KiviPaperiSakset
from tekstit import tietokoneen_siirto


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self, tuomari, tekoaly, io):
        super().__init__(tuomari, io)
        self.tekoaly = tekoaly

    def _tokan_siirto(self, ekan_siirto=None):
        siirto = self.tekoaly.anna_siirto()
        self.io.kirjoita(tietokoneen_siirto.format(siirto))
        return siirto
