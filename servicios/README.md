FORMAT: 1A
HOST: http://polls.apiblueprint.org/

# Servicios
En esta carpeta se define el servicio utilizado en la tarea 2
dentro del Sistema de Procesamiento de Comentarios (SPC).
La especificación del servicio del Procesador de Comentarios de IMDb,
servicio de procesador de sentimientos y el servicio de procesador
de tweets se realizó utilizando blueprint de Apiary.
La especificación es la siguiente:

## Procesador de Comentarios de IMDb

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
1. Ingresar a https://uaz.cloud.tyk.io/content/api/v1/information?t=Stranger+Things



## Procesador Sentimientos

FORMAT: 1A
HOST: http://localhost:8085

## Sentiment Analysis [/api/v1/SentimentAnalysis{?t}]

+ Parameters
+ t - Corresponde al comentario a procesar

### Sentiment Analysis [GET]

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
1. Ingresar a http://localhost:8085/api/v1/SentimentAnalysis/get




## Procesador Twitter

FORMAT: 1A
HOST: http://localhost:8086

## Twitter comentario [/api/v1/SentimentAnalysis/get]


+ Parameters
+ t - Corresponde a la cadena de texto para buscar tweets relacionados

### Get twitter comment [GET]

+ Response 200 (application/json)

{
"id" : "Some text",
"tweets" : "Some text",
}

+ Response 400 (text)

{
"title": "Bad Request"
"message": "The browser (or proxy) sent a request that this server could not understand."
}

Ejemplo de uso:
1. Abrir el navegador
1. Ingresar a http://localhost:8086/api/v1/tweets/set?t=Stranger+Things



## Twitter historial [/api/v1/SentimentAnalysis/get]


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
1. Ingresar a http://localhost:8086/api/v1/tweets/set?t=Stranger+Things






## Borrar tweets [/api/v1/SentimentAnalysis/get]


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
1. Ingresar a http://localhost:8086/api/v1/tweets/set?t=Stranger+Things
