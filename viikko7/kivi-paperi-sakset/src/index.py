from kps_factory import KPSFactory, Pelityyppi
from konsoli import Konsoli
from tekstit import aloitus_valikko, peliohje


def main():
    io = Konsoli()
    while True:
        io.kirjoita(aloitus_valikko)
        vastaus = io.lue()
        io.kirjoita(peliohje)

        if vastaus.endswith("a"):
            KPSFactory.luo(Pelityyppi.KAKSINPELI).pelaa()
        elif vastaus.endswith("b"):
            KPSFactory.luo(Pelityyppi.TEKOALY).pelaa()
        elif vastaus.endswith("c"):
            KPSFactory.luo(Pelityyppi.PAREMPIALY).pelaa()
        else:
            break


if __name__ == "__main__":
    main()
