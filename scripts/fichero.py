import pandas as pd

def csv_to_json(path):
    df = pd.read_csv(path, encoding= "ISO-8859-1")
    json = df.to_json(orient="records")
    
    name = "data.json"
    with open(json, "w") as json_file:
        json_file.write(json)
    
    fichero = open(name, "rb")
    
    return fichero

def json_to_csv():
    with open("data.json", "r") as json_file:
        json = json_file.read()
    
    df = pd.read_json(json, orient="records")
    
    name = "data.csv"
    
    df.to_csv(name, index=False)
    
    fichero = open(name, "rb")
    
    return fichero

