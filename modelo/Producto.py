import datetime
from ct import db, Serializador , Controller
from sqlalchemy import Column, Integer, Float, Text, DateTime

class Producto(db.Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    precio = Column(Float)
    fechaAlta = Column(db.DateTime, default=datetime.datetime.utcnow())
    #arrFotos = ["perfil.jpg","frontal.jpg", "default.png"]

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return self.nombre

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
