# Servicios
En esta carpeta se define el servicio utilizado en la tarea 2
dentro del Sistema de Procesamiento de Comentarios (SPC).
La especificación del servicio del Procesador de Comentarios de IMDb,
servicio de procesador de sentimientos y el servicio de procesador
de tweets se realizó utilizando blueprint de Apiary.
La especificación es la siguiente:

## Procesador de Comentarios de IMDb
  
FORMAT: 1A
HOST: http://localhost:8084

## Information Service [/api/v1/information{?t}]

+ Parameters
    + t - Corresponde al título de la película o serie de Netflix.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "Title": "Some text",
            "Year": "Some text", 
            "Rated": "Some text",
            "Released": "Some text",
            "Runtime": "Some text",
            "Genre": "Some text",
            "Director": "Some text",
            "Writer": "Some text",
            "Actors": "Some text",
            "Plot": "Some text",
            "Language": "Some text",
            "Country": "Some text",
            "Awards": "Some text.",
            "Poster": "Some text",
            "Metascore": "Some text",
            "imdbRating": "Some text",
            "imdbVotes": "Some text",
            "imdbID": "Some text",
            "Type": "Some text",
            "totalSeasons": "Some text",
            "Response": "Some text"
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Abrir el navegador
2. Ingresar a https://uaz.cloud.tyk.io/content/api/v1/information?t=Stranger+Things



## Procesador Sentimientos
  
FORMAT: 1A  
HOST: http://localhost:8086

## Análisis de sentimientos [/api/v1/sentiment]

+ Parameters
    + t - Corresponde al comentario de twitter a procesar 

### Análisis de sentimientos [POST]

+ Response 200 (application/json)

        { 
            "neg" : "Some text",
            "pos" : "Some text",
            "neutral" : "Some text"
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Abrir el navegador
2. Ingresar a http://localhost:8086/api/v1/sentiment?text=dont+like+simpsons


## Procesador Twitter

FORMAT: 1A
HOST: http://localhost:8085

## Twitter comentario [/api/v1/tweets/get{?t}]

+ Parameters
    + t - Corresponde a la cadena de texto para buscar tweets relacionados

### Get twitter comment [GET]

+ Response 200 (application/json)

        {
            "id" : "Some text",
            "text" : "Some text",
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso:
1. Abrir el navegador
2. Ingresar a http://localhost:8085//api/v1/tweets?t=Stranger+Things

## Twitter historial [/api/v1/api/v1/tweets_db]

### Get twitter comment [GET]

+ Response 200 (application/json)

        {
            "id" : "Some text",
            "tweets" : "Some text",
            "date" : "Some text",
            "feeling" : "Some text"
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso:
1. Abrir el navegador
2. Ingresar a http://localhost:8085/api/v1/api/v1/tweets_db


## Borrar tweets [/api/v1/remove_tweets_db]

### Delete tweets saved [POST]

+ Response 200 (application/json)

        {
            "data" : true
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso:
1. Abrir el navegador
2. Ingresar a http://localhost:8085//api/v1/remove_tweets_db




