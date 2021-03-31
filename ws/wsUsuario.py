from flask import Flask, jsonify, make_response, json, session
from ct import controller , db
from modelo.Usuario import Usuario
from modelo import Rol
from ws import wsRol
from ws.wsInstalaciones import wsInstalaciones
from ws.wsInstalaciones import getInstalacion
from ws.wsInstalaciones import getInstalacionSegunURL
from ws.wsRol import getRolDefault
from flask import Blueprint, render_template
from flask import request
from types import SimpleNamespace
from sqlalchemy import and_, or_, not_

wsUsuario = Blueprint('wsUsuario',__name__,static_folder='static', template_folder='templates')

#AGREGAR AL APP.PY:
#app.register_blueprint(wsUsuario,url_prefix='')


nombreVariableSesion = "user"


#|-------- VISTAS: --------|:
@wsUsuario.route('/usuarios')
def ventanaUsuarios():
    return render_template('usuarios/usuarios.html')



#|-------- LOGIN DE USUARIOS: --------|:
@wsUsuario.route('/login/<user>/<passw>')
def login(user , passw):
    rta = None


    print("VOY A LOGEAR A :" + str(user) + " - " + str(passw));

    usuarioDB = getUsuarioByEmailAndPassw(user , passw)

    if usuarioDB != None:
        rta = usuarioDB.serializar()
        session[nombreVariableSesion] = rta

    return jsonify(rta)

@wsUsuario.route('/comprobarUsuarioLogeado/')
def comprobarUsuarioLogeado():
    
    rta = None

    if session != None:
              
        if session != None:
            print("COMPROBANDO USUARIO LOGEADO: " + str(type(session)))
            
            if nombreVariableSesion in session:
                      
                usuarioSesionado =  session[nombreVariableSesion]

                if usuarioSesionado != None:
                    email = usuarioSesionado["email"]
                
                    if email != None:
                              
                        usuarioLogeado = getUsuarioByEmail(email)

                        print("EL USUARIO LOGEADO ES: " + str(email))

                        if usuarioLogeado != None:
                            rta = usuarioLogeado.serializar();
    
    return jsonify(rta)

@wsUsuario.route('/exit/')
def exit():
    
    rta = None

    if session != None:
              
        if session != None:
            
            if nombreVariableSesion in session:
                      
                session[nombreVariableSesion]  = None
                rta = None;
    
    return jsonify(rta)

#|-------- FIND --------|:
@wsUsuario.route('/findUsuarios')
def findUsuariosSerial():
    arr = findUsuarios()
    arrSerializado = []

    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    return jsonify(arrSerializado)

def findUsuarios():
    try:
        arr = db.session.query(Usuario).all()
    except Exception as e: 
        db.session.rollback()
        print(e) 

    return arr




#|-------- GET -------------|         
@wsUsuario.route('/getUsuario/<id>')
def getUsuarioSerial(id):
    rta = getUsuario(id)
    if rta != None:
        return jsonify(rta.serializar())
    else:
        return jsonify(None)
def getUsuario(id):
    rta = db.session.query(Usuario).filter_by(id=id).first()
    return rta

def getUsuarioByEmail(email):
    rta = db.session.query(Usuario).filter_by(email = email).first()

    return rta
def getUsuarioByEmailAndPassw(email , passw):
    
    rta = db.session.query(Usuario).filter(
        and_(
            Usuario.email == email,
            Usuario.passw == passw
        )
    ).first()

    return rta




#|-------- EMPTY --------|:
@wsUsuario.route('/getUsuarioEmpty/')
def getUsuarioEmpty():
          
    url = request.url 
          
    empty = Usuario()
    empty.id = -1
    empty.nombre = "TEST"
    empty.email = "jorgito"
    empty.activo = True
    empty.instalacion = getInstalacionSegunURL(url)
    empty.rol = getRolDefault()

    print("URL REQUEST: " + url)

    if empty != None:
        return jsonify(empty.serializar())
    else:
        return jsonify(None)





#|-------- ALTA --------|:
@wsUsuario.route('/altaUsuario/' , methods=['GET', 'POST'])
def altaUsuario():
          
    data = request.get_json()

    print("data type= " + str(type(data)))
    if json != None:
        for item in data:
            print(item)
    
    # CONVIERTO DE JSON A OBJ RECIBIDO:
    recibido = Usuario(**data)

    # CREO UN OBJETO NVO:
    nvo = Usuario(nombre="nvo")

    # POPULO EL OBJ NUEVO CON EL RECIBIDO:
    nvo.nombre = recibido.nombre
    nvo.email= recibido.email
    nvo.passw=recibido.passw
    nvo.token=recibido.token
    nvo.observaciones=recibido.observaciones
    nvo.fechaAlta=recibido.fechaAlta
    nvo.fechaNacimiento=recibido.fechaNacimiento
    nvo.telefono=recibido.telefono
    nvo.activo=recibido.activo

    # RELACIONES FK:
    nvo.fkRol=recibido.fkRol
    # rolDB = wsRol.getRolDB()
    print("ROL:" + str(recibido.fkRol))
    print("ROL NVO:" + str(nvo.fkRol))
        # self.rol=otro.rol
        # self.fkInstalacion=otro.fkInstalacion
        # self.instalacion=otro.instalacion


    # GUARDO EN DB:
    try:
        db.session.add(nvo)
        db.session.commit()

    except Exception as e: 
        db.session.rollback()
        print(e) 

    if nvo != None:
        return jsonify(nvo.serializar())
    else:
        return jsonify(None)






#|-------- RM --------|:
@wsUsuario.route('/rmUsuario/<id>')
def rmUsuario(id):

    usuarioDB = getUsuario(id)
    if usuarioDB != None:
          usuarioDB.activo = False

          db.session.add(usuarioDB)
          db.session.commit()


          if usuarioDB != None:
                return jsonify(usuarioDB.serializar())
          else:
                return jsonify(None)







#|-------- ACTIVAR --------|:
@wsUsuario.route('/activarUsuario/<id>')
def activarUsuario(id):

    usuarioDB = getUsuario(id)
    if usuarioDB != None:
        usuarioDB.activo = False;

    db.session.add(usuarioDB)
    db.session.commit()

    if usuarioDB != None:
        return jsonify(usuarioDB.serializar())
    else:
        return jsonify(None)







#|-------- SET CLAVE --------|:
# @wsUsuario.route('/setUsuario/<id>/<clave>/<valor>')
# def setUsuario(id, clave ,valor):

#     if id != -1:
#         usuarioDB = getUsuario(id)

#         if usuarioDB != None and clave != None and valor != None:
#             usuarioDB.getAttr(clave) = valor

#             db.session.add(usuarioDB)
#             db.session.commit()

#             if usuarioDB != None:
#                 return jsonify(usuarioDB.serializar())
#             else:
#                 return jsonify(None)
