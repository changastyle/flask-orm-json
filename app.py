from flask import Flask,render_template, jsonify, make_response, json , send_from_directory
from ct import db
from ws.wsProductos import wsProductos
from ws.wsTareas import wsTareas
from ct.Serializer import  Serializer
from modelo.Producto import Producto

# 1 - CREANDO LA FLASK APP:
class CustomFlask(Flask):
          
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='[%',
        block_end_string='%]',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='[#',
        comment_end_string='#]',
    ))

app = CustomFlask(__name__)
app.static_folder = "res/"
app.template_folder = "web/"

app.register_blueprint(wsProductos,url_prefix='')
app.register_blueprint(wsTareas,url_prefix='')


@app.route("/res/<path:path>")
def static_dir(path):
    # ruta = "/static/"+ str(path)
    # print("ruta estatic:" + ruta)
    return app.send_static_file(path)
    # return "static/"+ str(path)

@app.route('/')
def index():
    return render_template("tareas/tareas.html")


# 2 - RUN SERVER:
if __name__ == '__main__':
    #REPOBLAR DATABASE:
    db.Base.metadata.create_all(db.engine)
    app.run("127.0.0.1", 8000 , debug=True)