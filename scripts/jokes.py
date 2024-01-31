import requests

def jokes_bot():
    url = "https://v2.jokeapi.dev/joke/Any?lang=es&format=txt"
    response = requests.get(url)
    return response.text.replace("\n", " ")