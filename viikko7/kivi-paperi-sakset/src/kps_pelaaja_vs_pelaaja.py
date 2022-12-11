from kps import KiviPaperiSakset
from tekstit import toka_siirto_input


class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def __init__(self, tuomari, io):
        super().__init__(tuomari, io)

    def _tokan_siirto(self, ekan_siirto=None):
        return self.io.lue(toka_siirto_input)
