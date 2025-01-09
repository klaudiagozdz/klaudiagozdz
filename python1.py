# Zadanie 1: Napisz funkcję, która znajdzie sumę wszystkich liczb parzystych w liście 
# za pomocą pętli for i operatora warunkowego if.
def oblicz_sume_liczb_parzystych(lista):
    suma = 0
    for element in lista:
        if element %2 == 0:
            suma += element

    return suma
          
        
print(oblicz_sume_liczb_parzystych(3,2,5,7,6)) # 8

#2
# Stwórz funkcję, która znajdzie liczbę nieparzystych elementów w liście 
# przy użyciu pętli for i operatora warunkowego if.
def liczba_nieparzystych_elementow(lista):
    liczba_elementow = 0
    for element in lista:
        if element %2 == 1:
            liczba_elementow +=1
    return liczba_elementow

        
#3
# Utwórz funkcję, która znajdzie drugi największy element w liście 
# za pomocą pętli for i operatora warunkowego if
def drugi_najwiekszy_element(lista):
    # trzeba sie upewnić że lista ma co najmniej 2 elementy
    if len(lista) < 2:
        return None # jezeli lista jest mniejsza ma mniej niz 2 elementy to znaczy że nie istnieje bo my potrzebujemy co najmniej 2 elementów
 
    posortowana_lista = sorted(lista)
    return posortowana_lista[-2]

#4
#Zaimplementuj funkcję, która sprawdzi, czy w liście znajduje się co najmniej jeden element ujemny, 
# korzystając z pętli for i operatora warunkowego if.
def minimum_jeden_ujemny_element(lista):
    for element in lista:
        if element < 0:
            return True
        return False

#5
# Napisz funkcję, która znajdzie liczbę dodatnich liczb w liście 
# przy użyciu pętli for i operatora warunkowego if.
def liczba_dodatnich_elementow(lista):
    liczba_elementow = 0
    for element in lista:
        if element > 0:
            liczba_elementow +=1
    return liczba_elementow

#6
# Napisz funkcję, która obliczy średnią temperaturę z listy temperatur, 
# za pomocą pętli for i zwróci wynik zaokrąglony do dwóch miejsc po przecinku.
def oblicz_srednia_temperature(lista):
    if len(lista) == 0:
        return 0
    suma = 0
    for element in lista:
        suma += element
        srednia = suma/len(lista)
        return round(srednia, 2)

#7    
# Napisz funkcję, która obliczy średnią ocen z listy, 
# za pomocą pętli for i zwróci wynik zaokrąglony do dwóch miejsc po przecinku.
def oblicz_srednia_ocen(lista_ocen):
    if len(lista_ocen) == 0:
        return 0
    for element in lista_ocen:
        suma_ocen += element
        srednia_ocen = suma_ocen/len(lista_ocen)
        return round(srednia_ocen, 2)


#8
# Napisz funkcję, która obliczy średnią długość słów w liście, 
# za pomocą pętli for i zwróci wynik zaokrąglony do dwóch miejsc po przecinku.
def oblicz_dlugosc_slow(lista_slow):
    if len(lista_slow) == 0:
        return 0
    dlugosc_liter = 0 # nie może być "" bo to ma być jakaś wartość liczbowa
    for element in lista_slow:
        dlugosc_liter += len(element)
    srednia_dlugosc = dlugosc_liter/len(lista_slow) # nie obliczamy średniej w pętli
    return round(srednia_dlugosc, 2)

#Dodawanie długości słów: Zamiast dodawać same słowa, należy dodawać długości tych słów za pomocą len(element).
#dlugosc_liter = 0: Inicjujemy zmienną, która będzie sumować długości wszystkich słów w liście.
#Pętla for: W każdej iteracji pętli dodajemy do zmiennej dlugosc_liter długość bieżącego słowa (funkcja len(element)).
#Po zakończeniu pętli: Obliczamy średnią długość słów, dzieląc sumę długości przez liczbę słów w liście.



