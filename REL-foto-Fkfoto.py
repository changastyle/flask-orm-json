import modelo.Foto
from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship


     # FOTO:
     fkFoto = Column(Integer , ForeignKey('fotos.id'))
     foto = relationship('Foto' , foreign_keys=[fkFoto])

