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




