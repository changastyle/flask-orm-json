import datetime

from flask.json import jsonify
from ct import controller
from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from sqlalchemy.inspection import inspect
import modelo.Instalacion
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Foto(db.Base):
    __tablename__ = 'fotos'
    id = Column(Integer, primary_key=True)
    urlProvisoria = Column(Text, nullable=False)

    fkInstalacion  = Column(Integer , ForeignKey('instalaciones.id'))
    _instalacion = relationship("Instalacion", back_populates="arrFotos")

    activo = Column(Boolean , default=True)


    # @ManyToOne() @JoinColumn(name = "fkInstalacion") @JsonIgnore
    # private Instalacion instalacion;

    def __init__(self, urlProvisoria):
        self.urlProvisoria = urlProvisoria

    def __str__(self):
        return self.urlProvisoria


    def serializar(self):
        diccionarioSerializado = controller.serializar(self)

        #QUITAR CAMPOS AL DICCIONARIO:
        # arrAttsRm = ['pass','foto']
        # for attRm in arrAttsRm:
        #     if attRm in arrAttrs: 
        #         del diccionarioSerializado['attRm']

        # AGREGAR CAMPOS COMO TRANSIENT:
        #diccionarioSerializado['arrFotos'] = self.arrFotos
        

        return diccionarioSerializado
