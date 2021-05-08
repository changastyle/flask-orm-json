import datetime

from flask.json import jsonify
from ct import Serializador
from sqlalchemy.sql.sqltypes import Boolean
from ct import db
from sqlalchemy.inspection import inspect
import modelo.Instalacion
import modelo.Pagina
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class RelRolPagina(db.Base):
    __tablename__ = 'relsrolpaginas'
    id = Column(Integer, primary_key=True)
    
    #PAGINA:
    fkPagina = Column(Integer , ForeignKey('paginas.id'))
    pagina = relationship("Pagina" )

    #ROL:
    fkRol = Column(Integer , ForeignKey('roles.id'))
    rol = relationship("Rol" )

    #INSTALACION:
    fkInstalacion = Column(Integer , ForeignKey('instalaciones.id'))
    instalacion = relationship("Instalacion" )

    orden = Column(Integer)
    activo = Column(Boolean, default=True)


    def __init__(self):
        pass

    def __str__(self):
        return "REl" + str(id)


    def serializar(self):
                
        diccionarioSerializado = Serializador.serializar(self)

        #QUITAR CAMPOS AL DICCIONARIO:
        arrAttsRm = ['instalacion']
        for attRm in arrAttsRm:
            if attRm in arrAttsRm: 
                del diccionarioSerializado[attRm]

        # AGREGAR CAMPOS COMO TRANSIENT:
        # diccionarioSerializado['fullFoto'] = self.getFullFoto()
        

        return diccionarioSerializado