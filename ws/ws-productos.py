from crypt import methods

from flask import  Flask, jsonify

app = Flask(__name__)

app.route('/')
def hola():
    return "hola"

app.route('/findProductos')
def findProductos():
    array = ["lechuga","tomate" , "pera"]
    return jsonify(array)

if __name__ == "__main__":
    app.run()