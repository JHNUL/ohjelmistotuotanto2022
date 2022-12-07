from kps import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def hae_ekan_valinta(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def hae_tokan_valinta(self):
        return self.tekoaly.anna_siirto()

    def tulosta_tietokoneen_siirto(self, siirto):
        print(f"Tietokone valitsi: {siirto}")
