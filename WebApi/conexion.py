from pymongo import MongoClient
from datetime import datetime
from sanic import Sanic
from sanic.response import json
import asyncio
import motor.motor_asyncio
import json


# establish connex
#conn = MongoClient('localhost', 27017)
#conn = MongoClient()

# create db
#db = conn.baseDeDatos

# create collection
#collection = db.datosNodemcu

# <-------------------------------------------------------- INSERT
# Funciones para insertar datos
# def insertDatos(DataconFecha) :
#    """
#    Una vez que se agrego fecha y hora en la NBDataconFecha recibida por POST
#    agregamos el documento "registro"  en la base de datos.
#    """
#    insertData = collection.insert(DataconFecha)


async def insertarDatos(dataWDate):
    DB = motor.motor_asyncio.AsyncIOMotorClient(
        '127.0.0.1',
        27017,
        io_loop=asyncio.get_event_loop()
    )['sensores']
    Doc = DB['JsonData']
    insertData = await Doc.insert_one(dataWDate)


# def showData() :
# return [ a for a in collection.find()]
#    return collection.find()

# def showD() :
#   return [ a for a in collection.find()]
