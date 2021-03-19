from datetime import datetime
from flask import Flask, jsonify, make_response, json
from ct import db
from modelo.Instalacion import Foto
from flask import Blueprint, render_template
import inspect


wsFotos = Blueprint('wsFotos',__name__,static_folder='static', template_folder='templates')

@wsFotos.route('/abm-fotos')
def abm():
    return render_template('fotos/fotos.html')

@wsFotos.route('/getFoto/<id>')
def getInstalacion(id):
    rta = db.session.query(Foto).filter_by(id=id).first()
    if rta != None:
        return jsonify(rta.serializar())
    else:
        return jsonify(None)


@wsFotos.route('/findFotos')
def findFotos():
          
    inicio = datetime.now()

    arr = db.session.query(Foto).all()

    arrSerializado = []
    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    fin = datetime.now()

    distancia = int((fin - inicio).total_seconds() * 1000);
    print(inspect.currentframe().f_code.co_name + "(" + str(len(arrSerializado))+ ") TARDO " + str(distancia) + " MS")

    return jsonify(arrSerializado)

    
@wsFotos.route('/altaFoto/<nombre>/')
def altaFoto(nombre):
          
    nvo = Foto(nombre)
    db.session.add(nvo)
    db.session.commit()

    if nvo != None:
        return jsonify(nvo.serializar())
    else:
        return jsonify(None)