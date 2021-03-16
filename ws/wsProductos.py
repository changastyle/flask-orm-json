from flask import Flask, jsonify, make_response, json
from dao import dao, Serializer
from modelo.Producto import Producto
from flask import Blueprint, render_template

productos = Blueprint('productos',__name__,static_folder='static', template_folder='templates')

@productos.route('/getProducto/<id>')
def getProducto(id):
    rta = dao.session.query(Producto).filter_by(id=id).first()
    if rta != None:
        return jsonify(rta.serialize())
    else:
        return jsonify(None)


@productos.route('/findProductos')
def findProductos():
    arrProductos = dao.session.query(Producto).all()

    return jsonify(Serializer.serializarL(arrProductos))