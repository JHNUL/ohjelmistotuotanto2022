from enum import Enum
from komennot import Lisaa, Poista, Kuuluu, Kasvata


class Komento(Enum):
    LISAA = 1
    POISTA = 2
    KUULUU = 3
    KASVATA = 4


class Komentotehdas:
    @staticmethod
    def luo(komento: 'Komento'):
        if komento == Komento.LISAA:
            return Lisaa()
        if komento == Komento.POISTA:
            return Poista()
        if komento == Komento.KUULUU:
            return Kuuluu()
        if komento == Komento.KASVATA:
            return Kasvata()
        raise NotImplementedError(f"komentoa {komento} ei tunneta")
