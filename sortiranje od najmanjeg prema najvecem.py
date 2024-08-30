def najmanji(lista, start, end):
    # Pronalaženje indeksa najmanjeg elementa u podlisti
    min_index = start
    for i in range(start + 1, end + 1):
        if lista[i] < lista[min_index]:
            min_index = i
    return min_index

def zamijeni(lista, i, j):
    # Zamjena mjesta dvaju elemenata u listi
    lista[i], lista[j] = lista[j], lista[i]

def sortiraj(lista):
    # Kopiranje liste kako se originalna lista ne bi mijenjala
    lista = lista[:]
    
    # Implementacija Selection Sort algoritma
    for i in range(len(lista)):
        min_index = najmanji(lista, i, len(lista)-1)
        zamijeni(lista, i, min_index)
    
    return lista

# Primjer upotrebe:
lista = [64, 25, 12, 22, 11]
sortirana_lista = sortiraj(lista)
print(sortirana_lista)  # Očekivani ishod: [11, 12, 22, 25, 64]