import datetime
from dao import dao
from dao.Serializer import Serializer
from sqlalchemy import Column, Integer, Float, Text, DateTime

class Producto(dao.Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    precio = Column(Float)
    fechaAlta = Column(dao.TIMESTAMP, default=datetime.datetime.utcnow())
    arrFotos = ["perfil.jpg","frontal.jpg", "default.png"]

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return self.nombre

    def serialize(self):
        diccionarioSerializado = Serializer.serializar(self)
        print("TIPO SERIALIZAER:", str(type(diccionarioSerializado)))
        #del d['password']

        # AGREGAR CAMPOS COMO TRANSIENT:
        diccionarioSerializado['arrFotos'] = self.arrFotos

        #QUITAR CAMPOS AL DICCIONARIO:
        #diccionarioSerializado.pop("precio")

        return diccionarioSerializado
