#Proyecto: Scraping de rankings de tecnologías web más utilizadas
## Descripción
Este proyecto está realizado en Python y se utiliza bibliotecas como Selenium, para la recolección de datos de tres páginas web, y pandas, para la creación de un archivo Excel comparando los rankings adquiridos de cada fuente.

## Características
Recolecta los rankings de lenguajes de programación desde 3 fuentes:
- **PYPL** (PopularitY of Programming Language)
- **TIOBE Index**
- **RedMonk Ranking**

Crea una tabla comparativa en un archivo *Excel***, donde se listan los lenguajes de programación según su ranking en cada una de las fuentes.

## Tecnologías utilizadas
- Python 3.12
- Selenium 4.21.0
- pandas 2.2.3
- [ChromeDriver 130.0.6723.69 Stable Version](https://getwebdriver.com/ "ChromeDriver 130.0.6723.69 Stable Version")
- Navegador Brave

## Instalación
Clonar el siguiente repositorio

`> git clone https://github.com/FrancoEzequielRivera/TP-LP`

Instalar las bibliotecas necesarias

`> pip install -r requirements.txt`

Configurar la ruta de Brave

`23. brave_binary_path = '' ` 

> Nota: agregar la ruta completa de la locación de brave.exe (en la linea 23), por ejemplo, en mi caso es
C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe entre comillas.

## Uso
El script accede a cada una de las tres fuentes de rankings, recolecta los datos de lenguajes de programación y los organiza en un archivo Excel en formato de tabla comparativa. Cada fuente está representada en una columna distinta, y los lenguajes están alineados de acuerdo con su posición en el ranking de cada fuente.

El archivo generado se guarda como comparacion.xlsx.
