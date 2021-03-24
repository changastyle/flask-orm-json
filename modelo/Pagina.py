import datetime

from flask.json import jsonify
from ct import controller
from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from sqlalchemy.inspection import inspect
import modelo.Instalacion
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Pagina(db.Base):
    __tablename__ = 'paginas'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    enlace = Column(Text, nullable=False)
    jerarquiaR = Column(Integer)
    jerarquiaW = Column(Integer)
    urlBG = Column(Text, nullable=False)
    bgPosX = Column(Text, nullable=False)
    bgPosY = Column(Text, nullable=False)
    icono = Column(Text, nullable=False)
    mostrarEnMenu = Column(Boolean, default=True)
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