from tekstit import eka_siirto_input


class KiviPaperiSakset:

    def __init__(self, tuomari, io):
        self.tuomari = tuomari
        self.io = io

    def pelaa(self):

        ekan_siirto = self._ekan_siirto()
        tokan_siirto = self._tokan_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.io.kirjoita(self.tuomari)

            ekan_siirto = self._ekan_siirto()
            tokan_siirto = self._tokan_siirto(ekan_siirto)

        self.io.kirjoita("Kiitos!")
        self.io.kirjoita(self.tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]

    def _ekan_siirto(self):
        return self.io.lue(eka_siirto_input)

    def _tokan_siirto(self, ekan_siirto):
        return "k"
