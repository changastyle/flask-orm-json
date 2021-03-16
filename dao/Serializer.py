from sqlalchemy.inspection import inspect
import json
import datetime
class Serializer(object):

    def serializar(self):

        arrAttrs = {};
        if self != None:

            for nombreAttrLoop in inspect(self).attrs.keys():
                valorLoop = getattr(self, nombreAttrLoop)
                tipo = str(type(valorLoop))

                if tipo == "<class 'datetime.datetime'>":
                    print("valor loop:", valorLoop)
                    fecha = datetime.datetime.strptime(str(valorLoop), '%Y-%m-%d %H:%M:%S')
                    print("fecha:", fecha)
                    longFecha = fecha.timestamp()
                    print("ENTRE A FECHA")
                    print(nombreAttrLoop +" - tipo:" + str(tipo) + " = " + str(longFecha))
                    valorLoop = int(longFecha)
                else:
                    print(nombreAttrLoop + " - tipo:" + str(tipo) + " = " + str(valorLoop))

                arrAttrs[nombreAttrLoop] = valorLoop

           # return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
        return arrAttrs

    def serializarL(lista):
        return [itemLoop.serialize() for itemLoop in lista]
