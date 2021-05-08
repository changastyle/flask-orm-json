import datetime

from flask.json import jsonify
from ct import Serializador
from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from sqlalchemy.inspection import inspect
import modelo.Instalacion
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Promo(db.Base):
    __tablename__ = 'promos'
    id = Column(Integer, primary_key=True)
    href = Column(Text, nullable=False)
    nombre = Column(Text, nullable=False)
    titulo = Column(Text, nullable=False)
    subtitulo = Column(Text, nullable=False)
    terTitulo = Column(Text, nullable=False)


    # FOTO:
    fkFoto = Column(Integer , ForeignKey('fotos.id'))
    foto = relationship('Foto' , foreign_keys=[fkFoto])

    fkInstalacion  = Column(Integer , ForeignKey('instalaciones.id'))
    # _instalacion = relationship("Instalacion", back_populates="arrFotos")

    orden = Column(Integer , default=99)
    xs = Column(Boolean , default=False)
    activo = Column(Boolean , default=True)


    def __init__(self, href):
        self.href = href

    def __str__(self):
        return self.urlProvisoria


    def serializar(self):
                
        diccionarioSerializado = Serializador.serializar(self)

        #QUITAR CAMPOS AL DICCIONARIO:
        # arrAttsRm = ['arrFotos']
        # for attRm in arrAttsRm:
        #     if attRm in arrAttsRm: 
        #         del diccionarioSerializado[attRm]

        # AGREGAR CAMPOS COMO TRANSIENT:
        # diccionarioSerializado['fullFoto'] = self.getFullFoto()
        

        return diccionarioSerializado
   