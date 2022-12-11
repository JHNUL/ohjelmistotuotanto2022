from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from konsoli import Konsoli
from enum import Enum


class Pelityyppi(Enum):
    KAKSINPELI = 1
    TEKOALY = 2
    PAREMPIALY = 3


class KPSFactory:

    def luo(tyyppi):
        if tyyppi == Pelityyppi.KAKSINPELI:
            return KPSPelaajaVsPelaaja(Tuomari(), Konsoli())
        if tyyppi == Pelityyppi.TEKOALY:
            return KPSTekoaly(Tuomari(), Tekoaly(), Konsoli())
        if tyyppi == Pelityyppi.PAREMPIALY:
            return KPSParempiTekoaly(Tuomari(), TekoalyParannettu(10), Konsoli())
