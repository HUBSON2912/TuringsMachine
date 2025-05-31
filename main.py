def zamien_znak_na_liczbe(system_litera):
    if system_litera=='o':
        return 8
    elif system_litera=='d':
        return 10
    else:
        return -1

class Maszyna:

    # metody "prywatne"
    def __daj_pusta_lista_o_rozmiarze(self, rozmiar):
        res=[]
        while rozmiar>0:
            rozmiar-=1
            res.append(None)
        return res

    # metody "publiczne"
    def __init__(self, plik, rozmiar_maksymalny=5, pozycja=0):
        self.tasma=self.__daj_pusta_lista_o_rozmiarze(rozmiar_maksymalny)
        self.pozycja=pozycja
        self.plik_instrukcje=plik
        self.dodawanie_pozycja_1=-1
        self.dodawanie_pozycja_2=-1
        self.dodawanie_pozycja_wynik=-1
    
    def dlugoscTasmy(self):
        return len(self.tasma)

    def dodawanie(self):
        if self.dodawanie_pozycja_1==-1 or self.dodawanie_pozycja_2==-1 or self.dodawanie_pozycja_wynik==-1:
            print("ERROR: Nie wybrano pozycji")
            return
        
        self.tasma[self.dodawanie_pozycja_wynik]= self.tasma[self.dodawanie_pozycja_1]+self.tasma[self.dodawanie_pozycja_2]

    def przesun(self, strona, ilosc):
        nowa_pozycja=self.pozycja
        if strona=='<':
            nowa_pozycja-=ilosc
        elif strona=='>':
            nowa_pozycja+=ilosc
        
        # imitacja nieskończoności taśmy
        if nowa_pozycja<0:
            self.tasma=self.__daj_pusta_lista_o_rozmiarze(abs(nowa_pozycja)) + self.tasma
            if self.dodawanie_pozycja_1!=-1:
                self.dodawanie_pozycja_1+=abs(nowa_pozycja)
            if self.dodawanie_pozycja_2!=-1:
                self.dodawanie_pozycja_2+=abs(nowa_pozycja)
            if self.dodawanie_pozycja_wynik!=-1:
                self.dodawanie_pozycja_wynik+=abs(nowa_pozycja)
            nowa_pozycja=0
        elif nowa_pozycja>=self.dlugoscTasmy():
            self.tasma=self.tasma + self.__daj_pusta_lista_o_rozmiarze(nowa_pozycja-self.dlugoscTasmy()+1)
            # nowa_pozycja=self.dlugoscTasmy()

        self.pozycja=nowa_pozycja

    def wczytajLiczbe(self, system_litera, liczba_w_tym_systemie):
        # wybor systemu
        system=zamien_znak_na_liczbe(system_litera)

        if system==-1:  # jeśli niewłaściwy sytstem to NONE
            system=None
            liczba=None
        else:
            liczba=int(liczba_w_tym_systemie, system)
        self.tasma[self.pozycja]=liczba # nadpisanie

    def wyswietlLiczbe(self, system):  # system to system NA KTÓRY MA ZOSTAĆ zamieniona liczba
        system=zamien_znak_na_liczbe(system)
        
        # jesli niewłaściwy system to nic nie rób
        if system == -1:
            return
        
        liczbaDec=self.tasma[self.pozycja]
        match system:
            case 10:
                print(liczbaDec)
            case 8:
                print(oct(liczbaDec)[2:])
            

    def wyswietlTasme(self):
        print("TASMA:")
        indeks=0
        for element in self.tasma:
            if element==None:
                print(indeks, None, sep=": ")
            else:
                print(indeks, oct(element)[2:], sep=": ")
            indeks+=1

    def zaznacz_pozycje(self, ktory_czynnik):
        if ktory_czynnik=='!':
            self.dodawanie_pozycja_1=self.pozycja
        elif ktory_czynnik=='@':
            self.dodawanie_pozycja_2=self.pozycja
        elif ktory_czynnik=='#':
            self.dodawanie_pozycja_wynik=self.pozycja

    def wykonaj(self):
        wejscie=open(self.plik_instrukcje, "r")
        for linia in wejscie:
            # pomiń nieznane instrukcje
            if linia[0] == '<' or linia[0] == '>':
                znak, ilosc = linia.split()
                self.przesun(linia[0], int(ilosc))
            elif linia[0] == ',':
                znak, system, liczba=linia.split()
                self.wczytajLiczbe(system, liczba)
            elif linia[0] == '!' or linia[0] == '@' or linia[0] == '#':
                self.zaznacz_pozycje(linia[0])
            elif linia[0] == '+':
                self.dodawanie()
            elif linia[0] == '.':
                if linia==".\n" or linia==".":
                    self.wyswietlTasme()
                    continue
                znak, system = linia.split()
                self.wyswietlLiczbe(system)


Maschinengewehr = Maszyna("./instrukcje.txt")
Maschinengewehr.wykonaj()