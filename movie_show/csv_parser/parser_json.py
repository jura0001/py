from datamodel.movie import Movie
import json


class Parser:

    def parse(self, file_name):
        # Parse JSON from file with file_name
        # Returns list of Movie objects
        movies = []
        with open(file_name, 'r') as file:
            # TODO:
            # Parsirajte JSON datoteku, pomocu json paketa.
            # Potrebno je iz liste filmova izvuci ime filma i godinu filma.
            # Primjer datoteke nalazi se u test_data/movies.json
            # Metoda mora vracati listu objekata razreda Movie.
            data = json.load(file)
            for item in data:
                type = item.get('Type')
                if type == 'Movie':
                    name =item.get('Name')
                    year = item.get('Year')
                    year = int(year)
                    movies.append(Movie(name,year))
        return movies