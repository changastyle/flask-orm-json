import datetime

from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from ct import controller
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Cliente(db.Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    cuit = Column(Text, nullable=False)
    fechaAlta = Column(db.DateTime, default=datetime.datetime.utcnow())
    activo = Column(Boolean , default=True)



    def __str__(self):
        return self.nombre

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
