import requests
import os
import sys
from bs4 import BeautifulSoup as bs
import webbrowser
#Marcelo Alejandro Rodrigez Hernandez
print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break

#Ete script busca en un rango ingresado las paginas de noticias de la uanl, en especifico
#de la facultad que nosotros nombremos, si en el rango se encuentra la noticia,
#usando beautiful soup nos abrira las paginas relacionadas a la facultad en 
#google chrome, en caso de que no se encuentre no ses abrira nada y si la pagina
#tiene algun status diferente a 200 no se abrira y marcara error en la pagina