from dao import dao
from modelo.Producto import Producto

papaDB = dao.session.query(Producto).filter_by(nombre="papa").first()
print("PAPA DB: %s",papaDB.id)

