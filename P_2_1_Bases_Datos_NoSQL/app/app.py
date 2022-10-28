#./app/app.py

from bson.json_util import dumps
from pymongo import MongoClient

from flask import Flask, Response

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find() # devuelve un cursor(*), no una lista ni un iterador
    resJson = formatoJson(recetas)
    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')


@app.route('/recetas_de/<cadenaBuscar>')
def ejer1(cadenaBuscar):
    
    # Encontramos los documentos de la coleccion "recipes"
    recetas =  db.recipes.find({ "name": { "$regex": cadenaBuscar, "$options": "si"} })
    resJson = formatoJson(recetas)
    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')


@app.route('/recetas_con/<cadenaBuscar>')
def ejer2(cadenaBuscar):
    
    # Encontramos los documentos de la coleccion "recipes"
    recetas =  db.recipes.find( {"$or": [ {"ingredients.name": {"$regex": "(?i)"+cadenaBuscar}},{"instructions": {"$regex": "(?i)"+cadenaBuscar}}]})
    resJson = formatoJson(recetas)
    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_compuestas_de/<int:cantidad>/ingredientes')
def ejer3(cantidad):
    
    # Encontramos los documentos de la coleccion "recipes"
    recetas =  db.recipes.find({ "ingredients": { "$size": cantidad } })
    resJson = formatoJson(recetas)
    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(error):
    return f'<h1 style=text-align:center>Error 404, esta url no existe, prueba otra</h1>'

def formatoJson(recetas):
    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas   
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)
    return resJson
