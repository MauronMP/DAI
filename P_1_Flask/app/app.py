#./app/app.py
from flask import Flask, render_template, url_for
from flask import Flask
import os 
app = Flask(__name__)
          
def fibonacci(n):
    if(n>1):
        return fibonacci(n-1) + fibonacci(n-2)
    elif(n==1):
        return 1
    elif (n==0):
        return 0
    else:
        print("Escribe un numero positivo")


@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route("/fibonacci/<int:param>")
def Ejer_1(param):
    calculo = fibonacci(param)
    return f'<h1 style=text-align:center>Valor de {param} con fibonacci es: {calculo}</h1>'

#Ejercicio 2
@app.route('/ejer2')
def ejercicio_2(): 
    return render_template('index.html')

#Ejercicio 3
@app.errorhandler(404)
def page_not_found(error):
    return f'<h1 style=text-align:center>Error 404, esta url no existe, prueba otra</h1>'