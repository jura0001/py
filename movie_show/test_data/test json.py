import json

with open('test_data/csvjson.json','r') as file:
            # TODO:
            # Parsirajte JSON datoteku, pomocu json paketa.
            # Potrebno je iz liste filmova izvuci ime filma i godinu filma.
            # Primjer datoteke nalazi se u test_data/movies.json
            # Metoda mora vracati listu objekata razreda Movie.
            data = json.load(file)
            
for item in data:
        type = item.get('Type')
        if type == "Movie":
            name = item.get('Name')
            year = item.get('Year')
            print(name,year)
    