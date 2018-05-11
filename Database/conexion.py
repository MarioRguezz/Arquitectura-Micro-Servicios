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
import time

def isSqliteExist():
    if isfile("DBArch"):
        return True
    else:
        db = sqlite3.connect('DBArch')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE Twitter(id INTEGER PRIMARY KEY, name TEXT,  date TEXT, feeling TEXT)''')
        db.commit()
        db.close()


def storeTweet(Id,Tweet):
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    tweet = Tweet
    cursor.execute('''SELECT * FROM Twitter WHERE id=?''', (Id,))
    db.commit()
    all_rows = cursor.fetchall()
    if len(all_rows) == 0:
        cursor.execute('''INSERT INTO Twitter(Id, name, date) VALUES(?,?,?)''', (Id,tweet,time.strftime("%H:%M:%S")))
        db.commit()
        db.close()
    
def updateTweet(Id,Feeling):
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    cursor.execute('''UPDATE Twitter SET feeling = ? WHERE id = ? ''', (Feeling, Id))
    db.commit()
    db.close()

"""
def selectTweets():
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM Twitter ''')
    db.commit()
    db.close()
"""

def deleteTweets():
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    cursor.execute('''DROP TABLE Twitter''')
    db.commit()    
    db.close() 

def selectTweets():
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM Twitter ''')
    all_rows = cursor.fetchall()
    
    db.close()
    return all_rows

def selectTweet():
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM Twitter ''')
    user1 = cursor.fetchone() #retrieve the first row
    db.close()
    return user1[0]

def selectSentiment(Id):
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    cursor.execute('''SELECT feeling FROM Twitter where id=''' + Id)
    list = cursor.fetchall()
    return list[0][0]
