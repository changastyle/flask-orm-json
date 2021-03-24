import inspect 
import importlib

from sqlalchemy.sql.operators import startswith_op
nombreClase = input("CLASE:")

arrLineas = []

# nombreClase = nombreClase.lower()
nombreClase = nombreClase.capitalize()

paquete = "modelo." + str(nombreClase)
nombreClasee = str(nombreClase)

primeraLineaParametrosContructor = "      def __init__(self"
arrLineas.append(primeraLineaParametrosContructor)

#  1 - OBTENGO LOS ATRIBUTOS DE LA CLASE EN CUESTION:
clase = getattr(importlib.import_module(paquete), nombreClasee)
print("clase:" + str(type(clase)))
instancia = clase()
print("instancia:" + str(type(instancia)))



#  2 - RECORRO LOS ATRIBUTOS Y ACUMULO EN ARR LINEAS:
if instancia != None:
      arrKeys = instancia.__dir__()
      # arrKeys = instancia.__dict__.keys()

      print("PROPIEDADES: "  + str(len(arrKeys)))
      for propLoop in arrKeys:
            if not str(propLoop).startswith('_') and not str(propLoop).startswith("id") and not str(propLoop).startswith("serializar") and not str(propLoop).startswith("registry") and not str(propLoop).startswith("metadata"):
                  print(propLoop)
                  primeraLineaParametrosContructor = primeraLineaParametrosContructor + ("," + propLoop )
                  arrLineas.append("            self." + propLoop + " = " + propLoop)
      
      primeraLineaParametrosContructor = primeraLineaParametrosContructor + "):"
      arrLineas[0] = primeraLineaParametrosContructor


# 3 - GUARDO EL ARCHIVO:
nombreArchi = ""+ nombreClasee  + "-save"
f = open(nombreArchi + ".py", "w")
print("GUARDO ARCHIVO:" + str(nombreArchi))

strTotal = ""

for lineaLopp in arrLineas:
      strTotal += str("" + lineaLopp ) + "\n"

f.write(strTotal)
f.close()
