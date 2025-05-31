Instrukcje do maszyny Turinga podajesz w pliku `instrukcje.txt`.<br/>
Maszyna obsługuje dwa systemy: **oktalny** (8), **decymalny** (10)

Zachowanie jest podobne do zachowania Brainfucka:<br/>
Możesz wpisać lub wypisać liczbę w dowolnym z obsługiwanych systemów, przesuwać się na boki po "taśmie" oraz dodawać zaznaczone liczby.<br/> W odróżnieniu od BF tutaj taśma imituje nieskończoną: będąc na taśmie w punkcie 0 mogę przesunąć się w lewo tworząc nowe komórki (komórki zawsze są indeksowane od 0).<br/>Jeśli przesuniesz się poza zakres, wybrane do dodawania pozycje też się przesuwają tak, by zaznaczały wciąż tę samą liczbę. 

Możliwe instrukcje:
* `, SYSTEM LICZBA`     -   w obecnym miejscu na taśmię wpisz liczbę zapisaną w systemie SYSTEM
* `. SYSTEM`            -   wypisz liczbę z obecnej pozycji głowicy nad taśmą i zapisz ją w systemie SYSTEM
* `.`                   -   wyświetl całą taśmę w systemie ósemkowym
* `> ILOŚĆ`             -   przesuń się o ILOŚĆ pól w prawo
* `< ILOŚĆ`             -   przesuń się o ILOŚĆ pól w lewo
* `!`                   -   wybierz pierwszy składnik sumy
* `@`                   -   wybierz drugi składnik sumy
* `#`                   -   wybierz pozycję w której ma być zapisana suma
* `+`                   -   dodaj wybrane liczby i zapisz ją w wybranej pozycji. Jeśli nie wybrano wcześniej pozycji z użyciem instrukcji `!`, `@`, `#` wyświetla błąd.

Przykładowe instrukcje:
* `, d 13` - dodaj 13 w systemie dziesiętnym
* `, h 1a` - dodaj 1a w systemie szesnastkowym (26 w dziesiętnym)
* `> 5` - przesuń tasmę w prawo o 5 pól
* `. b` - wyświetl liczbę, nad którą znajduje się głowica, w systemie binarnym
* `+` - dodaj liczby

System ***MUSI*** być jedną literą:
* o - system oktalny
* d - system decymalny
