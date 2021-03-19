import datetime

from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from ct.Serializer import Serializer
from sqlalchemy import Column, Integer, Float, Text, DateTime

class Tarea(db.Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True)
    titulo = Column(Text, nullable=False)
    descripcion = Column(Text, nullable=False)
    fechaAlta = Column(db.DateTime, default=datetime.datetime.utcnow())
    fechaEntrega = Column(db.DateTime, default=datetime.datetime.utcnow())
    activa = Column(Boolean , default=True)
    terminada = Column(Boolean , default=False)
    fkCliente = Column(Integer , nullable=False)
    #arrFotos = ["perfil.jpg","frontal.jpg", "default.png"]

    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return self.titulo

    def serializar(self):
        diccionarioSerializado = {}

        if self != None:

            diccionarioSerializado = Serializer.serializar(self)
            print("TIPO SERIALIZAER:", str(type(diccionarioSerializado)))
            #del d['password']

            # AGREGAR CAMPOS COMO TRANSIENT:
            #diccionarioSerializado['arrFotos'] = self.arrFotos
            diccionarioSerializado['fechax'] = self.fechaEntrega
            
            #QUITAR CAMPOS AL DICCIONARIO:
            #diccionarioSerializado.pop("precio")

        return diccionarioSerializado
