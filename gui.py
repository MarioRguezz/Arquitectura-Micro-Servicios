# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: gui.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.2 Abril 2017
# Descripción:
#
#   Este archivo define la interfaz gráfica del usuario. Recibe dos parámetros que posteriormente son enviados
#   a servicios que la interfaz utiliza.
#   
#   
#
#                                             gui.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Porporcionar la in-  | - Consume servicios    |
#           |          GUI          |    terfaz gráfica con la|   para proporcionar    |
#           |                       |    que el usuario hará  |   información al       |
#           |                       |    uso del sistema.     |   usuario.             |
#           +-----------------------+-------------------------+------------------------+
#
import os
from flask import Flask, render_template, request
import urllib, json
import requests

app = Flask(__name__)


@app.route("/")
def index():
    # Método que muestra el index del GUI
    return render_template("index.html")


@app.route("/information", methods=['GET'])
def sentiment_analysis():
    # Se obtienen los parámetros que nos permitirán realizar la consulta
    title = request.args.get("t")
    if len(title) is not 0:
        # La siguiente url es para un servicio local
        url_omdb = urllib.urlopen("http://127.0.0.1:8084/api/v1/information?t=" + title)
        # La siguiente url es para un servicio en la nube, pregunta al instructor(a) si el servicio está activo
        # url_omdb = urllib.urlopen("https://uaz.cloud.tyk.io/content/api/v1/information?t=" + title)
        # Se lee la respuesta de OMDB
        json_omdb = url_omdb.read()
        # Se convierte en un JSON la respuesta leída
        omdb = json.loads(json_omdb)
        # Se llena el JSON que se enviará a la interfaz gráfica para mostrársela al usuario
        json_result = {'omdb': omdb}
        # Se regresa el template de la interfaz gráfica predefinido así como los datos que deberá cargar
        return render_template("status.html", result=json_result)
    else:
        return render_template("error-500.html")


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el Sistema de Procesamiento de Comentarios (SPC).
    port = int(os.environ.get('PORT', 8000))
    # Se habilita el modo debug para visualizar errores
    app.debug = True
    # Se ejecuta el GUI con un host definido cómo '0.0.0.0' para que pueda ser accedido desde cualquier IP
    app.run(host='0.0.0.0', port=port)
