from kps import KiviPaperiSakset
from tekstit import tietokoneen_siirto


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, tuomari, tekoalyparannettu, io):
        super().__init__(tuomari, io)
        self.tekoaly = tekoalyparannettu

    def _tokan_siirto(self, ekan_siirto=None):
        siirto = self.tekoaly.anna_siirto()
        self.io.kirjoita(tietokoneen_siirto.format(siirto))
        if ekan_siirto is not None:
            self.tekoaly.aseta_siirto(ekan_siirto)
        return siirto
