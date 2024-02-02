import requests
from random import randrange, uniform

# id = 2

async def people():
    #numero de naves 82
    id = randrange(0, 82)
    url = f"https://swapi.dev/api/people/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Peticion no es valida")
    else: 
        name = response.json()["name"]
        height = response.json()["height"]

        url_homeworld = response.json()["homeworld"]
        response_homeworld = requests.get(url_homeworld)
        homeworld = response_homeworld.json()["name"]

        url_movie = response.json()["films"]
        list_movie = []
        for url in url_movie:
            peli = requests.get(url)
            movie = peli.json()["title"]
            list_movie.append(movie)
        
        info = f"Nombre: {name}\nAltura: {height} cm \nProcedencia: {homeworld} \nAparece en: {str(list_movie)[1:-1]}"
        
        return info
    
async def planets():
    #numero de naves 60
    id = randrange(0, 60)
    url = f"https://swapi.dev/api/planets/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Peticion no es valida")
    else: 
        name_planet = response.json()["name"]
        terrain = response.json()["terrain"]
        population = response.json()["population"]
        climate = response.json()["climate"]
        
        info = f"Nombre: {name_planet}\nTipo de terreno: {terrain}\nPoblacion: {population}\nClima: {climate}"
        
        return info

async def starships():
    #numero de naves 36
    id = randrange(0, 36)
    url = f"https://swapi.dev/api/starships/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Peticion no es valida")
    else: 
        name_vehicle = response.json()["name"]
        model_vehicle = response.json()["model"]
        manufacturer = response.json()["manufacturer"]
        crew = response.json()["crew"]
        passengers = response.json()["passengers"]

        info = f"Nombre: {name_vehicle}\nModelo: {model_vehicle}\nFabricante: {manufacturer}\nTripulacion: {crew} ppl\nPasajeros: {passengers} ppl"

        return info
    
async def species():
    #numero de especies 37
    id = randrange(0, 37)
    url = f"https://swapi.dev/api/species/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Peticion no es valida")
    else: 
        name_specie = response.json()["name"]
        classification = response.json()["classification"]

        url_homeworld = response.json()["homeworld"]
        response_homeworld = requests.get(url_homeworld)
        homeworld = response_homeworld.json()["name"]

        language = response.json()["language"]

        url_people = response.json()["people"]
        list_people = []
        for url in url_people:
            p = requests.get(url)
            people = p.json()["name"]
            list_people.append(people)
        
        info = f"Nombre de especie: {name_specie}\nTipo: {classification}\nIdioma hablado: {language}\nHogar: {homeworld} \nEjemplos: {str(list_people)[1:-1]}"

        return info

async def films():
    #numero de peliculas 6 (sospechoso btw)
    id = randrange(0, 6)
    url = f"https://swapi.dev/api/films/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Peticion no es valida")
    else: 
        title = response.json()["title"]
        director = response.json()["director"]
        opening_crawl = response.json()["opening_crawl"]

        info = f"titulo {title}\nDirector: {director}\nInicio: {opening_crawl}"

        return info
