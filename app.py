from flask import Flask, jsonify, make_response, json
from dao import dao
from dao.Serializer import  Serializer
from modelo.Producto import Producto

# 1 - CREANDO LA FLASK APP:
app = Flask(__name__)

@app.route('/')
def index():
    return "hola"

@app.route('/getProducto/<id>')
def getProducto(id):
    rta = dao.session.query(Producto).first()
    return jsonify(rta.serialize())

@app.route('/findProductos')
def findProductos():
    arrProductos = dao.session.query(Producto).all()

    return jsonify(Serializer.serializarL(arrProductos))


# 2 - RUN SERVER:
if __name__ == '__main__':
    dao.Base.metadata.create_all(dao.engine)
    app.run("127.0.0.1", 5000 , debug=True)