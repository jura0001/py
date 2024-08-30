def broji_samoglasnike(text):
    # Osiguravamo da je ulazni parametar string
    text = str(text)
    samoglasnici = "aeiouAEIOU"
    broj_samoglasnika = 0
    
    # Brojimo samoglasnike u tekstu
    for char in text:
        if char in samoglasnici:
            broj_samoglasnika += 1
    
    return broj_samoglasnika

# Primjer upotrebe:
tekst = "Ovo je primjer teksta."
broj = broji_samoglasnike(tekst)
print(broj)  # Očekivani ishod: 8




def broji_samoglasnike1(rijec):
    rijec = str(rijec)
    samoglasnici = "aeiouAEIOU"
    broj_samoglasnika = 0

    for char in rijec:
        if char in samoglasnici:
            broj_samoglasnika +=1

    return broj_samoglasnika


rijec = "Ovo je probna raaijec"

broj1= broji_samoglasnike1(rijec)
print(broj1)