from sqlalchemy.inspection import inspect
from datetime import datetime as dt
import time
import datetime

def serializar(self):
    arrAttrs = {}
    
    arrKeys = inspect(self).attrs.keys()
    for nombreAttrLoop in arrKeys:
        valorLoop = getattr(self, nombreAttrLoop)
        tipoDato = str(type(valorLoop))

        # print(str(nombreAttrLoop) + " | " + tipoDato +" | " )

        if  nombreAttrLoop.startswith('_') or str(nombreAttrLoop).startswith("fk"):
            if nombreAttrLoop in arrAttrs: 
                del arrAttrs[nombreAttrLoop]
        elif  tipoDato == "<class 'datetime.datetime'>":
            timestamp =  time.mktime(valorLoop.timetuple())

            # print("FECHA RAW: " + str(valorLoop))
            # print("VALOR: " + str(type(valorLoop)) + " = " + str(valorLoop))
            # print("timestamp: " + str(type(timestamp)) + " = " + str(timestamp))

            dt_object = dt.fromtimestamp(timestamp)
            valorLoop = timestamp

            arrAttrs[nombreAttrLoop] = valorLoop
        elif str(type(valorLoop)).startswith("<class 'sqlalchemy.orm.collections.InstrumentedList'>"):

            # EN EL CASO DE QUE SEA UNA LISTA DE OBJETOS:
            arrAux = {}
            contador = 0
            for itemLoop in valorLoop:
                fotoSerializada = itemLoop.serializar()
                tipoFotoSerializada = type(fotoSerializada)
                arrAux[contador] = itemLoop.serializar()
                contador += 1

            arrAttrs[nombreAttrLoop] = arrAux

        elif str(type(valorLoop)) == "<class 'bool'>":
            if valorLoop == True:
                arrAttrs[nombreAttrLoop] = bool('true')
            else:
                arrAttrs[nombreAttrLoop] = bool('false')
        elif str(type(valorLoop)).startswith("<class 'modelo.") :
            arrAttrs[nombreAttrLoop] = valorLoop.serializar()
        else:
            arrAttrs[nombreAttrLoop] = valorLoop 

    return arrAttrs