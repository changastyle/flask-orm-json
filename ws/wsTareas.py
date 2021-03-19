from flask import Flask, jsonify, make_response, json
from ct import db, Serializer
from modelo.Tarea import Tarea
from flask import Blueprint, render_template

wsTareas = Blueprint('wsTareas',__name__,static_folder='static', template_folder='templates')


#@tareas.route('/tareas')
# def ventanaProductos():
#     return render_template('productos/productos.html')

@wsTareas.route('/getTarea/<id>')
def getTarea(id):
    rta = db.session.query(Tarea).filter_by(id=id).first()
    if rta != None:
        return jsonify(rta.serializar())
    else:
        return jsonify(None)


@wsTareas.route('/findTareas')
def findTareasx():
    arr = db.session.query(Tarea).all()

    arrSerializado = []
    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    return jsonify(arrSerializado)

    
# @wsTareas.route('/saveProducto/<nombre>/<precio>')
# def saveProducto(nombre, precio):
          
#     nvo = Producto(nombre,precio)
#     dao.session.add(nvo)
#     dao.session.commit()

#     if nvo != None:
#         return jsonify(nvo.serializar())
#     else:
#         return jsonify(None)