import requests
import pandas as pd


def meteo_bot():
    ceo_json = pd.read_json("scripts/ceo.json") 
    vento_json = pd.read_json("scripts/vento.json")

    url = " https://servizos.meteogalicia.gal/mgrss/predicion/jsonPredConcellos.action"
    response = requests.get(url,params = {"idConc" : 15050})

    nomeConcello = response.json()["predConcello"]["nome"]
    tMax = response.json()["predConcello"]["listaPredDiaConcello"][0]["tMax"]
    tMin = response.json()["predConcello"]["listaPredDiaConcello"][0]["tMin"]
    ceo = response.json()["predConcello"]["listaPredDiaConcello"][0]["ceo"]
    vento = response.json()["predConcello"]["listaPredDiaConcello"][0]["vento"]

    ceo_valor_manha = ceo["manha"]
    ceo_valor_noite = ceo["noite"]
    ceo_valor_tarde = ceo["tarde"]

    vento_valor_manha = vento["manha"]
    vento_valor_noite = vento["noite"]
    vento_valor_tarde = vento["tarde"]

    #-----------------------------CEO
    filtro_manha_ceo = ceo_json['valor'] == ceo_valor_manha
    estado_manha_ceo = ceo_json.loc[filtro_manha_ceo, 'estado'].values[0]

    filtro_tarde_ceo = ceo_json['valor'] == ceo_valor_tarde
    estado_tarde_ceo = ceo_json.loc[filtro_tarde_ceo, 'estado'].values[0]

    filtro_noite_ceo = ceo_json['valor'] == ceo_valor_noite
    estado_noite_ceo = ceo_json.loc[filtro_noite_ceo, 'estado'].values[0]

    #----------------------------VENTO
    filtro_manha_vento = vento_json['valor'] == vento_valor_manha
    estado_manha_vento = vento_json.loc[filtro_manha_vento, 'estado'].values[0]

    filtro_tarde_vento = vento_json['valor'] == vento_valor_tarde
    estado_tarde_vento = vento_json.loc[filtro_tarde_vento, 'estado'].values[0]

    filtro_noite_vento = vento_json['valor'] == vento_valor_noite
    estado_noite_vento = vento_json.loc[filtro_noite_vento, 'estado'].values[0]

    # linea1 = "O concello seleccionado é {nomeConcello}\nTemperatura maxima de hoxe -> {tMax}º \nTemperatura minima de hoxe -> {tMin}º"
    # linea2 = "Estado do ceo pola maña -> {estado_manha_ceo} \nEstado do ceo pola tarde -> {estado_tarde_ceo} \nEstado do ceo pola noite -> {estado_noite_ceo}"
    # linea3 = "Estado do vento pola maña -> {estado_manha_vento}\nEstado do vento pola tarde -> {estado_tarde_vento} \nEstado do vento pola noite -> {estado_noite_vento}"

    # return linea1, linea2, linea3

    informacion_meteo = (
            f"O concello seleccionado é *{nomeConcello}* \n"
            f"Temperatura máxima de hoxe -> *{tMax}º*\n"
            f"Temperatura mínima de hoxe -> *{tMin}º*\n\n"
            f"Estado do ceo pola maña -> *{estado_manha_ceo}*\n"
            f"Estado do ceo pola tarde -> *{estado_tarde_ceo}*\n"
            f"Estado do ceo pola noite -> *{estado_noite_ceo}*\n\n"
            f"Estado do vento pola maña -> *{estado_manha_vento}*\n"
            f"Estado do vento pola tarde -> *{estado_tarde_vento}*\n"
            f"Estado do vento pola noite -> *{estado_noite_vento}*"
        )

    return informacion_meteo
    