#9
# importuj biblioteke statistics i za jej pomoca zaimplementuj 
# funkcje srednia_import
# wynik zaokrąglij do 2 miejsca po przecinku
import statistics
def oblicz_srednia_import(lista):
    srednia = statistics.mean(lista)
    return round(srednia, 2)    
#lista: To lista liczb, z której będziemy obliczać średnią. Wszystkie elementy w tej liście muszą być liczbami 
# (np. całkowitymi lub zmiennoprzecinkowymi).
# statistics.mean(lista): Funkcja ta sumuje wszystkie elementy w liście i dzieli tę sumę przez liczbę elementów 
# w tej liście, aby uzyskać średnią arytmetyczną.



#10
# Napisz funkcję, która obliczy ocenę studenta na podstawie listy wyników egzaminów, przy czym ocena będzie wynosiła 2, 
# jeśli przynajmniej połowa wyników jest niższa od 50 punktów, 
# w przeciwnym razie oblicz średnią z wyników i przypisz ją jako ocenę.
def oblicz_ocene(lista):
    pozytywne_wyniki = [wynik for wynik in lista if wynik >= 50] #Tworzymy listę pozytywne_wyniki, która zawiera tylko te elementy z lista, które są większe lub równe 50.
    if len(pozytywne_wyniki) >= len(lista) /2 : # Sprawdzamy, czy liczba wyników w pozytywne_wyniki jest co najmniej równa połowie liczby wszystkich elementów w lista.
        srednia = sum(pozytywne_wyniki)/ len(pozytywne_wyniki)
        return round(srednia, 2)
    else:
        return 2



    
#11
# Napisz funkcję, która obliczy ocenę studenta na podstawie listy liczby punktów zdobytych w różnych przedmiotach. 
# Jeśli przynajmniej połowa przedmiotów ma wynik większy niż 60 punktów, 
# oblicz średnią z tych przedmiotów i przypisz ją jako ocenę. Jeśli nie, przypisz ocenę 2.
def oblicz_ocene(lista):
    pozytywne_wyniki = [wynik for wynik in lista if wynik > 60]
    if len(pozytywne_wyniki) >= len(lista) / 2 :
        srednia = sum(pozytywne_wyniki)/ len(pozytywne_wyniki)
        return round(srednia, 2)
    else:
        return 2
# zamiast pozytywne wyniki lepiej uzyc ppzytywne przedmioty

#12
# Napisz funkcję, która obliczy ocenę studenta na podstawie wyników z różnych testów. 
# Jeśli przynajmniej połowa testów została zdana (wynik > 60), 
# to ocena to średnia wyników z tych testów. Jeśli nie, ocena wynosi 2.
def oblicz_ocene(lista):
    pozytywne_wyniki = [wynik for wynik in lista > 60]
    if len(pozytywne_wyniki) >= len(lista) / 2:
        srednia = sum(pozytywne_wyniki) / len(pozytywne_wyniki)
        return round(srednia, 2)
    else: 
        return 2
# zamiast pozytywne wyniki można użyć pozytywne testy

#13
# Napisz funkcję, która obliczy średnią ważoną ocen studenta, gdzie każda ocena jest reprezentowana przez listę zawierającą 
# dwa elementy: 
# wagę oceny i samą ocenę. Wynik funkcji ma być zaokrąglony do dwóch miejsc po przecinku.
def oblicz_srednia_wazona(lista):
    suma_wazonych_ocen = sum(ocena * waga for ocena, waga in lista)
    suma_wag = sum(waga for _, waga in lista)
    if suma_wag == 0:
        return 0  # Zapobiega dzieleniu przez zero
    srednia_wazona = suma_wazonych_ocen / suma_wag
    return round(srednia_wazona, 2)

#Zadanie 14: Funkcja generująca skrót z pierwszych liter każdego słowa Napisz funkcję, 
# która przyjmuje zdanie jako argument i zwraca skrót utworzony z pierwszych liter każdego słowa, zapisany dużymi literami.
# Wynik ma być zwrócony jako jeden ciąg znaków (bez kropek między literami).
def pierwsze_litery_slowa(slowa):
    slowa_lista = slowa.split()
    inicjaly = ""
    for element in slowa_lista:
         inicjaly += element[0].upper()
    return inicjaly

