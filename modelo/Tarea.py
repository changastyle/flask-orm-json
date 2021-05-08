import datetime

from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from modelo import Usuario
from ct import Serializador
from sqlalchemy import Column, Integer, Float, Text, DateTime ,ForeignKey
from sqlalchemy.orm import relationship

class Tarea(db.Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True)
    titulo = Column(Text, nullable=False)
    descripcion = Column(Text, nullable=False)
    fechaAlta = Column(db.DateTime, default=datetime.datetime.utcnow())
    fechaEntrega = Column(db.DateTime, default=datetime.datetime.utcnow())
    activa = Column(Boolean , default=True)
    terminada = Column(Boolean , default=False)

    # fkCliente  = Column(Integer , ForeignKey('usuarios.id'))
    # usuario = relationship("Usuario" )
    #arrFotos = ["perfil.jpg","frontal.jpg", "default.png"]

    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return self.titulo

    def serializar(self):
                
        diccionarioSerializado = Serializador.serializar(self)

        #QUITAR CAMPOS AL DICCIONARIO:
        # arrAttsRm = ['pass','foto']
        # for attRm in arrAttsRm:
        #     if attRm in arrAttrs: 
        #         del diccionarioSerializado['attRm']

        # AGREGAR CAMPOS COMO TRANSIENT:
        #diccionarioSerializado['arrFotos'] = self.arrFotos
        

        return diccionarioSerializado   
