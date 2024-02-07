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


async def cartelera():
    url_cartelera = "https://www.ecartelera.com/cines/cinesa-marineda-city/"
    pagina_cartelera = requests.get(url_cartelera)
    soup = BeautifulSoup(pagina_cartelera.content, "html.parser")
    
    peliculas = soup.find_all(class_ = "titem")
    
    listado_peliculas = []
    mensaje = " 📽️*CARTELERA*📽️ \n"

    for p in peliculas:
        titulo = p.find(class_ ="tit").text
        link = p.find(class_ = "tit").find("a").get("href")
        
        casts = [actor.text for actor in p.find(class_ = "cast").find_all("a")]
        director = p.find(class_ = "dir").text.replace("Dir.:", "")
        pelicula = [titulo, link, casts, director]
        listado_peliculas.append(pelicula)
    
    for i in listado_peliculas[:10]:
        mensaje += f"*Titulo:* [{i[0]}]({i[1]}) \n👥 *Cast:* {', '.join(i[2])} \n🎥 *Director:* {i[3]} \n \n"

    return mensaje