#Zadanie 15: Funkcja do konwersji pełnego imienia na nazwisko i inicjał imienia Napisz funkcję, 
# która przyjmuje pełne imię i nazwisko jako argument i zwraca je w formacie: N. Nazwisko, 
# gdzie N to inicjał imienia zapisany wielką literą. Całe nazwisko powinno być również zapisane dużymi literami.
def konwertuj_imie_nazwisko(imie_nazwisko):
    imie_nazwisko_lista = imie_nazwisko.split()
    if len(imie_nazwisko_lista) < 2:
        return "Błędne dane"
    inicjal = imie_nazwisko_lista[0][0].upper + "."  #imie_nazwisko_lista[0] to pierwsze słowo w tej liście (czyli imię).
                                                    #imie_nazwisko_lista[0][0]: Pobiera pierwszy znak pierwszego słowa (czyli pierwszą literę imienia).
    nazwisko = imie_nazwisko_lista[-1].upper()  #imie_nazwisko_lista[-1]: Zwraca ostatni element listy imie_nazwisko_lista, którym jest nazwisko (w przypadku, 
                                                #gdy lista zawiera tylko imię i nazwisko, to będzie to nazwisko).
                                                #.upper(): Zamienia całe nazwisko na wielkie litery
    return inicjal +" "+ nazwisko 




#Zadanie 16: Zwrot unikalnych znaków w kolejności wystąpienia Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca listę unikalnych znaków w kolejności ich pierwszego pojawienia się.
#Przykład:
#Wejście: "abracadabra"
#Oczekiwane wyjście: ['a', 'b', 'r', 'c', 'd']
def zwroc_liste_unikalnych_znakow(ciag):
    napotkane = {}
    for element in ciag:
        if element not in ciag:
            napotkane.append(element) #Użycie add() jest poprawne dla zbiorów (set), ale nie dla list. musi  być append
    return napotkane
          


#Zadanie 17: Znajdowanie najczęściej występującego znaku w ciągu Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca najczęściej występujący znak oraz liczbę jego wystąpień.
#Przykład:
#Wejście: "banana"
#Oczekiwane wyjście: ('a', 3)
def zwroc_najczesciej_wystepujacy_znak(slowo):
    licznik = {}
    for element in slowo:
        if element in slowo:
            licznik[element] += 1
        else:
            licznik[element] = 1
            najczestszy_znak = max(licznik, key=licznik.get)
    return najczestszy_znak, licznik[najczestszy_znak]

#max() to funkcja, która zwraca największy element w podanym iterowalnym obiekcie (w tym przypadku klucz w słowniku licznik).
#key=licznik.get: Argument key pozwala określić, według jakiej zasady max() wybiera największy element. 
#licznik.get jest funkcją, która dla danego klucza zwraca jego wartość (liczbę wystąpień znaku).
#Działanie: max() przegląda wszystkie klucze w licznik i zwraca ten klucz, dla którego licznik.get(klucz) 
# (czyli liczba wystąpień) jest największa.



#Zadanie 18: Liczenie samogłosek i spółgłosek w ciągu Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca liczbę samogłosek i spółgłosek.
#Przykład:
#Wejście: "hello"
#Oczekiwane wyjście: {'samogloski': 2, 'spolgloski': 3}
def zwoc_liczbe_samoglosek_i_spolglosek(slowo):
    licznik = {"samogloski": 0, "spolgloski": 0}
    samogloski = "aeouiyAEOUIY"
    spolgloski = "bBcCDdfFgGHhJjKklLZzVvNnMmWwRrTtPp"
    for element in slowo:
        if element in samogloski:
            licznik["samogloski"] +=1
        elif element in spolgloski:
            licznik["spolgloski"] +=1
    return licznik



#Zadanie 19: Sprawdzenie anagramów Napisz funkcję, która przyjmuje dwa ciągi znaków i sprawdza, 
# czy są one anagramami (tzn. czy składają się z tych samych liter w różnych kolejnościach).
#Przykład:
#Wejście: "listen", "silent"
#Oczekiwane wyjście: True
def czy_anagramy(ciag1, ciag2):
    return sorted(ciag1) == sorted(ciag2)  #Jeśli dwa ciągi mają te same znaki w tej samej liczbie, to po posortowaniu będą wyglądały identycznie





