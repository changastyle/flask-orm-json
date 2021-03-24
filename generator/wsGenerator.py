
def generarWS(nombreClase):

      nombreClase = nombreClase.lower()
      nombreClase = nombreClase.capitalize()
      nombreWS = str("ws") + nombreClase.capitalize()


      lowerNombreClase = nombreClase.lower()
      capitalNombreClase = nombreClase.capitalize()

      arrLineas = [
      "from flask import Flask, jsonify, make_response, json\n",
      "from ct import db, controller\n",
      "from modelo." + capitalNombreClase + " import " + capitalNombreClase + "\n",
      "from flask import Blueprint, render_template\n",
      "\n",
      nombreWS + " = Blueprint('"+ nombreWS +"',__name__,static_folder='static', template_folder='templates')\n",
      "\n",
      "#AGREGAR AL APP.PY:\n",
      "#app.register_blueprint(" + nombreWS + ",url_prefix='')\n",
      "\n",
      "\n",
      "@"+ nombreWS + ".route('/" + lowerNombreClase + "s')\n",
      "def ventana" + capitalNombreClase + "s():\n",
      "    return render_template('" + lowerNombreClase + "/" + lowerNombreClase + ".html')\n",
      "\n",
      "@" + nombreWS + ".route('/get" + capitalNombreClase + "/<id>')\n",
      "def get" + capitalNombreClase + "(id):\n",
      "    rta = db.session.query(" + capitalNombreClase + ").filter_by(id=id).first()\n",
      "    if rta != None:\n",
      "        return jsonify(rta.serializar())\n",
      "    else:\n",
      "        return jsonify(None)\n",
      "\n",
      "\n",
      "@" + nombreWS + ".route('/find" + capitalNombreClase + "s')\n",
      "def find" + capitalNombreClase+ "s():\n",
      "    arr = db.session.query(" + capitalNombreClase + ").all()\n",
      "\n",
      "    arrSerializado = []\n",
      "    for itemLoop in arr:\n",
      "        arrSerializado.append(itemLoop.serializar()) \n",
      "\n",
      "    return jsonify(arrSerializado)\n",
      "\n",
      "\n",
      "@" +  nombreWS +".route('/alta" + capitalNombreClase + "/<nombre>/<precio>')\n",
      "def alta" + capitalNombreClase + "(nombre, precio):\n",
      "\n"          ,
      "    nvo = " + capitalNombreClase + "(nombre,precio)\n",
      "    db.session.add(nvo)\n",
      "    db.session.commit()\n",
      "\n",
      "    if nvo != None:\n",
      "        return jsonify(nvo.serializar())\n",
      "    else:\n",
      "        return jsonify(None)\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "@" + nombreWS + ".route('/rm" + capitalNombreClase + "/<id>')\n"
      "def rm" + capitalNombreClase + "(id):"
      "\n"
      "\n"
      "    " + lowerNombreClase + "DB = get" + capitalNombreClase + "(id)\n"
      "    if " + lowerNombreClase + "DB != None:\n"
      "          " + lowerNombreClase + "DB.activo = False\n"
      "\n"
      "          db.session.add(" + lowerNombreClase + "DB)\n"
      "          db.session.commit()\n"
      "\n"
      "\n"
      "          if " + lowerNombreClase + "DB != None:\n"
      "                return jsonify(" + lowerNombreClase + "DB.serializar())\n"
      "          else:\n"
      "                return jsonify(None)\n"

      "@ws" + capitalNombreClase + ".route('/activar" + capitalNombreClase + "/<id>')\n"
      "def activar" + capitalNombreClase + "(id):\n"
      "\n"
      "    " + lowerNombreClase + "DB = get" + capitalNombreClase + "(id)\n"
      "    if " + lowerNombreClase + "DB != None:\n"
      "        " + lowerNombreClase + "DB.activo = False;\n"
      "\n"
      "    db.session.add(" + lowerNombreClase + "DB)\n"
      "    db.session.commit()\n"
      "\n"
      "    if " + lowerNombreClase + "DB != None:\n"
      "        return jsonify(" + lowerNombreClase + "DB.serializar())\n"
      "    else:\n"
      "        return jsonify(None)\n"
      "\n"
      "@ws" + capitalNombreClase + ".route('/set" + capitalNombreClase + "/<id>/<clave>/<valor>')\n"
      "def set" + capitalNombreClase + "(id, clave ,valor):\n"
      "\n"
      "    if id != -1:\n"
      "        " + lowerNombreClase + "DB = get" + capitalNombreClase + "(id)\n"
      "\n"
      "        if " + lowerNombreClase + "DB != None and clave != None and valor != None:\n"
      "            " + lowerNombreClase + "DB.getAttr(clave) = valor\n"
      "\n"
      "            db.session.add(" + lowerNombreClase + "DB)\n"
      "            db.session.commit()\n"
      "\n"
      "            if " + lowerNombreClase + "DB != None:\n"
      "                return jsonify(" + lowerNombreClase + "DB.serializar())\n"
      "            else:\n"
      "                return jsonify(None)\n"
      ]


      f = open(nombreWS + ".py", "w")
      strTotal = ""
      for lineaLopp in arrLineas:
            strTotal += str("" + lineaLopp)
      f.write(strTotal)
      f.close()


nombreClase = input("A QUE CLASE LE VAS A CREAR EL WS:")

generarWS(nombreClase)