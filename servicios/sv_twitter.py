# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: sv_twitter.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Equipo Alfeluma
# Version: 1.1 Mayo 2018
# Descripción:
#
#   Este archivo define el rol de un servicio. Su función general es porporcionar en un objeto JSON de los tweets, así como borrarlos
#   y consultarlos mediante la API proporcionada por 
#   evauación de los tweets guardados para saber si son positivos, negativos o neutros mediante la  API proporcionada
#   ('https://developer.twitter.com/').
#
#
#
#                                        sv_twitter.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un JSON que  | - Utiliza el API de    |
#           |    Procesador         |    contenga tweets      |   twitter.     |
#           |    twitter            |  - Guardar los tweets   | - Devuelve un JSON con |
#           |                       |  - Borrar los tweets de |  tweets o guarda tweets|
#           |                       |    base de datos        | o borra tweets de la bd|
#           +-----------------------+-------------------------+------------------------+
#
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8085/api/v1/tweets?text=tweet  para adquirir los tweets
#
import os
from flask import Flask, abort, render_template, request
import urllib, json
import twitter
import requests
import json
import sys
sys.path.insert(0, 'Database')
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
        tweets.append({"id":tweet.id,"text":tweet.text})
        conexion.storeTweet(tweet.id,tweet.text)
    return json.dumps({"tweets":tweets})

@app.route("/api/v1/tweets_db")
def tweets_db():
    """
    Este método obtiene información acerca de una película o serie
    específica.
    :return: JSON con la información de la película o serie
    """
    # Se lee el parámetro 't' que contiene el título de la película o serie que se va a consultar
    tweets_db = conexion.selectTweets()
    tweets = []
    for tweet in tweets_db:
        tweets.append({"id":tweet[0],"text":tweet[1],"date":tweet[2],"feeling":tweet[3]})
    return json.dumps({"tweets":tweets})


@app.route("/api/v1/remove_tweets_db")
def remove_tweets_db():
    """
    Este método obtiene información acerca de una película o serie
    específica.
    :return: JSON con la información de la película o serie
    """
    # Se lee el parámetro 't' que contiene el título de la película o serie que se va a consultar
    conexion.deleteTweets()
    tweets_db = conexion.selectTweets()
    tweets = []
    for tweet in tweets_db:
        tweets.append({"id":tweet[0],"text":tweet[1],"date":tweet[2],"feeling":tweet[3]})
    print tweets
    return json.dumps({"tweets":tweets})


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8085))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
