from bs4 import BeautifulSoup

import requests
url= ""
response = requests.get(url).content
class Parser:
    def parse(self, file_name):
        movies = []
        with open("website.html") as file:
        
            reader = file.read()
            soup = BeautifulSoup(reader,'html.parser')
            names = soup.find_all(name='names')
            years = soup.find_all(name='years')
            for names in names:
                movies.append(names.getText())
        return movies
