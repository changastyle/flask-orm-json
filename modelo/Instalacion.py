import datetime

from flask.json import jsonify
from ct import Serializador
from sqlalchemy.inspection import inspect
from sqlalchemy.sql.expression import true
from modelo.Foto import Foto
from sqlalchemy.sql.sqltypes import Boolean
from ct import db
import json
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Instalacion(db.Base):
    __tablename__ = 'instalaciones'


    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    urlDominio = Column(Text, nullable=False)
    urlDominioDos = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    passw = Column(Text, nullable=False)
    cc = Column(Text, nullable=False)
    alias = Column(Text, nullable=False)
    firmaMail = Column(Text, nullable=False)
    msg = Column(Text, nullable=False)
    txtTiempoEnvio = Column(Text, nullable=False)
    clientID = Column(Text, nullable=False)
    clientSecret = Column(Text, nullable=False)
    calle = Column(Text, nullable=False)
    ciudad = Column(Text, nullable=False)
    pais = Column(Text, nullable=False)
    carpetaWeb = Column(Text, nullable=False)
    colorPri = Column(Text, nullable=False)
    colorSec = Column(Text, nullable=False)
    colorTer = Column(Text, nullable=False)
    lat = Column(Integer, nullable=False)
    longi = Column(Integer, nullable=False)
    googleMaps = Column(Text, nullable=False)
    prefijo = Column(Text, nullable=False)
    telefonoFijo = Column(Text, nullable=False)
    telefonoWpp = Column(Text, nullable=False)
    minimoCompra = Column(Integer, nullable=False)
    bullets = Column(Boolean , default=False)
    activo = Column(Boolean , default=True)

    # arrFotos = relationship("Foto" ,back_populates="_instalacion")

    fkLogo  = Column(Integer , ForeignKey('fotos.id'))
    logo = relationship("Foto" , foreign_keys=[fkLogo])
    # fkLogo = Column('fkLogo' , Integer , ForeignKey('fkLogo'))
    

    # fkFoto  = Column(Integer, ForeignKey('foto.id'))
    # arrFotos  = relationship("Foto", foreign_keys=[fkFoto])
    # instalacion  = relationship("Instalacion", back_populates = "arrFotos")

    # @OneToOne() @JoinColumn(name = "fkFavicon")
    # private Foto favicon;
    
    # @OneToOne() @JoinColumn(name = "fkLogo")
    # private Foto logo;
    # @OneToMany(cascade = CascadeType.PERSIST, mappedBy = "instalacion") @JsonIgnore
    # private List<Producto> arrProductos;
    # @OneToMany(cascade = CascadeType.PERSIST, mappedBy = "instalacion")
    # private List<Promo> arrPromos;
    # @OneToMany(cascade = CascadeType.PERSIST, mappedBy = "instalacion") @JsonIgnore
    # private List<RelCategoriaInstalacion> arrRelCategorias;
    # @OneToMany(cascade = CascadeType.PERSIST, mappedBy = "instalacion") @JsonIgnore
    # private List<RelDiaInstalacion> arrRelsDiasTrabajo;
    # @OneToMany(cascade = CascadeType.PERSIST, mappedBy = "instalacion") @JsonIgnore
    # private List<Foto> arrFotos;
    
    # @OneToOne() @JoinColumn(name = "fkClienteVolatil")
    # private Cliente clienteVolatil;

  
    #arrFotos = ["perfil.jpg","frontal.jpg", "default.png"]

    def __init__(self , data):
        self.__dict__ = json.loads(data)


    def __str__(self):
        return self.nombre

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def serializar(self):
                
        diccionarioSerializado = Serializador.serializar(self)

        #QUITAR CAMPOS AL DICCIONARIO:
        arrAttsRm = ['passw', 'clientID' , 'clientSecret']
        for attRm in arrAttsRm:
            if attRm in arrAttsRm: 
                del diccionarioSerializado[attRm]

        # AGREGAR CAMPOS COMO TRANSIENT:
        # diccionarioSerializado['fkLogo'] = self.logo.serializar()
        

        return diccionarioSerializado
