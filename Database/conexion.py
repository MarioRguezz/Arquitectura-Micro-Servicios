# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: conexion.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Equipo Alfeluma
# Version: 1.1 Mayo 2018
# Descripción:
#
#   Este archivo se encarga generar una base de datos sqlite en caso de no haberla y si existe, de insertar, seleccionar, borrar
#   entradas de tweets que se evaluaron 
#
#
#
#                                        sv_information.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Insertar, Consultar  | - Utiliza SQLite3      |
#           |     Manejador y       |    Borrar entradas en   |   basado en documento  |
#           |     conexión          |    la base de datos     |                        |
#           |                       |    además verificar que |                        |
#           |                       |    exista.              |                        |
#           +-----------------------+-------------------------+------------------------+
#
#	Ejemplo de uso: Usar un SGBD para consultar ejecución de DBArch la cual está en Database si no se encuentra se genera al correr por primera vez
#
import sqlite3
from os.path import isfile, getsize

def isSqliteExist():
    if isfile("DBArch"):
        return True
    else:
        db = sqlite3.connect('DBArch')
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE Twitter(id INTEGER PRIMARY KEY AUTOINCREMENT, stringSearched TEXT,  tweet TEXT, feeling TEXT)''')
        db.commit()


def storeTweet(Tweet, Feeling):
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    tweet = Tweet
    feeling = Feeling
    cursor.execute('''INSERT INTO Twitter(tweet, feeling) VALUES(?,?)''', (tweet,feeling))


def deleteTweets():
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    tweet = Tweet
    feeling = Feeling
    cursor.execute('''INSERT INTO Twitter(tweet, feeling) VALUES(?,?)''', (tweet,feeling))

