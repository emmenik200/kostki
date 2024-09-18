import random

tab = []
test = True


def losowanie():
    num = random.randint(1, 6)  # losowanie liczby
    tab.append(num)

    print("kostka ", x + 1, " ", num)


def sumowanie():
    suma = 0
    j = 1
    size = len(tab)

    # sortowanie
    for i in range(size):
        for j in range(0, size - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]

    # print(tab)              #tablica po sortowaniu

    # liczenie punktów
    for x in range(size - 1):
        y = x + 1

        if tab[x] == tab[y]:
            c = tab[x]
            for z in range(size):
                if tab[z] == c:
                    suma = suma + tab[z]

                    tab[z] = 0

    # print(tab)             #tablica po zliczeniu punktów

    print("suma punktów wynośi: ", suma)


while test == True:
    tab.clear()  # czyszczenie tablicy
    print("Ile kostek? (Od 3 do 10)")
    ile_k = int(input())
    if ile_k < 3 or ile_k > 10:  # sprawdzenie poprawności wpisanego inputu
        print("zła ilość kostek!")
    else:
        for x in range(ile_k):
            losowanie()

    sumowanie()

    # zakończenie programu
    print("jeszcze raz?")
    again = input()
    if again == "t":
        test = True
    elif again == "n":
        test = False
        break
    else:
        print("Error. Wrong input")
        break

    """

    nazwa:          losowanie

    opis:           losuje liczbe od 1 do 6 i dodaje wartość do tablicy oraz wypisuje numer kostki i jej wartość

    paraetry:       num - liczba losowa wstawiana do tablicy
                    x+1 - zmienna wykorzystana w pętli for pokazująca która kostka była 
                        właśnie losowana
    _____________________________________________________________________________________                
    nazwa:          sumowanie

    opis:           pożądkuje tablice i liczy punkty 

    parametry:      suma - ilość punktów 
                    c - zmienna przetrzymująca wartość sprawdzanego elementu tablicy
                    size - ilość elementów w tablicy

    autor: Bartłomiej Cholewiński
    """