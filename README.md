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

##Instalación ##

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

