from dao import dao
from modelo.Producto import Producto


def chota():

    dao.Base.metadata.create_all(dao.engine)

    arroz = Producto("ARROZ",1.25)
    dao.session.add(arroz)
    print(arroz.id)
    dao.session.commit()
    print(arroz.id)

chota()


