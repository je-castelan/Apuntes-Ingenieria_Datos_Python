APUNTES INGENIERÍA DE DATOS CON PYTHON (ANACONDA)
=================================================

### Índice ###

 * [Instalación](instalación)
 * [Hola mundo](#hola-mundo)
 * [Creación de entorno virtual](#Creación-de-entorno-virtual)
 * [Tipos de datos](#Tipos-de-datos)
 * [Fuentes de datos](#Fuentes-de-datos)
 * [ETL](#etl)
 * [Introducción a las tecnologías web](#Introducción-a-las-tecnologías-web)
 * [Realizar solicitudes HTTP con Python](#Realizar-solicitudes-HTTP-con-Python)
 * [Cómo trabajar con un documento HTML](#Cómo-trabajar-con-un-documento-HTML)
 * [Analizando un sitio web para encontrar las directivas a utilizar al hacer un web scrapping](#Analizando-un-sitio-web-para-encontrar-las-directivas-a-utilizar-al-hacer-un-web-scrapping)
 * [Solicitudes a la web mediante Requests](#Solicitudes-a-la-web-mediante-Requests)
 * [Implementación de web Scrapper](#Implementación-de-web-Scrapper)

## Instalación ##

Se realiza la descarga del aplicativo en su [página oficial](https://www.anaconda.com/download), donde se observan la instrucciónes para diversos sistemas operativos.

Este puede generar conflicto con la terminal zsh, la cual puede ser corregida siguiendo los pasos dando click [aquí](https://medium.com/@sumitmenon/how-to-get-anaconda-to-work-with-oh-my-zsh-on-mac-os-x-7c1c7247d896)

Se revisa que anaconda haya quedado instalado correctamente con el siguiente comando

> conda --version

Para conocer que comandos podemos usar usamos --help

> conda --help

Para desplegar los paquetes que se instalaron usamos list

> conda list 

## Creación de entorno virtual ##

Creamos un ambiente virtual como buena práctica usando el siguiente comando

> conda create --name [nombre-del-proyecto] [librerías-a-usar] 

Aquí un ejemplo

> conda create --name dataengine beautifulsoup4 requests numpy pandas matplotlib yaml

Para activar el entorno virtual, usamos: 

> source activate dataengine 
 
Para salir del entorno virtual usamos:

> source deactivate 

Usamos `env list` para mostrar los ambientes virtuales existentes

> conda env list

Para eliminar entornos, usamos el siguiente comando

> conda remove --name [nombre-del-proyecto]

 
## Hola mundo ##

Para acceder a Jupyter, usamos el siguiente comando, el cual abre un portal en tu browser.

> jupyter notebook

En Jupyner, se usan diversos teclas rápidas que a continuación se listan.
> CNTL + ENTER - Ejecuta una línea

> SHIFT + ENTER - Ejecuta una línea y crea una nueva

> ESC - Cambia de modo edición (verde) y navegación (azul)

A continuación, algunas teclas rápidas en modo navegación

> B -> Nueva linea 

> P-> Barra de ayuda 

> X-> Corta 

> V -> Pegar 

> DD -> Eliminar 

> M -> Modo markdown 

En modo markdown, uso estas ediciones de texto

> # para tamaño H1

> ## para H2 

>  **ASI SALE NEGRILLAS** 

> *Así de hacen cursivas* 

## Tipos de datos ##

Existen

 - `Primitivos` Los existentes en los lenguajes de programación como bool, str, int, obj, float
 - `Estructurados` Parten de bases de datos (SQL)
 - `Semiestructurados` Parten de elementos ordenados pero sin un orden consecutivo (HTML)
 - `No estructurados` Parten de una información sin orden lógico visible

## Fuentes de datos ##

 - `Web` Es una mina enorme con datos financieros, de startups, del clima, precipitación fluvial, astronómicos, de negocios, etc. 
 - `APIs` Endpoints que viven en la web y nos devuelven JSON. Por ejemplo, la API de twitter, google, facebook.
 - `User Analytics` Son el comportamiento del usuario dentro de nuestra aplicaciones, algo similiar a los que nos ofrece Google Analytics. 
 - `IoT - sensores` Se ha vuelto una mina espectacular en los últimos años. Como automóviles.
 - `Datasets públicos` Algunas páginas recomendadas son Google Datasets y data.world y Kaggle.

## ETL ##

Significa Extract Transform Load

 - `Extract` Es el proceso de lectura de datos de diversas fuentes
   * Base de datos
   * CRM
   * Archivos CSV
   * Datasets públicos

 - `Transform` En este momento cuando nosotros tenemos que transformar los datos, tenemos que identificar datos faltantes o datos erróneos o una edad negativa. En esta etapa donde tenemos que identificar todos los problemas y solucionarlos mediante algunos metodos como:
   * Limpieza
   * Estructurado
   * Enriquecimiento

 - `Load` Una vez transformados debemos insertarlos en el data warehouse, depende del tipo de solución que se haya escogido.

## Introducción a las tecnologías web ##

Las tecnologías web en principio podemos pensarlas como el internet, pero el internet es mucho más grande, es la red de redes, la forma en la que millones de computadores se conectan entre ellas para transferirse información.

El internet también se compone de otros pedazos como telefonía (voip), mail (pop3, imap), compartir archivos (ftp). El internet es una red que une varias redes públicas, privadas, académicas, de negocios, de gobiernos, etc.

La web específicamente es un espacio de información en el cual varios documentos(y otros recursos web) se pueden acceder a través de URLs y vínculos(links). La comunicación se da a través del protocolo HTTP.

Elementos básicos de la web:

 - `HTML` nos da la estructura de la información. Es un lenguaje para anotar pedazos de información para que el navegador o otros tipos de programa puedan interpretar que tipo de información se encuentra ahí.
 - `CSS` nos permite darle colores, arreglar el texto y añadir diferentes elementos de presentación.
 - `Javascript` nos permite añadir interactividad y cómputo a nuestra web.
 - `JSON` Simplemente es una forma de transmitir datos entre servidores y clientes. Es la forma estándar en las que en la web y las aplicaciones se comunican con los servidores backend.

## Realizar solicitudes HTTP con Python ##

Para poder experimentar con la web necesitamos un método programático para solicitar URLs y obtener HTML

`Requests` Nos permite generar solicitudes a la web dentro de Python y utilizar los diferentes verbos HTTP, normalmente utilizaremos el método **GET** porque vamos a traer datos, **delete** para eliminar datos y **options**

**requests.get('url')** para hacer una solicitud a la web y nos devolverá un objeto response

```
import requests
response = requests.get('http://www.platzi.com')
```

Todas las solicitudes HTTP tienen metadatos para que los diferentes sistemas y computadoras puedan entender de qué va la solicitud

El uso de docstring de la respuesta HTTP saldrá si llamamos a la variable de `response` con un simbolo `?` al final.

```
response?
```

Si se desea ver la librería como está implementada, usamos doble interrogación `??`

```
response??
```

Para ver las funciones que se pueden usar, usamos el siguiente comando

```
print(dir(response))
```

Para validar el código de salida de la respuesta 

```
print(response.status_code)
```

Para desplegar los header de la solicitud en un diccionario

```
print(response.headers)
```

Para visualizar el contenido de tu solicitud

```
print(response.text)
```

## Cómo trabajar con un documento HTML ##

En el caso de Python la librería estándar para manipular los documentos HTML se llama `BeautifulSoup`.

`BeautifulSoup` nos ayuda a organizar gramaticalmente(parsear) el documento HTML para que tengamos una estructura con la cual podamos manejar y extraer información. BeautifulSoup convierte el string de HTML en un **árbol de nodos** para poder manipularlo.

Para manipularlo podemos usar los **selectores CSS** con soup.select()

Para usarlo, necesitamos importarlo con bs4

```
import bs4
soup = bs4.BeautifulSoup(response.text,'html.parser')
```

Con ellos podemos empezar a obtener información

> Título en el head

```
print(soup.title.text)
```

> Selector de css en el head

```
print(soup.select('meta[name=description]'))
```

> Selector que solo apunta al elemento "content"

```
print(soup.select('meta[name=description]'))[0]['content'])
```

> Obtención de links (hay que analizar como están estructuradas inspeccionando la página)

```
courses_link = soup.select('.Card_link')
courses = [course['href'] for course in courses_links]

for course in courses:
   print(course)

```

## Analizando un sitio web para encontrar las directivas a utilizar al hacer un web scrapping ##

Para poder desarrollar scrapers debemos entender los datos semi estructurados dados por el HTML para determinar qué tipo de selectores CSS necesitamos para sacar información.

## Solicitudes a la web mediante Requests ##

Un buen Data engineer utiliza los conceptos de la ingeniería de software para poder desarrollar sus programa. En nuestro caso para poder desarrollar nos apoyaremos de un patrón.

`Page Object Patter` Es un patrón que consiste en esconder los queries especificos que se utilizan para manipular un documento HTML detrás de un objeto que representa la página web.

Si estos queries se añaden directamente al código principal, el código se vuelve frágil y va a depender mucho de la modificación que hagan a la web otras personas y arreglarlo se vuelve muy complicado.

## Implementación de web Scrapper ##

Crear una carpeta con los siguientes archivos

web_scrapper
|----config.yaml
|----common.py
|----main.py
|----news_page_objects.py

En `config.yaml` cargamos las urls a analizar, así como los selectores usados para los queries.

> vi config.yaml

```
news_sites:
  eluniversal:
    url: http://www.eluniversal.com.mx
  elpais:
    url: https://elpais.com
```

En `common.py` se ingresa la carga del archivo config.yaml.

> vi common.py

```
import yaml


__config = None

def config():
	global __config
	if not __config:
		with open('config.yaml', mode='r') as f:
			__config =yaml.load(f)
	return __config
```

En `news_page_objects.py` se da de alta los elementos que se encuentran en las páginas y como se detectan, en forma de una clase Modelo

```
import bs4
import requests
from common import config

class HomePage:
	"""Clase del objeto HTML consultado y analizado"""
	def __init__(self, news_site_uid, url):
		"""Constructor donde se consulta a la URL"""
		self._config = config()['news_sites'][news_site_uid]
		self._queries = self._config['queries']
		self._html = None	
		self._visit(url)

	@property
	def articule_links(self):
		link_list = []
		for link in self._select(self._queries['homepage_articule_links']):
			if link and link.has_attr('href'):
				link_list.append(link)
		return set(link['href'] for link in link_list)

	def _select(self, query_string):
		return self._html.select(query_string)

	def _visit(self, url):
		"""Función para obtener el contenido y hacer el parseo"""
		response = requests.get(url)
		response.raise_for_status()
		self._html = bs4.BeautifulSoup(response.text, 'html.parser')
```

En `main.py` se genera la aplicación principal. Se usa la librería `argparse` para hacer un menú precargado.

```
import argparse
import logging
"""Importacion de libreria de logging a nivel INFO"""
logging.basicConfig(level=logging.INFO)

import news_page_objects as news
from common import config


logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
	""""Modulo que genera el scrapper de la pagina seleccionada"""
	host = config()['news_sites'][news_site_uid]['url']
	logging.info('Beggining scrapper for {}'.format(host))
	homepage = news.HomePage(news_site_uid, host)

	for link in homepage.articule_links:
		print(link) 

if __name__ == '__main__':
	"""Funcion principal"""
	parser = argparse.ArgumentParser()
	news_site_choices = list(config()['news_sites'].keys())
	parser.add_argument(
		'news_site',
		help='Site that you want to scrape',
		type=str,
		choices=news_site_choices
		)

	args = parser.parse_args()
	_news_scraper(args.news_site)
```