#Zadanie 20: Liczenie słów w ciągu znaków Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca słownik z liczbą wystąpień każdego słowa w tym ciągu.
#Przykład:
#Wejście: "to be or not to be"
#Oczekiwane wyjście: {'to': 2, 'be': 2, 'or': 1, 'not': 1}
def oblicz_slowa_zdanie(zdanie):
    posortowana_zdanie = zdanie.split()
    licznik = {}
    for element in posortowana_zdanie:
        if element in licznik: # nie posortowana_zdanie
            licznik[element] += 1
        else:
            licznik[element] = 1 #Jeśli usuniesz else, funkcja nie będzie wiedziała, co zrobić, gdy napotka nowe słowo
    return licznik



    # 1
# zadeklaruj funkcje oblicz_pole_prostokata, która przyjmuje długości dwóch boków jako dane wejściowe 
# funkcja ma zwracać wielkość pola prostokąta
def oblicz_pole_prostokata(bok1, bok2):
    pole = bok1 * bok2
    return pole



# 2
# zadeklaruj funkcje oblicz_obwod_prostokata, która przyjmuje długości dwóch boków jako dane wejściowe
# funkcja ma zwracać wielkość obwodu prostokąta 
def oblicz_obwod_prostokata(bok1, bok2):
    obwod = 2*bok1 + 2*bok2
    return obwod


# 3 
# zadeklaruj funkcje oblicz_pole_trojkata, która przyjmuje podstawę i wysokość jako dane wejściowe 
# funkcja ma zwracać wielkość pola trójkąta;
def oblicz_pole_trojkata(podstawa, wysokosc):
    pole = 1/2*podstawa * wysokosc
    return pole


# 4
# zadeklaruj funkcję oblicz_obwod_kola, która przyjmuje promień jako daną wejściową
# funkcja ma zwracać wielkość obwodu koła
# podpowiedź: użyj wartości pi z paczki math
import math
def oblicz_obwod_kola(promien):
    obwod = 2 * math.pi * promien
    return obwod


# 5
# zadeklaruj funkcję oblicz_pole_kola, która przyjmuje promień jako daną wejściową
# funkcja ma zwracać wielkość pola koła
import math 
def oblicz_pole_kola(promien):
    pole = math.pi * promien^2
    return pole



# 6
# zadeklaruj funkcję oblicz_pole_trapezu, która przyjmuje długości podstaw i wysokość jako dane wejściowe
# funkcja ma zwracać wielkość pola trapezu
def oblicz_pole_trapezu(podstawa1, podstawa2 wysokosc):
    pole = ((podstawa1 + podstawa2 )* wysokosc) /2
    return pole

# 7
# zadeklaruj funkcję oblicz_objetosc_kuli, która przyjmuje promień jako daną wejściową
# funkcja ma zwracać wielkość objętości kuli
import math
def oblicz_objetosc_kuli(promien):
    objetosc = 4/3 * math.pi * promien**3
    return objetosc


# 8
# zadeklaruj funkcję oblicz_pole_powierzchni_kuli, która przyjmuje promień jako daną wejściową
# funkcja ma zwracać wielkość pola powierzchni kuli




# 11
# zadeklaruj funkcję oblicz_pole_szesciokata, która przyjmuje długość boku jako daną wejściową
# funkcja ma zwracać wielkość pola sześciokąta foremnego
import math
def oblicz_pole_szesciokata(bok):
    pole = ((3 * math.sqrt(3)) / 2) * bok**2
    return pole




# 19
# zadeklaruj funkcję oblicz_cene_z_vatem, która przyjmuje cenę netto i stawkę VAT jako dane wejściowe
# funkcja ma zwracać cenę brutto (z VAT)
def oblicz_cene_z_vatem(cena_netto, VAT):
    cena_z_vat = cena_netto * (1 + VAT / 100)
    return cena_z_vat



