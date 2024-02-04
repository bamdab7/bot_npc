import requests
from random import randrange, random

id = 0

async def people():
    id = 0
    #numero de naves 82
    id = randrange(0, 82)
    url = f"https://swapi.dev/api/people/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        info = f"La identificacion con num {id} de este individuo no esta en nuestra base de datos, prueba otra vez... 👽"
        return info
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
        
        info = f"\n*👽 PERSONAJES 👽*\nNombre: *{name}*\nAltura: *{height} cm*\nProcedencia: *{homeworld}* \nAparece en: *{str(list_movie)[1:-1]}*"
        
        return info
    
async def planets():
    id = 0
    #numero de naves 60
    id = randrange(0, 60)
    url = f"https://swapi.dev/api/planets/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        info = f"El planeta num {id} esta muy lejos, prueba otra vez... 👽"
        return info
    else: 
        name_planet = response.json()["name"]
        terrain = response.json()["terrain"]
        population = response.json()["population"]
        climate = response.json()["climate"]
        
        info = f"\n*🪐 PLANETAS 🪐*\nNombre: *{name_planet}*\nTipo de terreno: *{terrain}*\nPoblacion: *{population}*\nClima: *{climate}*"
        
        return info

async def starships():
    id = randrange(0,36)
    # mi_array = [2,3,5,9,10,11,12,13,15,17,21,22,23,27,28,29,31,32,39,40,41,43,47,48,49,52,]
    # id = random.choice(mi_array)

    url = f"https://swapi.dev/api/starships/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        info = f"Esta nave numero {id} seguro es de nuevos rebeldes,no la conocemos, prueba otra vez... 👽"
        return info
    else: 
        name_vehicle = response.json()["name"]
        model_vehicle = response.json()["model"]
        manufacturer = response.json()["manufacturer"]
        crew = response.json()["crew"]
        passengers = response.json()["passengers"]

        info = f"\n*🛸 NAVES 🛸*\nNombre: *{name_vehicle}*\nModelo: *{model_vehicle}*\nFabricante: *{manufacturer}*\nTripulacion: *{crew} ppl*\nPasajeros: *{passengers} ppl*"

        return info
    
async def species():
    id = 0
    #numero de especies 37
    id = randrange(0, 37)
    url = f"https://swapi.dev/api/species/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        info = f"Especie nueva, todavia no sabemos nada, solo que es la {id} en aparecer, prueba otra vez... 👽"
        return info
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
        
        info = f"\n*🧬 ESPECIES 🧬*\nNombre de especie: *{name_specie}*\nTipo: *{classification}*\nIdioma hablado: *{language}*\nHogar: *{homeworld}* \nEjemplos: *{str(list_people)[1:-1]}*"

        return info

async def films():
    id = 0
    #numero de peliculas 6 (sospechoso btw)
    id = randrange(0, 6)
    url = f"https://swapi.dev/api/films/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        info = f"No hicimos esta peli numero {id}, prueba otra vez... 👽"
        return info
    else: 
        title = response.json()["title"]
        director = response.json()["director"]
        opening_crawl = response.json()["opening_crawl"]

        info = f"\n*📽️ PELICULAS 📽️*\nTitulo *{title}*\nDirector: *{director}*\nInicio: *{opening_crawl}*"

        return info
