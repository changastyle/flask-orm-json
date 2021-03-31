from flask import Flask,render_template, jsonify, make_response, json , send_from_directory
from ct import db
from ws.wsProductos import wsProductos
from ws.wsTareas import wsTareas
from ws.wsInstalaciones import wsInstalaciones
from ws.wsPagina import wsPagina
from ws.wsFotos import wsFotos
from ws.wsRol import wsRol
from ws.wsUsuario import wsUsuario
from modelo.Producto import Producto

# -1 - FLASK CONFIG:
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
DEBUG = True
app.static_folder = "res/"
app.template_folder = "web/"
app.secret_key = "CLAVE-MAESTRA-SESSION"

# 0 REGISTER WS:
app.register_blueprint(wsProductos,url_prefix='')
app.register_blueprint(wsTareas,url_prefix='')
app.register_blueprint(wsInstalaciones,url_prefix='')
app.register_blueprint(wsFotos,url_prefix='')
app.register_blueprint(wsPagina,url_prefix='')
app.register_blueprint(wsUsuario,url_prefix='')
app.register_blueprint(wsRol,url_prefix='')
#
#  1 - INDEX HTML:
@app.route('/')
def index():
    return render_template("home/home.html")
    # return render_template("tareas/tareas.html")

# 2 - RES FOLDER:
@app.route("/res/<path:path>")
def static_dir(path):
          return app.send_static_file(path)

# 5 - NO CACHE
@app.after_request
def add_header(r):
    
    if DEBUG:
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'

    return r

# 3 - RUN FLASK APP & POPULATING DB:
if __name__ == '__main__':
    #REPOBLAR DATABASE:
    db.Base.metadata.create_all(db.engine)
    app.run("localhost", 8000 , debug=DEBUG)