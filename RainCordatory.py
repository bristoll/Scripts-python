# Acceder a google
# buscar tiempo+ciudad
# acceder al dato de precipitaciones de google (a traves del id que esta dentro de un span  id="wob_pp")
#dato >40% es que va a llover!
# enviar ese dato por correo
#import requests
from bs4 import BeautifulSoup    
import requests
#class="dia d-2 clearfix dlD"
#class="rain T4Loc color-texto-t50-0"

#obtenemos la pagina y lo guardamos en documento
peticion=requests.get("http://www.tiempo.com/palmas-de-gran-canaria-las.htm")
#En texto guardamos solo la parte del html con .text
texto=peticion.text
#formateamos el documentocomo html para mayor facilidad
documento= BeautifulSoup(peticion.text, 'html.parser')
#Buscamos con .find el tag title ( da problemas con class)
dia2= documento.findAll("dl",{"class":"dia d-2 clearfix dlD"})
#Con get_text nos quedamos solo con el texto flanqueado por el tag
dia2=BeautifulSoup(str(dia2),"html.parser")

rain=dia2.find("dd",{"class":"rain T4Loc"})
if rain == None:
	print("No hay previsión de precipitaciones.")
	input()
else:
	rain=BeautifulSoup(str(rain),"html.parser")
	lluvia=rain.find("abbr")
	dato=lluvia.get_text()
	print(rain)
	print("")
	print(dato)
	input()
