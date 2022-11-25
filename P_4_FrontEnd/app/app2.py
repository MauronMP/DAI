#./app/app.py
from cmath import exp
from curses import raw
from queue import Empty
from flask import request, jsonify
from bson import ObjectId
from pymongo import MongoClient
from bson.json_util import dumps
from flask import Flask, Response, render_template


app = Flask(__name__)


# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)


# Base de datos
db = client.cockteles



### Busqueda simple por id como parámetro.
def buscarPorId(id):
    buscado = db.recipes.find_one({'_id':ObjectId(id)})
    if buscado:
        buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
        return jsonify(buscado)
    else:
        return jsonify({'error':'No se ha encontrado, compruebelo'}), 404


### Routa simple para metodos get sin parámetro y por nombre
@app.route('/api2/recipes', methods=['GET'])
def api2_get():
    cadenaBuscar = request.args.get('con','')
    
    if(cadenaBuscar != ''):        
        buscados =  db.recipes.find( {"$or": [ {"ingredients.name": {"$regex": "(?i)"+cadenaBuscar}},{"instructions": {"$regex": "(?i)"+cadenaBuscar}}]})
    else:    
        buscados =  db.recipes.find()
        
    if(buscados):    
        lista = []
        for recipe in buscados:
            recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
            lista.append(recipe)
        return jsonify(lista)
    else:
        return jsonify({'error':'No se ha encontrado, compruebelo'}), 404
    
### Routa simple para metodo post sin parámetro
@app.route('/api2/recipes', methods=['POST'])
def api2_post():     
    cocktel = request.json   
    result = db.recipes.insert_one(cocktel)
    id = result.inserted_id
    buscados = db.recipes.find({'_id':ObjectId(id)})
    return (buscarPorId(id))


#Get con id
@app.route('/api2/recipes/<id>', methods=['GET'])
def api_2_getId(id):
    if request.method == 'GET':
        return (buscarPorId(id))

#Put con id
@app.route('/api2/recipes/<id>', methods=['PUT'])
def api_2_putId(id):
    if request.method == 'PUT':
        cocktelActulizado = request.json  
        db.recipes.update_one({"_id":ObjectId(id)},{"$set": cocktelActulizado})
        return (buscarPorId(id))

#Delete por id
@app.route('/api2/recipes/<id>', methods=['DELETE'])
def api_2_deleteId(id):
    buscado = db.recipes.find_one({'_id':ObjectId(id)})
    if buscado:
        buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
        db.recipes.delete_one({"_id":ObjectId(id)})
        return jsonify(id)
    else:
        return jsonify({'error':'Not found'}), 404

@app.route('/')
def home(): 
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
