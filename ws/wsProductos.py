from flask import Flask, jsonify, make_response, json
from ct import db, Controller
from modelo.Producto import Producto
from flask import Blueprint, render_template

wsProductos = Blueprint('wsProductos',__name__,static_folder='static', template_folder='templates')


@wsProductos.route('/productos')
def ventanaProductos():
    return render_template('productos/productos.html')

@wsProductos.route('/getProducto/<id>')
def getProducto(id):
    rta = db.session.query(Producto).filter_by(id=id).first()
    if rta != None:
        return jsonify(rta.serializar())
    else:
        return jsonify(None)


@wsProductos.route('/findProductos')
def findProductos():
    arr = db.session.query(Producto).all()

    arrSerializado = []
    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    return jsonify(arrSerializado)

    
@wsProductos.route('/saveProducto/<nombre>/<precio>')
def saveProducto(nombre, precio):
          
    nvo = Producto(nombre,precio)
    db.session.add(nvo)
    db.session.commit()

    if nvo != None:
        return jsonify(nvo.serializar())
    else:
        return jsonify(None)