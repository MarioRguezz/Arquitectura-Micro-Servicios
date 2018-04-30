# Servicios
En esta carpeta se define el servicio utilizado en la tarea 2 dentro del Sistema de Procesamiento de Comentarios (SPC). La especificación del servicio del Procesador de Comentarios de IMDb se realizó utilizando blueprint de Apiary.
La especificación es la siguiente:

## Procesador de Comentarios de IMDb
  
FORMAT: 1A  
HOST: https://uaz.cloud.tyk.io/content

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
