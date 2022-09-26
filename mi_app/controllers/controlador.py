from flask import Flask, render_template
from mi_app import app

@app.route('/')
def hola_mundo():
    return 'Hola'

@app.route('/play')
def plantilla_1():
    return render_template('index.html', color='#9fc5f8', numero = 3)

@app.route('/play/<int:numero>')
def plantilla_2(numero):
    return render_template("index.html", color = '#9fc5f8', numero = numero)

@app.route('/play/<int:numero>/<string:color>')
def plantilla_3(color,numero):
    return render_template("index.html", color = color, numero= numero)

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez." ,404
