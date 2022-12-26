#./app/app.py
from cmath import exp
from curses import raw
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


@app.route('/')
def home(): 
    return render_template('index.html')

app.run(debug=True)

### Busqueda simple por id como parámetro.
def buscarPorId(id):
    buscado = db.recipes.find_one({'_id':ObjectId(id)})
    if buscado:
        buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
        return jsonify(buscado)
    else:
        return jsonify({'error':'No se ha encontrado, compruebelo'}), 404


### Routa simple para metodos get y post sin parámetro
@app.route('/api/recipes', methods=['GET', 'POST'])
def api_1():
    if request.method == 'GET':
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
       
        
    if request.method == 'POST':
       cocktel = request.json   
       result = db.recipes.insert_one(cocktel)
       id = result.inserted_id
       buscados = db.recipes.find({'_id':ObjectId(id)})
       return (buscarPorId(id))


### Get Put y Delete por parámetro un ID
@app.route('/api/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    if request.method == 'GET':
        return (buscarPorId(id))

    if request.method == 'DELETE':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            db.recipes.delete_one({"_id":ObjectId(id)})
            return jsonify(id)
        else:
            return jsonify({'error':'Not found'}), 404


    if request.method == 'PUT':
        cocktelActulizado = request.json  
        db.recipes.update_one({"_id":ObjectId(id)},{"$set": cocktelActulizado})
        return (buscarPorId(id))
