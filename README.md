JESTEŚMY LUDEM WYBRANYM! BOGACTWO DLA NAS, WŁADZA DLA BELIARA.

Instrukcje do maszyny Turinga podajesz w pliku `instrukcje.txt`.<br/>
Maszyna obsługuje cztery systemy: **binarny** (2), **oktalny** (8), **decymalny** (10) i **heksadecymalny** (16).

Zachowanie jest podobne do zachowania Brainfucka:<br/>
Możesz wpisać lub wypisać liczbę w dowolnym systemie oraz przesuwać się na boki po "taśmie". <br/> W odróżnieniu od BF tutaj taśma imituje nieskończoną: będąc na taśmie w punkcie 0 mogę przesunąć się w lewo tworząc nowe komórki (komórki zawsze są indeksowane od 0).

Możliwe instrukcje:
* `, SYSTEM LICZBA`     -   w obecnym miejscu na taśmię wpisz liczbę zapisaną w systemie SYSTEM
* `. SYSTEM`            -   wypisz liczbę z obecnej pozycji głowicy nad taśmą i zapisz ją w systemie SYSTEM
* `.`                   -   wyświetl całą taśmę
* `> ILOŚĆ`             -   przesuń się o ILOŚĆ pól w prawo
* `< ILOŚĆ`             -   przesuń się o ILOŚĆ pól w lewo

System ***MUSI*** być jedną literą:
* b - system binarny
* o - system oktalny
* d - system decymalny
* h - system heksadecymalny