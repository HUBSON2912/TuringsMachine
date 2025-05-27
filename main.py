def daj_liczbe_binarnie(liczbaDec):
    liczbaBin = str(bin(liczbaDec))
    return liczbaBin[2:]  # odetnij 0b

def daj_liczbe_oktalnie(liczbaDec):
    liczbaBin = str(oct(liczbaDec))
    return liczbaBin[2:]  # odetnij 0o

def daj_liczbe_haksadecymalnie(liczbaDec):
    liczbaBin = str(hex(liczbaDec))
    return liczbaBin[2:]  # odetnij 0x

class Maszyna:

    # metody "prywatne"    
    def __zmien_system_litera_na_system_liczba(self, litera):
        match litera:
            case 'b':
                return 2
            case 'h':
                return 16
            case 'o':
                return 8
            case 'd':
                return 10
            case _:
                return -1

    def __daj_pusta_lista_o_rozmiarze(self, rozmiar):
        res=[]
        while rozmiar>0:
            rozmiar-=1
            res.append( {"wartosc": None, "system": None} )
        return res

    # metody "publiczne"
    def __init__(self, plik, rozmiar_maksymalny=5, pozycja=0):
        self.tasma=self.__daj_pusta_lista_o_rozmiarze(rozmiar_maksymalny)  # [{"wartosc": w_dec, "system": sys}]
        self.pozycja=pozycja
        self.plik_instrukcje=plik
    
    def dlugoscTasmy(self):
        return len(self.tasma)

    def przesun(self, strona, ilosc):
        nowa_pozycja=self.pozycja
        if strona=='<':
            nowa_pozycja-=ilosc
        elif strona=='>':
            nowa_pozycja+=ilosc
        
        # imitacja nieskończoności taśmy
        if nowa_pozycja<0:
            self.tasma=self.__daj_pusta_lista_o_rozmiarze(abs(nowa_pozycja)) + self.tasma
            nowa_pozycja=0
        elif nowa_pozycja>=self.dlugoscTasmy():
            self.tasma=self.tasma + self.__daj_pusta_lista_o_rozmiarze(nowa_pozycja-self.dlugoscTasmy()+1)
            # nowa_pozycja=self.dlugoscTasmy()

        self.pozycja=nowa_pozycja

    def wczytajLiczbe(self, system_litera, liczba_w_tym_systemie):
        system=self.__zmien_system_litera_na_system_liczba(system_litera)
        liczba=int(liczba_w_tym_systemie, system)
        self.tasma[self.pozycja]= {"wartosc": liczba, "system": system}  # nadpisanie

    def wyswietlLiczbe(self, system):  # system to system NA KTÓRY MA ZOSTAĆ zamieniona liczba
        system=self.__zmien_system_litera_na_system_liczba(system)
        
        if system == -1:
            system=self.tasma[self.pozycja]["system"]
        
        liczbaDec=self.tasma[self.pozycja]["wartosc"]
        match system:
            case 2:
                print(daj_liczbe_binarnie(liczbaDec))
            case 8:
                print(daj_liczbe_oktalnie(liczbaDec))
            case 10:
                print(liczbaDec)
            case 16:
                print(daj_liczbe_haksadecymalnie(liczbaDec))

    def wyswietlTasme(self):
        print("TASMA:")
        indeks=0
        for element in self.tasma:
            print(indeks, element, sep=": ")
            indeks+=1

    def wykonaj(self):
        wejscie=open(self.plik_instrukcje, "r")
        for linia in wejscie:
            if linia[0] == '<' or linia[0] == '>':
                znak, ilosc = linia.split()
                self.przesun(linia[0], int(ilosc))
            elif linia[0] == ',':
                znak, system, liczba=linia.split()
                self.wczytajLiczbe(system, liczba)
            elif linia[0] == '.':
                if linia==".\n" or linia==".":
                    self.wyswietlTasme()
                    continue
                znak, system = linia.split()
                self.wyswietlLiczbe(system)


Maschinengewehr = Maszyna("./instrukcje.txt")
Maschinengewehr.wykonaj()