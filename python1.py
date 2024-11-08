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
def oblicz_srednia_ocen(lista):
    wyniki = 0
    if wyniki < 50:
        return 2
    

# Napisz funkcję, która obliczy ocenę studenta na podstawie listy liczby punktów zdobytych w różnych przedmiotach. 
# Jeśli przynajmniej połowa przedmiotów ma wynik większy niż 60 punktów, 
# oblicz średnią z tych przedmiotów i przypisz ją jako ocenę. Jeśli nie, przypisz ocenę 2.


# Napisz funkcję, która obliczy ocenę studenta na podstawie wyników z różnych testów. 
# Jeśli przynajmniej połowa testów została zdana (wynik > 60), 
# to ocena to średnia wyników z tych testów. Jeśli nie, ocena wynosi 2.

# Napisz funkcję, która obliczy średnią ważoną ocen studenta, gdzie każda ocena jest reprezentowana przez listę zawierającą 
# dwa elementy: 
# wagę oceny i samą ocenę. Wynik funkcji ma być zaokrąglony do dwóch miejsc po przecinku.

