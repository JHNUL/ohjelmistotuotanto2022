from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def _tokan_siirto(self, ekan_siirto=None):
        return input("Toisen pelaajan siirto: ")
