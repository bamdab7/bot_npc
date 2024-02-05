import requests 
import pandas as pd
from IPython import display


from dotenv import load_dotenv
import os

url = "https://api.nasa.gov/planetary/apod"

load_dotenv()
api_key = os.getenv("api_key")    




def info_img():
    response = requests.get(url, params = {"api_key" : api_key})
    titulo_image = response.json()["title"]
    descripcion = response.json()["explanation"]

    info = f"*{titulo_image}*\n{descripcion}"
    return info

def daily_img():
    response = requests.get(url, params = {"api_key" : api_key})
    image = response.json()["url"]
    # img = display.Image(image)

    return image
