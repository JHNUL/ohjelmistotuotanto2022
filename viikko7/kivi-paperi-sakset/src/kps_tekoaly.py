from kps import KiviPaperiSakset
from tekstit import tietokoneen_siirto


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self, tuomari, tekoaly):
        super().__init__(tuomari)
        self.tekoaly = tekoaly

    def _tokan_siirto(self, ekan_siirto=None):
        siirto = self.tekoaly.anna_siirto()
        print(tietokoneen_siirto.format(siirto))
        return siirto
