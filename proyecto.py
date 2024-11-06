from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import pandas as pd

def quitar_no_webs(lista):
    filtro = ["JavaScript", "Python", "Ruby", "PHP", "Java", "C#", "Go", "Golang", "TypeScript", "Kotlin", "Rust", "Perl", "Swift", "R", "Dart", "Elixir", "Scala", "Lua", "Haskell"]
    lista_filtrada = []

    for lenguaje in lista:
        if lenguaje in filtro:
            lista_filtrada.append(lenguaje)

    return lista_filtrada


# Establecer ruta del chromedriver y brave.exe
path_py = os.path.abspath(__file__)
file_path = os.path.dirname(path_py)
ruta_chrome = os.path.join(file_path, "chromedriver.exe") # Ruta de chromedriver.exe
brave_binary_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe' # Ruta de brave.exe

# Configuración del chromedriver y de Brave
service = Service(ruta_chrome)
brave_options = webdriver.ChromeOptions()
brave_options = Options()

# Establecer la ubicación del binario de Brave
brave_options.binary_location = brave_binary_path

# Guardo las configuraciones del navegador
web = webdriver.Chrome(service=service, options=brave_options)

# Navego a la web pypl
web.get('https://pypl.github.io/PYPL.html')

# Selecciono los nombres de los lenguajes
tabla_ranking_pypl = web.find_element(By.TAG_NAME, 'tbody')
lenguajes_pypl = tabla_ranking_pypl.find_elements(By.TAG_NAME, 'tr') # Selecciono cada caja de cada lenguaje
nombre_lenguajes_pypl = [] # Lista donde guardaré los nombres como string

# Recorro cada lenguaje y almaceno los nombres en una lista
for i in range(1, len(lenguajes_pypl)-1):

    caja_lenguaje = lenguajes_pypl[i]
    caja_lenguaje = caja_lenguaje.find_elements(By.TAG_NAME, 'td') # Caja lenguaje tiene datos de un lenguaje

    nombre_lenguajes_pypl.append(caja_lenguaje[2].text)

###############################################################################################################

# Navego a la web tiobe
web.get('https://www.tiobe.com/tiobe-index/')

# Selecciono los nombres de los lenguajes
tabla_ranking_tiobe = web.find_element(By.XPATH, '//*[@id="top20"]/tbody')
lenguajes_tiobe = tabla_ranking_tiobe.find_elements(By.TAG_NAME, 'tr') # Selecciono cada caja de cada lenguaje
nombre_lenguajes_tiobe = [] # Lista donde guardaré los nombres como string

# Recorro cada lenguaje y almaceno los nombres en una lista
for i in range(len(lenguajes_tiobe)):

    caja_lenguaje = lenguajes_tiobe[i]
    caja_lenguaje = caja_lenguaje.find_elements(By.TAG_NAME, 'td') # Caja lenguaje tiene datos de un lenguaje

    nombre_lenguajes_tiobe.append(caja_lenguaje[4].text)

###############################################################################################################

# Navego a la web redmonk
web.get('https://redmonk.com/sogrady/2024/03/08/language-rankings-1-24/')

# Selecciono los nombres de los lenguajes
seccion_nombres_redmonk = web.find_element(By.XPATH, '/html/body/div/div/div/main/div[1]/article/div/p[7]')
lista_nombres_redmonk = seccion_nombres_redmonk.text.splitlines()
nombre_lenguajes_redmonk = [] # Lista donde guardaré los nombres como string
caracteres_indeseados = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Recorro cada nombre de cada lenguaje, quito caracteres indeseados y los almaceno en una lista
for nombre in lista_nombres_redmonk:
    nuevo_nombre = ""
    for letra in nombre:
        if letra not in caracteres_indeseados:
            nuevo_nombre += letra
    nombre_lenguajes_redmonk.append(nuevo_nombre)

# Quito los lenguajes no web de los rankings y limito el tamaño de las listas a 10
nombre_lenguajes_pypl = quitar_no_webs(nombre_lenguajes_pypl)
nombre_lenguajes_pypl = nombre_lenguajes_pypl[:10]

nombre_lenguajes_tiobe = quitar_no_webs(nombre_lenguajes_tiobe)
nombre_lenguajes_tiobe = nombre_lenguajes_tiobe[:10]

nombre_lenguajes_redmonk = quitar_no_webs(nombre_lenguajes_redmonk)
nombre_lenguajes_redmonk = nombre_lenguajes_redmonk[:10]

# Creo un diccionario con lenguajes y sus puntajes
puntajes = {
    "JavaScript": 0,
    "Python": 0,
    "Ruby": 0,
    "PHP": 0,
    "Java": 0,
    "C#": 0,
    "Go": 0,
    "Golang": 0,
    "TypeScript": 0,
    "Kotlin": 0,
    "Rust": 0,
    "Perl": 0,
    "Swift": 0,
    "R": 0,
    "Dart": 0,
    "Elixir": 0,
    "Scala": 0,
    "Lua": 0,
    "Haskell": 0
}

# Asigno un puntaje a cada lenguaje según la posición que ocupe
for lista in [nombre_lenguajes_pypl, nombre_lenguajes_tiobe, nombre_lenguajes_redmonk]:
    for i in range(len(lista)):
        lenguaje = lista[i]
        puntajes[lenguaje] += (10 - i)

# Transformo a puntajes en listas y le asigno un tamaño = 10 a cada una
puntajes_ordenados = dict(sorted(puntajes.items(), key=lambda item: item[1], reverse=True)) # Ordeno los puntajes de forma descendente
puntajes_clave = list(puntajes_ordenados.keys())
puntajes_clave = puntajes_clave[:10]

puntajes_valor = list(puntajes_ordenados.values())
puntajes_valor = puntajes_valor[:10]

# Guardo las listas en un diccionario
datos = {
    'PYPL' : nombre_lenguajes_pypl,
    'TIOBE' : nombre_lenguajes_tiobe,
    'REDMONK' : nombre_lenguajes_redmonk,
    '' : '',
    'Puntaje': puntajes_valor,
    'Lenguaje': puntajes_clave
}

# Creo un Data Frame con el diccionario
dataf = pd.DataFrame(datos)

# Creo un archivo excel con el Data Frame
dataf.to_excel("comparacion.xlsx", index=False)