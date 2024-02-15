import pandas as pd
from io import StringIO

def csv_to_json(nombre_fichero,path):
    df = pd.read_csv(path, encoding= "ISO-8859-1")
    json = df.to_json(orient="records")
    
    name = f"{nombre_fichero}.json"
    with open(name, "w") as json_file:
        json_file.write(json)
    
    fichero = open(name, "rb")
    
    return fichero

def json_to_csv(nombre_fichero):
    with open("data.json", "r") as json_file:
        json = json_file.read()
    
    df = pd.read_json(json, orient="records")
    
    name = f"{nombre_fichero}.csv"
    
    df.to_csv(name, index=False)
    
    fichero = open(name, "rb")
    
    return fichero

def info_fichero_csv(path):
    df = pd.read_csv(path, encoding="ISO-8859-1")

    with StringIO() as s:
        df.info(buf=s)
        cabecera = s.getvalue()
    
    return cabecera
    
    
def info_fichero_json(path):
    df = pd.read_json(path, orient="records")

    with StringIO() as s:
        df.info(buf=s)
        cabecera = s.getvalue()
    
    return cabecera