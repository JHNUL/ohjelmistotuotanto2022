from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def hae_ekan_valinta(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def hae_tokan_valinta(self):
        return self.tekoaly.anna_siirto()

    def tulosta_tietokoneen_siirto(self, siirto):
        print(f"Tietokone valitsi: {siirto}")

    def aseta_tietokoneen_siirto(self, siirto):
        self.tekoaly.aseta_siirto(siirto)
