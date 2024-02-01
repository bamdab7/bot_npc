import requests

id = 2

async def people():
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
        
        info = f"Name -> {name}\nHeight -> {height} \nHomewordl -> {homeworld} \nAppears in -> {str(list_movie)[1:-1]}"
        
        return info
    
async def planets():
    url = f"https://swapi.dev/api/planets/{id}/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Peticion no es valida")
    else: 
        name_planet = response.json()["name"]
        terrain = response.json()["terrain"]
        population = response.json()["population"]
        climate = response.json()["climate"]
        
        info = f"Nome ->{name_planet}\nTerrain -> {terrain}\nPopulation -> {population}\n Climate -> {climate}"
        
        return info

async def starships():
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

        info = f"Vehicle name -> {name_vehicle}\nModel -> {model_vehicle}\nManufacturer -> {manufacturer}\nCrew -> {crew} ppl\nPassengers -> {passengers} ppl"

        return info