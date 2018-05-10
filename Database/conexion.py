#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
from os.path import isfile, getsize

def isSqliteExist():
    if isfile("DBArch"):
        return True
    else:
        db = sqlite3.connect('DBArch')
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE Twitter(id INTEGER PRIMARY KEY AUTOINCREMENT, tweet TEXT, feeling TEXT)''')
        db.commit()



def storeTweet(Tweet, Feeling):
    db = sqlite3.connect('DBArch')
    cursor = db.cursor()
    tweet = Tweet
    feeling = Feeling
    cursor.execute('''INSERT INTO Twitter(tweet, feeling) VALUES(?,?)''', (tweet,feeling))





def isSqliteExist():
    if isfile("DBArch"):
        return True
    else:
        db = sqlite3.connect('DBArch')
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE Twitter(id INTEGER PRIMARY KEY, tweet TEXT, feeling TEXT)''')
        db.commit()


