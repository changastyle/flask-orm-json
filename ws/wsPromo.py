from flask import Flask, jsonify, make_response, json
from ct import db, Controller
from modelo.Promo import Promo
from ws.wsInstalaciones import wsInstalaciones
from flask import Blueprint, render_template 
from flask import request


wsPromo = Blueprint('wsPromo',__name__,static_folder='static', template_folder='templates')

#AGREGAR AL APP.PY:
#app.register_blueprint(wsPromo,url_prefix='')


@wsPromo.route('/promos')
def ventanaPromos():
    return render_template('promo/promo.html')

@wsPromo.route('/getPromo/<id>')
def getPromo(id):
    rta = db.session.query(Promo).filter_by(id=id).first()
    if rta != None:
        return jsonify(rta.serializar())
    else:
        return jsonify(None)


@wsPromo.route('/findPromos')
def findPromos():
    arr = db.session.query(Promo).all()

    arrSerializado = []
    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    return jsonify(arrSerializado)


@wsPromo.route('/findPromosByInstalacion')
def findPromosByInstalacion():
    
    arrSerializado = []
    arr = []

    url = request.url 
    instalacionDB = Controller.getInstalacionSegunURL(url)

    if instalacionDB != None:
        # try:
        arr = db.session.query(Promo).filter(Promo.fkInstalacion == instalacionDB.id).all()

        for itemLoop in arr:
            arrSerializado.append(itemLoop.serializar()) 
        # except Exception as e: 
        #     print(e)
        #     db.session.rollback()
        

    return jsonify(arrSerializado)


@wsPromo.route('/altaPromo/<nombre>/<precio>')
def altaPromo(nombre, precio):

    nvo = Promo(nombre,precio)
    db.session.add(nvo)
    db.session.commit()

    if nvo != None:
        return jsonify(nvo.serializar())
    else:
        return jsonify(None)




@wsPromo.route('/rmPromo/<id>')
def rmPromo(id):
    pass
    # promoDB = 
    # if promoDB != None:
    #       promoDB.activo = False

    #       db.session.add(promoDB)
    #       db.session.commit()


    #       if promoDB != None:
    #             return jsonify(promoDB.serializar())
    #       else:
    #             return jsonify(None)
@wsPromo.route('/activarPromo/<id>')
def activarPromo(id):

    promoDB = getPromo(id)
    if promoDB != None:
        promoDB.activo = False;

    db.session.add(promoDB)
    db.session.commit()

    if promoDB != None:
        return jsonify(promoDB.serializar())
    else:
        return jsonify(None)

@wsPromo.route('/setPromo/<id>/<clave>/<valor>')
def setPromo(id, clave ,valor):
    pass
    # if id != -1:
    #     promoDB = getPromo(id)

    #     if promoDB != None and clave != None and valor != None:
    #         promoDB.getAttr(clave) = valor

    #         db.session.add(promoDB)
    #         db.session.commit()

    #         if promoDB != None:
    #             return jsonify(promoDB.serializar())
    #         else:
    #             return jsonify(None)
