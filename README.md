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
 * [Introducción a Pandas](#Introducción-a-Pandas)
 * [Estructura de datos Series](#Estructura-de-datos-Series)
 * [Estructura de datos DataFrames](#Estructura-de-datos-DataFrames)
 * [Índices y selección](#Índices-y-selección)
 * [Data wrangling con Pandas](#Data-wrangling-con-Pandas)
 * [¿Cómo trabajar con datos faltantes?](#Cómo-trabajar-con-datos-faltantes)
 * [Enriquecimiento de los datos](#Enriquecimiento-de-los-datos)
 * [Valores duplicados en Jupyter](#Valores-duplicados-en-Jupyter)
 * [Visualización de datos](#Visualización-de-datos)
 * [Automatización del Pipline](#Automatización-del-Pipline)
 * [Cargando datos a SQLite](#Cargando-datos-a-SQLite)
 * [Introducción a los sistemas de datos](#Introducción-a-los-sistemas-de-datos)
 * [¿Por qué usar la nube?](#Por-qué-usar-la-nube)

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
|----config.yaml - Cargamos las urls a analizar, así como los selectores usados para los queries.
|----common.py - se ingresa la carga del archivo config.yaml.
|----main.py - se genera la aplicación principal. Se usa la librería `argparse` para hacer un menú precargado.
|----news_page_objects.py - se da de alta los elementos que se encuentran en las páginas y como se detectan, en forma de una clase Modelo

## Introducción a Pandas ##

Pandas nos otorga diversa facilidades para el `domados de datos`. Nos otorga dos estructura de datos:

 - `Series`: Es un array unidimensional que representa una columna.
 - `DataFrame`: Es un conjunto de series que forman una tabla. Se pueden acceder a través de indices como un etiqueta(label) o pueden ser posicionales es decir 0 o indice 100. También pueden ser rangos o slices

Estas estructuras de datos no son contenedores de datos. En Pandas las utilizamos para transformar y enriquecer nuestros datos, manipularlos, manejar los faltantes, realizar operaciones aritméticas, combinar diferentes dataframes en uno solo para obtener una nueva tabla.

## Estructura de datos Series ##

Series es un vector unidimensional, para poder acceder a esta lista podemos usar posiciones o labels, siendo este último el preferido para manipular las series. Una diferencia importante sobre las listas de Python es que los datos son `homogéneos`, es decir solo podemos tener un tipo de dato por cada Serie.

Las Series se pueden crear a partir de cualquier secuencia(listas, tuplas, arrays de numpy y diccionarios).

En Python tenemos la filosofía del Duck Typing, si se ve como un pato y hace cuac, a ese animal le llamamos pato, si una serie se comporta una lista, se accede como una lista en principio deberíamos llamarla lista, pero esto no es así.

Una mejor aproximación para inicializar Series es utilizar diccionarios.

Debemos entrar a Jupyter

> source activate dataengine

> jupyter notebook

Se inicializa Pandas

> import pandas as pd

Se crea la serie con lista

> series_test = pd.Series([100,200,300])

> series_test

```
0    100
1    200
2    300
dtype: int64

```

También se puede crear como diccionario para que tenga índices

> series_test2 = pd.Series({1999: 48, 2000: 65, 2001:89})

> series_test2

```
1999    48
2000    65
2001    89
dtype: int64
```

## Estructura de datos DataFrames ##

DataFrames son simplemente una tabla donde las filas y las columnas tienen etiquetas, se puede construir de diferentes formas pero siempre debemos considerar que la estructura que necesitamos construir para inicializarla tiene que ser bidimensional. Una matriz y puede ser una lista de listas, lista de tuplas, un diccionario de Python u otro DataFrame.

Si solo tenemos una dimensión a eso no le llamamos DataFrame, le llamamos Serie. Cuando utilizamos un diccionario las llaves se convierten en las llaves de la columna.

Se inicializa Pandas

> import pandas as pd

Se crea el DataFrame como diccionario

> frame_test = pd.DataFrame({1999: [74,30,39],2000: [44,86,23], 2001: [35,46,64]})

> frame_test

```
  1999  2000  2001
0 74	44	35
1	30	86	46
2	39	23	64
```

También se puede crear con lista de listas.

> frame_test2 = pd.DataFrame([[74,30,39],[44,86,23],[35,46,64]], columns = [1999,2000,2001])

> frame_test2

```
  1999  2000  2001
0 74	44	35
1	30	86	46
2	39	23	64
```

## Índices y selección ##

Existen muchas formas de manipular los DataFrames y de seleccionar los elementos que queremos transformar.

```
Dictionary like:
df[`col1`] #Regresa un dataserie
df[['col1', 'col3']] #Regresa un dataframe

Numpy like:
# iloc = index location
df.iloc[:] #fila
df.iloc[:,:] #fila y columna

Label based:
# loc = location
df.loc[:] # fila
df.loc[:,:] #fila y columna

```

Para leer datos se usa

> el_universal =  pd.read_csv('carpeta/archivo.csv')

Para solo imprimir un extracto del DataFrame

> el_universal.head() #primeros 5

> el_universal.tail() #ultimos 5

Dictionary like

> el_universal['title'] #Devuelve una series

> el_universal[['title','url']] #Devuelve un DataFrame

Numpy like (excluye último valor de la selección)

> el_universal.iloc[10:15] #Devuelve los registros de la 10 a la 15

> el_universal.iloc[13]['title'] #Devuelve el título del registro 13

> el_universal.iloc[:6,0] #Primera columna de los primeros 6 registros

Label based (incluye último valor de la selección)

> el_universal.loc[: , 'body':'title'] #Body y title de todos los registros

## Data wrangling con Pandas ##

Data wrangling es una de las actividades más importantes de todos los profesionales de datos. Simplemente es limpiar, transformar y enriquecer el dataset para objetivos posteriores.

Pandas es una de las herramientas más poderosas para realizar este ““domado”” de datos. Recordemos que Pandas trae muchas de sus abstracciones del lenguaje R, pero nos otorga lo mejor de ambos mundos, por eso es tan popular.

Nos permite:

 - Generar transformaciones con gran facilidad.
 - Trabajar rápidamente con datasets grandes
 - Detectar y reemplazar faltantes
 - Agrupar y resumir nuestros datos
 - Visualizar nuestros resultados.

En el wrapngling podemos hacer labores como:

 - Añadir campos con un valor estático

```
el_universal['newspaper_uid'] = 'el_universal'
el_universal.head()
```

 - Añadir campos a partir de otros campos

 ```
 #Obtener host
 from urllib.parse import urlparse
 el_universal['host'] = el_universal['url'].apply(lambda url: urlparse(url).netloc)
 el_universal.head()
 ```

 - Contar registros con valores similares

 > el_universal['host'].value_counts()

 ```
 www.eluniversal.com.mx         87
 www.viveusa.mx                  9
 www.elbotiquin.mx               8
 sanluis.eluniversal.com.mx      5
 oaxaca.eluniversal.com.mx       5
 www.eluniversalqueretaro.mx     5
 www.elgrafico.mx                5
 de10.com.mx                     4
 www.unionjalisco.mx             4
 www.unioncdmx.mx                2
 www.unionpuebla.mx              2
 www.unionedomex.mx              2
 www.unionyucatan.mx             2
 www.unionguanajuato.mx          1
 www.clubeluniversal.mx          1
 ```

## ¿Cómo trabajar con datos faltantes? ##

Los datos faltantes representan un verdadero problema sobre todo cuando estamos realizando agregaciones. Imagina que tenemos datos faltantes y los llenamos con 0, pero eso haría que la distribución de datos se modificaría radicalmente. Podemos eliminar los registros, pero la fuerza de nuestras conclusiones se debilita.

 Pandas nos otorga varias funcionalidades para identificarlas y para trabajar con ellas. Existe el concepto que se llama NaN, cuando existe un dato faltante simplemente se rellena con un NaN y en ese momento podemos preguntar cuáles son los datos faltantes con .isna().

 notna() para preguntar dónde hay datos completos.
 dropna() para eliminar el registro.

 Para reemplazar:
 fillna() donde le damos un dato centinela
 ffill() donde utiliza el último valor.

 - Rellenado de nulos
```
#Primero obtiene los números de registro con datos faltantes
missing_title_mask = el_universal['title'].isna()
#Extrae la última parte de la URL
missing_titles = (el_universal[missing_title_mask]['url']
                  .str.extract(r'(?P<missing_titles>[^/]+)$')
                  .applymap(lambda title: title.split('-'))
                  .applymap(lambda title_word_list: ' '.join(title_word_list)))
#Añade títulos faltantes
el_universal.loc[missing_title_mask, 'title'] =  missing_titles.loc[:,'missing_titles']

```

 - Generación de ID's
```
# Añade UID a las filas las cuales las genera hexadecimalmente
import hashlib
uids = (el_universal
        .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
        .apply(lambda hash_object: hash_object.hexdigest())
        )
el_universal['uid'] = uids
#Asigna uids como index
el_universal.set_index('uid', inplace=True)
el_universal
```
 - Depurado de saltos de línea

 ```
 stripped_body = (el_universal
                  .apply(lambda row: row['body'], axis=1)
                  .apply(lambda body: list(body))
                  .apply(lambda letters: list(map(lambda letter: letter.replace('\n',''), letters)))
                  .apply(lambda letters: ''.join(letters))
                 )
el_universal['body'] = stripped_body
 el_universal
 ```

## Enriquecimiento de los datos ##
 Podemos enriquecer nuestra tabla con información adicional, un poco de información numérica para realizar análisis posterior.

 Usaremos `nltk` es una librería dentro del stack de Ciencia de Datos de Python que nos va a permitir tokenizar, separar palabras dentro del título y nos permitirá contar la frecuencia de cuántas palabras existen en nuestro título y body

Debemos importar las siguientes Librerías
```
import nltk
from nltk.corpus import stopwords
```

Para la primera vez de ejecución, debemos descargar las siguientes librerías

> nltk.download('punkt')
> nltk.download('stopwords')


Se declara que se tokenizarán palabras en español

> stop_words = set(stopwords.words('spanish'))

Esta sería la función de tokenizar


```def tokenize_columns(df, column_name):
    return (df
           .dropna()
           .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
           .apply(lambda tokens: list(filter(lambda token: token.isalpha(),tokens)))
           .apply(lambda tokens: list(map(lambda token: token.lower(),tokens)))
           .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
        .apply(lambda valid_word_list: len(valid_word_list))
           )
```

Esta se puede usar para toknizar rl nombre y el título

> el_universal['n_tokens_title'] = tokenize_columns(el_universal,'title')
> el_universal['n_tokens_body'] = tokenize_columns(el_universal,'body')

## Valores duplicados en Jupyter ##

Estos valores duplicados es importantes identificarlos y removerlos de nuestro datasets para que esos valores no generen un peso no justificado dentro del análisis a realizar dentro de nuestro Pipelines.

Pandas nos otorga la función drop_duplicates para eliminar estos valores duplicados.

```
el_universal.drop_duplicates(subset=['title'],keep='first', inplace=True)
el_universal
```

## Visualización de datos ##

Idealmente se debe trabajar con más de un datarame para este módulo

```
clean_eluniversal = pd.read_csv('Data_Wrangling/eluniversal_2019_04_21_cleaned_articles.csv')
clean_elpais = pd.read_csv('Data_Wrangling/elpais_2019_04_21_cleaned_articles.csv')
```

La función `describe()` explica los estadísticos de un DataFrame

> clean_eluniversal.describe()

```
n_tokens_title	n_tokens_body
count	128.000000	128.000000
mean	5.351562	236.492188
std	1.872258	213.998234
min	1.000000	9.000000
25%	4.000000	111.000000
50%	5.000000	172.000000
75%	7.000000	275.500000
max	9.000000	1318.000000
```

Graficamos con puntos con la función `plot(style=.)`

> clean_elpais['n_tokens_title'].plot(style='k.') #K= negro. EL punto es que se hace la gráfica de puntos

> clean_eluniversal['n_tokens_title'].plot(style='r.') #r= rojo. EL punto es que se hace la gráfica de puntos

Se usa `pd.concat` para unir dos DataFrames

> all_newspapers = pd.concat([clean_eluniversal, clean_elpais])

Para generar una tabla con agrupaciones sobre un campo específico, se usa `groupby`

> grouped = all_newspapers.groupby('newspaper_uid')

Para hacer histogramas, se usa `hist()`

> grouped.hist()

Para generar una tabla con valores estadísticos agupados, se usa `agg`

> grouped['n_tokens_body'].agg(['min','mean','max'])

La función `plot` sin argumentos genera una gráfica de líneas

> grouped.plot()

## Introducción a los sistemas de datos ##

Los sistemas de datos vienen en muchos sabores y colores, SQL, NoSQL, especializados en procesamiento en bloque, chorro y streaming. Este tipo de sistema nos permite realizar queries sofisticadas y compartir nuestro trabajo con otros miembros del equipo.

Procesamiento de bloque: Estamos hablando de datos históricos, qué sucedió ayer, en el trimestre pasado, cuáles fueron las ventas del año anterior o de los últimos cinco años. Nos permite realizar el procesamiento de manera eficiente.

Procesamiento en chorro: Significa que estamos procesando los datos conforme van llegando, las transformaciones se realizan en tiempo real, Este tipo de sistema nos sirven para cuando queremos realizar decisiones en donde la importancia del tiempo es fundamental.

El criterio principal a tener en cuenta: El tiempo que tienes. Si bien los sistemas open source son gratis, para poderlos implementar necesitas tener conocimientos de cloud, debes poder saber trabajar y mantener máquinas.

SQL vs NoSQL

La discusión más relevante en el mundo de las aplicaciones web y móvil, donde dependiendo de la aplicación, la decisión puede ser fundamental para el crecimiento de la app.
La verdad es que para los profesionales de los datos, especialmente los profesionales de los datos. Es necesario saber ambos.

## Cargando datos a SQLite ##

Para ello, hay que instalar `sqlarchemy`

> conda install sqlalchemy

Se debe tener una clase de motor de base de DATOS

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///newspaper.db')

Session = sessionmaker(bind=Engine)

Base = declarative_base()
```

Y este manejará una clase con el modelado de la tabla

```
from sqlalchemy import Column, String, Integer

from load_sql import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(String, primary_key=True)
    body = Column(String)
    host = Column(String)
    title = Column(String)
    newspaper_uid = Column(String)
    n_tokens_body = Column(Integer)
    n_tokens_title = Column(Integer)
    url = Column(String, unique=True)

    def __init__(self, uid,body,host,newspaper_uid, n_tokens_body,n_tokens_title,title,url):
        self.id= uid
        self.body = body
        self.host = host
        self.newspaper_uid = newspaper_uid
        self.title = title
        self.n_tokens_body = n_tokens_body
        self.n_tokens_title = n_tokens_title
        self.url = url
```

Con ello, en una aplicación main se hace la carga

```
def main(filename):
    Base.metadata.create_all(Engine)
    session = Session()
    articles = pd.read_csv(filename)

    for index, row in articles.iterrows():
        logger.info('Loading article uid {} into DB'.format(row['uid']))
        article = Article(row['uid'],
                        row['body'],
                        row['host'],
                        row['newspaper_uid'],
                        row['n_tokens_body'],
                        row['n_tokens_title'],
                        row['title'],
                        row['url'])
        session.add(article)
    session.commit()
    session.close()
```

## Automatización del Pipline ##

Se hará el ETL en una sola función.

```
def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info("Starting extract process")
    for news_site_uid in news_sites_uids:
        subprocess.run(['python','main.py',news_site_uid], cwd='../Web_Scrapper')
        subprocess.run(['find','.','-name','{}*'.format(news_site_uid),
                        '-exec', 'mv', '{}', '../Data_Wrangling/{}.csv'.format(news_site_uid),
                        ';'], cwd='../Web_Scrapper')

def _transform():
    logger.info("Starting transform process")
    for news_site_uid in news_sites_uids:
        subprocess.run(['python','newspaper_receipe.py','{}.csv'.format(news_site_uid)], cwd='../Data_Wrangling')
        subprocess.run(['find','.','-name','{}*cleaned*'.format(news_site_uid),
                        '-exec', 'mv', '{}', '../Load_Database/{}.csv'.format(news_site_uid),
                        ';'], cwd='../Data_Wrangling')
        subprocess.run(['find','.','-name','{}*'.format(news_site_uid),
                        '-exec', 'rm', '{}',';'], cwd='../Data_Wrangling')

def _load():
    logger.info("Starting loading process")
    for news_site_uid in news_sites_uids:
        subprocess.run(['python','main.py','{}.csv'.format(news_site_uid)], cwd='../Load_Database')
        subprocess.run(['find','.','-name','{}*'.format(news_site_uid),
                        '-exec', 'rm', '{}',';'], cwd='../Load_Database')
```

## ¿Por qué usar la nube? ##
La nube nos da un poder de cómputo casi inimaginable, nos permite procesar terabytes de datos en segundos. La nube se puede usar en dos grandes ocasiones. Cuando los datos ya no caben en tu computadora loca o cuando el tiempo de procesamiento esta siendo muy extenso, es en ese momento donde deberías usar la nube.

Si estas en un entorno de producción, si estas trabajando en una empresa y los datos de esa empresa ya viven en la nube, lo lógico es realizar el trabajo en la nube. Automatizar los scripts en ese mismo ambiente.

Diversas nubes ya ofrecen paquetes completos para el ciclo de datos, como Google Cloud:

 * Dataflow
 * Pub/Sub
 * Cloud Storage
 * Datalab
 * BigQuery
 * Dataproc
 * Firestore
