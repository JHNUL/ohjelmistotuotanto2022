from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def __init__(self, tuomari):
        super().__init__(tuomari)

    def _tokan_siirto(self, ekan_siirto=None):
        return input("Toisen pelaajan siirto: ")
