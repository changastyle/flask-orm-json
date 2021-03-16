from flask import Flask,render_template, jsonify, make_response, json
from dao import dao
from ws.wsProductos import productos
from dao.Serializer import  Serializer
from modelo.Producto import Producto

# 1 - CREANDO LA FLASK APP:
app = Flask(__name__)
app.register_blueprint(productos,url_prefix='')

@app.route('/')
def index():
    # return "hola"
    return render_template("index.html")


# 2 - RUN SERVER:
if __name__ == '__main__':
    #REPOBLAR DATABASE:
    dao.Base.metadata.create_all(dao.engine)
    app.run("127.0.0.1", 5000 , debug=True)