import random
from mozliwosci_wygranej import wygrana, polowiczna_wygrana
znaki = ["$", "@", "-", "#"]

kwota_gracza = input("Jaką kwotą gracz dysponuje ? \n")

# sprawdzenie czy gracz wprowadził kwote w postaci liczby
while kwota_gracza.isdigit() is False:
    try:
        kwota_gracza = int(kwota_gracza)
    except ValueError:
        kwota_gracza = input("Nie podałeś kwoty w formie liczby, podaj liczbę \n")
        continue
kwota_gracza = int(kwota_gracza)

# pobranie stanu konta maszyny
with open("stan_konta.txt", "r") as plik:
    stan_konta = plik.read()
    stan_konta = int(stan_konta)

while True:
    stawka = input("Ile chcesz postawić? \nJeżeli chcesz zakończyć grę wpisz \"esc\"\n")

# zakonczenia gry, aby zakonczyc gre nalezy wprowadzic "esc", aktualny stan konta maszyny jest zapisany do pliku tekstowego
    if stawka == "esc":
        with open("stan_konta.txt", "w") as plik:
            stan_konta = str(stan_konta)
            plik.write(stan_konta)
        break
    else:
        try:
            stawka = int(stawka)
        except ValueError:
            print("Nie podałeś stawki w formie liczby \n")
            continue
    stawka = int(stawka)

# sprawdzenie czy gracz nie podal wiekszej stawki niz dysponuje
    if stawka > kwota_gracza:
        print("Nie dysponujesz taką ilością pieniędzy!!")
        continue
    elif stawka == 0:
        print("Podaj wartość większą niż 0!")
        continue

    losowanie = random.choices(znaki, k=3)
    print(losowanie)

# sprawdzenie wygranej ($$$ = stawka * 50, @@@ lub ### = stawka * 10)
    if losowanie in wygrana:
        if losowanie == wygrana[0]:
            stawka *= 50
            kwota_gracza += stawka
            stan_konta -= stawka
        else:
            stawka *= 10
            kwota_gracza += stawka
            stan_konta -= stawka

# sprawdzenie polowicznej wygranej czyli dwa te same znaki obok siebie które nie są "-" = stawka * 2
    else:
        if polowiczna_wygrana(losowanie[0], losowanie[1], losowanie[2]) is True:
            stawka *= 2
            kwota_gracza += stawka
            stan_konta -= stawka
        else:
            kwota_gracza -= stawka
            stan_konta += stawka
    print(kwota_gracza)

# warunek przegranej
    if kwota_gracza == 0:
        with open("stan_konta.txt", "w") as plik:
            stan_konta = str(stan_konta)
            plik.write(stan_konta)
        print("Przegrałeś :(")
        break