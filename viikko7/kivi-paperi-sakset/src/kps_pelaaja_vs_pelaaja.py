from kps import KiviPaperiSakset
from tekstit import toka_siirto_input


class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def __init__(self, tuomari):
        super().__init__(tuomari)

    def _tokan_siirto(self, ekan_siirto=None):
        return input(toka_siirto_input)
