# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: sv_sentiment.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Equipo Alfeluma
# Version: 1.1 Mayo 2018
# Descripción:
#
#   Este archivo define el rol de un servicio. Su función general es porporcionar en un objeto JSON
#   información detallada acerca de una pelicula o una serie en particular haciendo uso del API proporcionada
#   por IMDb ('https://www.imdb.com/').
#
#
#
#                                        sv_information.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un JSON que  | - Utiliza el API de    |
#           |    Procesador de      |    contenga información |   IMDb.                |
#           |     comentarios       |    detallada de pelí-   | - Devuelve un JSON con |
#           |       de IMDb         |    culas o series en    |   datos de la serie o  |
#           |                       |    particular.          |   pelicula en cuestión.|
#           +-----------------------+-------------------------+------------------------+
#
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8084/api/v1/information?t=matrix
#
import os
from flask import Flask, abort, render_template, request
import urllib, json
import twitter
import requests
import json
import pymongo
from pymongo import MongoClient
import sys
sys.path.insert(0, '../Database')
import conexion

app = Flask(__name__)


@app.route("/api/v1/tweets")
def tweets():
    """
    Este método obtiene información acerca de una película o serie
    específica.
    :return: JSON con la información de la película o serie
    """
    # Se lee el parámetro 't' que contiene el título de la película o serie que se va a consultar
    title = request.args.get("t")
    api = twitter.Api(consumer_key='BUfe9SBJHUYCfBa8Fax14wmqn',
                      consumer_secret='JYS7Cz1j5tfkZw7L44JcXzzgzt3cAkKn5LNl1jBIf4JnCCA03S',
                      access_token_key='174333272-muKrJ9mlEfRwUwzoK5BKz1IrwwrqyIrnVj8LqZbO',
                      access_token_secret='wPvxXEuBkI7KVJyLdJMvh0woD87gaElNuwDde7qlOslFo')
    conexion.isSqliteExist()
    search = api.GetSearch(title, count=50)
    tweets = []
    for tweet in search:
        tweets.append(tweet.text)
        conexion.storeTweet(tweet.id,tweet.text)
    print json.dumps({"tweets":tweets})
    
    for tweet in conexion.selectTweets():
        print tweet
    
    sentiments = {}

    
    for tweet in search:
        r = requests.post("http://text-processing.com/api/sentiment/", data = {'text' : tweet.text})
        response = json.loads(r.text)
        if not response["label"] in sentiments:
            sentiments[response["label"]] = 1
        else:
            sentiments[response["label"]] += 1
    return json.dumps(sentiments), 200


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8085))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
