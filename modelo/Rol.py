import datetime

from flask.json import jsonify
from ct import controller
from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from sqlalchemy.inspection import inspect
import modelo.Instalacion
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Rol(db.Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    jerarquia = Column(Integer)
    orden = Column(Integer)
    activo = Column(Boolean, default=True)

    def __init__(self, urlProvisoria):
        self.urlProvisoria = urlProvisoria

    def __str__(self):
        return self.urlProvisoria


    def serializar(self):
                
        diccionarioSerializado = controller.serializar(self)

        #QUITAR CAMPOS AL DICCIONARIO:
        # arrAttsRm = ['arrFotos']
        # for attRm in arrAttsRm:
        #     if attRm in arrAttsRm: 
        #         del diccionarioSerializado[attRm]

        # AGREGAR CAMPOS COMO TRANSIENT:
        # diccionarioSerializado['fullFoto'] = self.getFullFoto()
        

        return diccionarioSerializado