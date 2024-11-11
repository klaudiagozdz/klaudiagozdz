# Zadanie 1: Napisz funkcję, która znajdzie sumę wszystkich liczb parzystych w liście 
# za pomocą pętli for i operatora warunkowego if.
def oblicz_sume_liczb_parzystych(lista):
    suma = 0
    for element in lista:
        if element %2 == 0:
            suma += element

    return suma
          
        
print(oblicz_sume_liczb_parzystych(3,2,5,7,6)) # 8


# Stwórz funkcję, która znajdzie liczbę nieparzystych elementów w liście 
# przy użyciu pętli for i operatora warunkowego if.
def liczba_nieparzystych_elementow(lista):
    liczba_elementow = 0
    for element in lista:
        if element %2 == 1:
            liczba_elementow +=1
    return liczba_elementow

        

# Utwórz funkcję, która znajdzie drugi największy element w liście 
# za pomocą pętli for i operatora warunkowego if
def drugi_najwiekszy_element(lista):
    # trzeba sie upewnić że lista ma co najmniej 2 elementy
    if len(lista) < 2:
        return None # jezeli lista jest mniejsza ma mniej niz 2 elementy to znaczy że nie istnieje bo my potrzebujemy co najmniej 2 elementów
 
    posortowana_lista = sorted(lista)
    return posortowana_lista[-2]


#Zaimplementuj funkcję, która sprawdzi, czy w liście znajduje się co najmniej jeden element ujemny, 
# korzystając z pętli for i operatora warunkowego if.
def minimum_jeden_ujemny_element(lista):
    for element in lista:
        if element < 0:
            return True
        return False


# Napisz funkcję, która znajdzie liczbę dodatnich liczb w liście 
# przy użyciu pętli for i operatora warunkowego if.
def liczba_dodatnich_elementow(lista):
    liczba_elementow = 0
    for element in lista:
        if element > 0:
            liczba_elementow +=1
    return liczba_elementow


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

    
# Napisz funkcję, która obliczy średnią ocen z listy, 
# za pomocą pętli for i zwróci wynik zaokrąglony do dwóch miejsc po przecinku.
def oblicz_srednia_ocen(lista_ocen):
    if len(lista_ocen) == 0:
        return 0
    for element in lista_ocen:
        suma_ocen += element
        srednia_ocen = suma_ocen/len(lista_ocen)
        return round(srednia_ocen, 2)



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

#Zadanie 1: Funkcja generująca skrót z pierwszych liter każdego słowa Napisz funkcję, 
# która przyjmuje zdanie jako argument i zwraca skrót utworzony z pierwszych liter każdego słowa, zapisany dużymi literami.
# Wynik ma być zwrócony jako jeden ciąg znaków (bez kropek między literami).

#Zadanie 2: Funkcja do konwersji pełnego imienia na nazwisko i inicjał imienia Napisz funkcję, 
# która przyjmuje pełne imię i nazwisko jako argument i zwraca je w formacie: N. Nazwisko, 
# gdzie N to inicjał imienia zapisany wielką literą. Całe nazwisko powinno być również zapisane dużymi literami.

#Zadanie 1: Zwrot unikalnych znaków w kolejności wystąpienia Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca listę unikalnych znaków w kolejności ich pierwszego pojawienia się.
#Przykład:
#Wejście: "abracadabra"
#Oczekiwane wyjście: ['a', 'b', 'r', 'c', 'd']

#Zadanie 2: Znajdowanie najczęściej występującego znaku w ciągu Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca najczęściej występujący znak oraz liczbę jego wystąpień.
#Przykład:
#Wejście: "banana"
#Oczekiwane wyjście: ('a', 3)

#Zadanie 3: Liczenie samogłosek i spółgłosek w ciągu Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca liczbę samogłosek i spółgłosek.
#Przykład:
#Wejście: "hello"
#Oczekiwane wyjście: {'samogloski': 2, 'spolgloski': 3}

#Zadanie 4: Sprawdzenie anagramów Napisz funkcję, która przyjmuje dwa ciągi znaków i sprawdza, 
# czy są one anagramami (tzn. czy składają się z tych samych liter w różnych kolejnościach).
#Przykład:
#Wejście: "listen", "silent"
#Oczekiwane wyjście: True


#Zadanie 5: Liczenie słów w ciągu znaków Napisz funkcję, 
# która przyjmuje ciąg znaków i zwraca słownik z liczbą wystąpień każdego słowa w tym ciągu.
#Przykład:
#Wejście: "to be or not to be"
#Oczekiwane wyjście: {'to': 2, 'be': 2, 'or': 1, 'not': 1}