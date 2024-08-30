from datamodel.movie import Movie
import csv

class Parser:

    def parse(self, file_name):
        # Parse CSV from file with file_name
        # Returns list of Movie objects
        movies = []
        with open(file_name, 'r') as file:
            # TODO:
            # Parsirajte CSV datoteku, delimiter je ';'.
            # Potrebno je iz liste filmova izvuci ime filma i godinu filma.
            # Primjer datoteke nalazi se u `test_data/movies.csv`
            # Metoda mora vracati listu objekata razreda `Movie`.
            reader = csv.reader(file, delimiter=';')
            for row in reader:    
                if row and row[0]=='Movie':   # provjerava je li redak nije prazan       
                        title = row[1]
                        year = row[2]
                        movies.append(Movie(title, year))
        return movies
 
