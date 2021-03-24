from flask import Flask, jsonify, make_response, json
from ct import db, controller
from modelo.Rol import Rol
from flask import Blueprint, render_template

wsRol = Blueprint('wsRol',__name__,static_folder='static', template_folder='templates')

#AGREGAR AL APP.PY:
#app.register_blueprint(wsRol,url_prefix='')


@wsRol.route('/rols')
def ventanaRols():
    return render_template('rol/rol.html')

@wsRol.route('/getRol/<id>')
def getRol(id):
    rta = getRolDB(id)
    if rta != None:
        return jsonify(rta.serializar())
    else:
        return jsonify(None)

def getRolDB(id):
    rta = db.session.query(Rol).filter_by(id=id).first()
    if rta != None:
        return rta.serializar()
    else:
        return None

def getRolDefault():
    rta = db.session.query(Rol).filter_by(id=1).first()
    return rta

@wsRol.route('/findRols')
def findRols():
    arr = db.session.query(Rol).all()

    arrSerializado = []
    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    return jsonify(arrSerializado)


@wsRol.route('/altaRol/<nombre>/<precio>')
def altaRol(nombre, precio):

    nvo = Rol(nombre,precio)
    db.session.add(nvo)
    db.session.commit()

    if nvo != None:
        return jsonify(nvo.serializar())
    else:
        return jsonify(None)




@wsRol.route('/rmRol/<id>')
def rmRol(id):

    rolDB = getRol(id)
    if rolDB != None:
          rolDB.activo = False

          db.session.add(rolDB)
          db.session.commit()


          if rolDB != None:
                return jsonify(rolDB.serializar())
          else:
                return jsonify(None)
@wsRol.route('/activarRol/<id>')
def activarRol(id):

    rolDB = getRol(id)
    if rolDB != None:
        rolDB.activo = False;

    db.session.add(rolDB)
    db.session.commit()

    if rolDB != None:
        return jsonify(rolDB.serializar())
    else:
        return jsonify(None)

