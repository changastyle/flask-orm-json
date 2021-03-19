from sqlalchemy.inspection import inspect
import json
import time
from datetime import datetime as dt
import datetime
class Serializer(object):

    def serializar(self):

        arrAttrs = {};
        if self != None:

            for nombreAttrLoop in inspect(self).attrs.keys():
                valorLoop = getattr(self, nombreAttrLoop)
                tipo = str(type(valorLoop))

                soyFecha = False
                if tipo == "<class 'datetime.datetime'>":
                    soyFecha = True
                    print("FECHA RAW: " + str(valorLoop))
                    print("VALOR: " + str(type(valorLoop)) + " = " + str(valorLoop))

                    timestamp =  time.mktime(valorLoop.timetuple())
                    print("timestamp: " + str(type(timestamp)) + " = " + str(timestamp))

                    dt_object = dt.fromtimestamp(timestamp)
                    print("dt_object: " + str(type(dt_object)) + " = " + str(dt_object))
                    # fechaDT = datetime.datetime.strptime(str(valorLoop), '%Y-%m-%d %H:%M:%S')
                    # # print("fechaDT: " + str(fechaDT))
                    # # longFecha = fechaDT.timestamp()
                    valorLoop = timestamp

                    # fechax = datetime.datetime.strptime(str(valorLoop), '%Y-%m-%d %H:%M:%S')
                    # print("fechax: " + str(fechax))
                else:
                    soyFecha = False      
                    print(nombreAttrLoop + " - tipo:" + str(tipo) + " = " + str(valorLoop))

                arrAttrs[nombreAttrLoop] = valorLoop

                # SI SOY FECHA AGREGO UNA SEGUNDO ATT JS MULTIPLICADA POR 1000:
                if soyFecha:
                    nuevoNombre = str(nombreAttrLoop+"JS")
                    arrAttrs[nuevoNombre] = (valorLoop * 1000)

        return arrAttrs
