from sqlalchemy.inspection import inspect
from datetime import datetime as dt
import time
import datetime
from flask import session , request , jsonify 
from ct import  db
from modelo.Usuario import Usuario
from modelo.Instalacion import Instalacion
from sqlalchemy import and_, or_, not_



nombreVariableSesion = "user"


def limpiarURL(url , request):
    
    posDotCom = -1
    posDosPuntos = -1

    strHttp = "://"
    strDotCom = ".com"
    strDosPuntos = ":"

    urlGet = request.args.get('url')
    if urlGet != None:
        url = urlGet

    print("URL PROCESADA: " + str(url))
    
    if url != None:
        
        # HTTP:
        if strHttp in url:
            posHttp = url.index(strHttp)

            if posHttp > -1:
                largoPosHttp = len(strHttp)
                largoTotal = posHttp + largoPosHttp
                url = url[ largoTotal : ]

        # DOT COM:            
        if strDotCom in url:
            posDotCom = url.index(strDotCom)

            if posDotCom > -1:
                url = url[0 : posDotCom]

        # DOS PUNTOS:            
        if strDosPuntos in url:
            posDosPuntos = url.index(strDosPuntos)

            if posDosPuntos > -1:
                url = url[0 : posDosPuntos]
    

    print("URL PROCESADA: " + str(url))
    return url







# LOGEO DE USUARIOS:
def loginSerial(user , passw):
    rta = None


    print("VOY A LOGEAR A :" + str(user) + " - " + str(passw));

    usuarioDB = getUsuarioByEmailAndPassw(user , passw)

    if usuarioDB != None:
        rta = usuarioDB.serializar()
        session[nombreVariableSesion] = rta

    return rta

def comprobarUsuarioLogeadoSerial():
          
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

                        print("EL USUARIO LOGEADO ES: " + str(usuarioLogeado))

                        if usuarioLogeado != None:
                            rta = usuarioLogeado
    
    return rta
    
def getUsuarioByEmail(email):
          
    try:
        rta = db.session.query(Usuario).filter_by(email = email).first()
    except Exception as e: 
        print(e)
        db.session.rollback()

   

    return rta


def exitSerial():
    
    rta = None

    if session != None:
              
        if session != None:
            
            if nombreVariableSesion in session:
                      
                session[nombreVariableSesion]  = None
                rta = None


def getUsuarioByEmailAndPassw(email , passw):
          
    rta = db.session.query(Usuario).filter(
        and_(
            Usuario.email == email,
            Usuario.passw == passw
        )
    ).first()

    return rta

def getInstalacionSegunURL(url):
          
    rta = None
    
    url = limpiarURL(url , request)

    print("URL RECIBIDA: " + url)

    search = "%" + url + "%"

    print("SEARCH:" + search)

    try:

        rta = db.session.query(Instalacion).filter(
            or_(
                Instalacion.urlDominio.like(search),
                Instalacion.urlDominioDos.like(search)
            )
        ).first()
    
    except Exception as e: 
        print(e)
        db.session.rollback()

    return rta
