from flask import Flask, jsonify, make_response, json
from ct import db, controller
from modelo.Pagina import Pagina
from flask import request
from flask import Blueprint, render_template
from sqlalchemy import and_, or_, not_

wsPagina = Blueprint('wsPagina',__name__,static_folder='static', template_folder='templates')

#AGREGAR AL APP.PY:
#app.register_blueprint(wsPagina,url_prefix='')


@wsPagina.route('/getPerfilByURL/<url>')
def getPerfilByURL(url):

    #Cliente usuarioLogeado = MasterController.dameClienteLogeadoFromDB(request);
        
    if url != None:
        url = controller.limpiarURL(url , request)

        search = "%" + url + "%"
        
        rta = db.session.query(Pagina).filter(
                Pagina.enlace.like(search)
        ).first()

        if rta == None:
            print("PAGINA RTA: "+ str(rta))

        return rta

        #perfilWeb.setArrRelsPaginas(perfilWeb.dameArrRelsPaginasPosiblesSegunUsuario(usuarioLogeado));
        
        # List<RelPerfilPagina> arrRels = new ArrayList<>();
        # if(perfilWeb.isEsHome())
        # {
        #     List<Categoria> arrCategoriasConProductos = wsCategoria.findCategoriasByInstalacionConProductos(request);
            
        #     //AGREGO LAS CATEGORIAS DE PRODUCTOS A LA BARRA DE MENU:
        #     for(Categoria categoriaLoop : arrCategoriasConProductos)
        #     {
        #         String urlPaginaAux =  "../categoria/categoria.jsp?fkCategoria=" + categoriaLoop.getId();
        #         String nombrePaginaAux = categoriaLoop.getNombre() ;
        #         String iconoPaginaAux = categoriaLoop.getIcono() ;
        #         Pagina paginaAux = new Pagina(true, 0, 0, urlPaginaAux, iconoPaginaAux , true, true, nombrePaginaAux, 1, "", perfilWeb);
        #         paginaAux.setMostrarEnMenu(true);
                
        #         RelPerfilPagina relPerfilPagina = new RelPerfilPagina(true,paginaAux, perfilWeb);
        #         arrRels.add(relPerfilPagina);
        #     }
            
        #     perfilWeb.setArrRelsPaginas(arrRels);
        # }
        
        # wsClick.addClick(request, -1, -1, paginaDB.getId());

@wsPagina.route('/getPagina/<id>')
def getPagina(id):
    rta = db.session.query(Pagina).filter_by(id=id).first()
    if rta != None:
        return jsonify(rta.serializar())
    else:
        return jsonify(None)


@wsPagina.route('/findPaginas')
def findPaginas():
    arr = db.session.query(Pagina).all()

    arrSerializado = []
    for itemLoop in arr:
        arrSerializado.append(itemLoop.serializar()) 

    return jsonify(arrSerializado)


@wsPagina.route('/altaPagina/<nombre>/<precio>')
def altaPagina(nombre, precio):

    nvo = Pagina(nombre,precio)
    db.session.add(nvo)
    db.session.commit()

    if nvo != None:
        return jsonify(nvo.serializar())
    else:
        return jsonify(None)




@wsPagina.route('/rmPagina/<id>')
def rmPagina(id):

    paginaDB = getPagina(id)
    if paginaDB != None:
          paginaDB.activo = False

          db.session.add(paginaDB)
          db.session.commit()


          if paginaDB != None:
                return jsonify(paginaDB.serializar())
          else:
                return jsonify(None)
@wsPagina.route('/activarPagina/<id>')
def activarPagina(id):

    paginaDB = getPagina(id)
    if paginaDB != None:
        paginaDB.activo = False;

    db.session.add(paginaDB)
    db.session.commit()

    if paginaDB != None:
        return jsonify(paginaDB.serializar())
    else:
        return jsonify(None)