# 2
# zadeklaruj funkcję oblicz_kilometry_na_mile, która przyjmuje wartość liczbową kilometrów
# funkcja ma zwracać liczbę mil 
# przyjmij, że 1 km = 0.6214 mili
# rozwiązanie zaokrąglij do 2 miejsca po przecinku
def oblicz_kilometry_na_mile(km):
    wartosc = km * 0.6214
    return round(wartosc, 2)


# 3
# zadeklaruj funkcję oblicz_funty_na_kilogramy, która przyjmuje wartość liczbową funtów
# funkcja ma zwracać liczbę kilogramów 
# przyjmij, że 1 funt = 0.4536 kg
# rozwiązanie zaokrąglij do 2 miejsca po przecinku
def oblicz_funty_na_kilogramy(funty):
    wynik = funty * 0.4536
    return round(wynik, 2)



# 4
# zadeklaruj funkcję oblicz_celsjusze_na_fahrenheity, która przyjmuje wartość liczbową stopni Celsjusza
# funkcja ma zwracać liczbę stopni Fahrenheita 
# wzór: F = C * 9/5 + 32
# rozwiązanie zaokrąglij do 2 miejsca po przecinku
def oblicz_celsjusze_na_fahrenheity(celsjusz):
    wynik = (celsjusz * 9/5) + 32
    return round(wynik, 2)


# 6
# zadeklaruj funkcję oblicz_minuty_na_godziny, która przyjmuje wartość liczbową minut
# funkcja ma zwracać liczbę godzin 
# rozwiązanie zaokrąglij do 2 miejsca po przecinku
def oblicz_minuty_na_godziny(minuta):
    wynik = minuta /60
    return round(wynik, 2)



# 7
# Zadeklaruj funkcję wymien_slowa_po_przecinku, ktora przyjmuje łańcuch znaków 
# funkcja ma zwrócić łańcuch znaków, którego słowa orginalnego łańcucha zostały
# podzielone przecinkiem, jak w przykładzie poniżej:
# Przykład: "tosty ser szynka" --> "tosty, ser, szynka"
def wymien_slowa_po_przecinku(tekst):
    slowa = tekst.split()
    return ",".join(slowa)




# 8
# Zadeklaruj funkcję polacz_slowa_z_kreskami, ktora przyjmuje łańcuch znaków 
# funkcja ma zwrócić łańcuch znaków, którego słowa orginalnego łańcucha zostały
# połączone kreskami, jak w przykładzie poniżej:
# Przykład: "pies kot mysz" --> "pies-kot-mysz"
def polacz_slowa_z_kreskami(tekst):
    slowa = tekst.splt()
    return "-".join(slowa)



# 9
# Zadeklaruj funkcję odwroc_slowa, ktora przyjmuje łańcuch znaków 
# funkcja ma zwrócić łańcuch znaków, którego słowa orginalnego łańcucha zostały
# odwrócone, jak w przykładzie poniżej:
# Przykład: "dom drzewo rzeka" --> "mod owerzd ekar"
def odwroc_slowa(ciag):
    slowa = ciag.split()
    slowa_odwrocone = [slowo[::-1] for slowo in slowa]
    return slowa_odwrocone





# 10
# Zadeklaruj funkcję zamien_na_duze_litery, ktora przyjmuje łańcuch znaków 
# funkcja ma zwrócić łańcuch znaków, którego wszystkie litery zostały zamienione
# na duże, jak w przykładzie poniżej:
# Przykład: "dzień dobry" --> "DZIEŃ DOBRY"
def zamien_na_duze_litery(tekst):
    wynik = " "
    for litera in tekst:
        if litera.islower():
            wynik += litera.upper()
         
        return wynik

    



# 11
# Zadeklaruj funkcję zamien_na_male_litery, ktora przyjmuje łańcuch znaków 
# funkcja ma zwrócić łańcuch znaków, którego wszystkie litery zostały zamienione
# na małe, jak w przykładzie poniżej:
# Przykład: "WITAJ ŚWIECIE" --> "witaj świecie"

