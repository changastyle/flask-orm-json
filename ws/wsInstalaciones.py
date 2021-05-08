from datetime import datetime
from flask import Flask, jsonify, make_response
import json
from ct import db
from modelo.Instalacion import Instalacion
from flask import Blueprint, render_template
import inspect
from flask import request
from sqlalchemy import and_, or_, not_
from ct import Controller
import flask
wsInstalaciones = Blueprint('wsInstalaciones',__name__,static_folder='static', template_folder='templates')


@wsInstalaciones.route('/abm-instalaciones')
def abm():
    return render_template('instalaciones/instalaciones.html')

@wsInstalaciones.route('/getInstalacion/<id>')
def getInstalacion(id):
    rta = db.session.query(Instalacion).filter_by(id=id).first()
    if rta != None:
        # print("RTA: " + str(type(rta)) + " -" + str(rta))
        # f = open("JSON.txt", "w")
        # f.write(str(rta.serializar()))
        # f.close()
        # return jsonify(rta.as_dict())
        return rta.serializar()
    else:
        return jsonify(None)

@wsInstalaciones.route('/getInstalacionSegunURL/<url>')
def getInstalacionSegunURL(url):
    
    url = Controller.limpiarURL(url , request)

    print("URL RECIBIDA: " + url)

    search = "%" + url + "%"

    print("SEARCH:" + search)

    rta = db.session.query(Instalacion).filter(
        or_(
            Instalacion.urlDominio.like(search),
            Instalacion.urlDominioDos.like(search)
        )
    ).first()
    

    if rta != None:
        if flask.request.method == 'POST' or flask.request.method == 'GET':
            return rta.serializar()
        else:
            pass
    else:
        return jsonify(None)

    return rta


@wsInstalaciones.route('/findInstalaciones')
def findInstalaciones():
          
    inicio = datetime.now()

    arr = db.session.query(Instalacion).all()

    arrSerializado = []
    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    fin = datetime.now()

    distancia = (fin - inicio).total_seconds() * 1000;
    print("TIPO:" + str(type(distancia)))
    print(inspect.currentframe().f_code.co_name + "() TARDO " + str(distancia) + " MS")

    return jsonify(arrSerializado)

    
@wsInstalaciones.route('/altaProducto/<nombre>/')
def altaProducto(nombre):
          
    nvo = Instalacion(nombre)
    db.session.add(nvo)
    db.session.commit()

    if nvo != None:
        return jsonify(nvo.serializar())
    else:
        return jsonify(None)