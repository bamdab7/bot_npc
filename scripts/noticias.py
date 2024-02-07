import requests
from bs4 import BeautifulSoup

async def voz_galicia():
    url_voz_galicia = "https://www.lavozdegalicia.es/coruna/"
    pagina_voz_galicia = requests.get(url_voz_galicia)
    soup = BeautifulSoup(pagina_voz_galicia.content, "html.parser")
    
    noticias = soup.find_all(class_ = "article-min")

    listado_noticias = []
    mensaje = " *📰 LA VOZ DE GALICIA - NOTICIAS 📰* \n \n"
    
    for n in noticias:
        titulo = n.find("h4").text.replace("\n" , "")
        enlace = n.find("a").get("href")
        notice = [titulo,enlace]
        listado_noticias.append(notice)
    
    for i in listado_noticias[:5]: #las 5 mas importantes
        # mensaje+= f"{i[0]} \n _{url_voz_galicia}{i[1]}_ \n \n"
        mensaje+= f"• [{i[0]}]({url_voz_galicia}{i[1]}) \n \n"
    # print(mensaje)
    return mensaje


async def basket():
    url_basket = "https://www.leboro.es/noticias.aspx"

    pagina_basket = requests.get(url_basket)

    soup = BeautifulSoup(pagina_basket.content, "html.parser")
    
    noticias = soup.find_all(class_ = "titulo")
    
    listado_noticias = []
    mensaje = " *🏀 LEB ORO - NOTICIAS 🏀* \n \n"
    
    for n in noticias:
        enlace = n.find("a").get("href")
        titulo = n.find("a").get("title")
        notice = [titulo,enlace]
        listado_noticias.append(notice)
        
    for i in listado_noticias[:5]: #las 5 mas importantes
        # mensaje+= f"{i[0]} \n _{i[1]}_ \n \n"
        
        mensaje += f"• [{i[0]}]({i[1]})\n \n"



    # print(mensaje)
    return mensaje