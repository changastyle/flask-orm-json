import datetime

from flask.json import jsonify
import ct.Serializador
from sqlalchemy.sql.sqltypes import Boolean, Date
from ct import db
from ct import Serializador
from sqlalchemy.inspection import inspect
import modelo.Instalacion
import modelo.Rol
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Usuario(db.Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    email = Column(Text, nullable=False , default="xxx")
    passw = Column(Text, nullable=False , default="xxx")
    token = Column(Text, nullable=False, default="xxx")
    observaciones = Column(Text, nullable=True)
    fechaAlta = Column(Date , default= datetime.datetime.now)
    fechaNacimiento = Column(Date , default= datetime.datetime.now)
    telefono = Column(Text, nullable=True , default="xxx")

    # ROL:
    fkRol  = Column(Integer , ForeignKey('roles.id') , default=1)    
    rol = relationship('Rol' , foreign_keys=[fkRol])
    
    # INSTALACION:
    fkInstalacion = Column(Integer , ForeignKey('instalaciones.id'))
    instalacion = relationship('Instalacion' , foreign_keys=[fkInstalacion])

    # arrFavoritos
    activo = Column(Boolean, default=True)

    def __init__(self, **kwargs): 
       for claveParam , valorParam in kwargs.items():
            valorLoop = setattr(self, claveParam , valorParam)
            print(str(self.nombre) + " {} = {}".format(claveParam, valorParam))


    def __str__(self):
        if self.nombre == None:
            return "nada"
        else:
            return self.nombre
                  


    def serializar(self):
                
        diccionarioSerializado = Serializador.serializar(self)

        #QUITAR CAMPOS AL DICCIONARIO:
        arrAttsRm = ['passw']
        for attRm in arrAttsRm:
            if attRm in arrAttsRm: 
                del diccionarioSerializado[attRm]

        # AGREGAR CAMPOS COMO TRANSIENT:
        # diccionarioSerializado['_sa_instance_state'] = self.__instance__()
        

        return diccionarioSerializado