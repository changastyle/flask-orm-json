import os
import pandas as pd
import codecs

def leerXLSX(carpeta , ruta ):
      clear = lambda: os.system('cls')
      clear()

      datosExcel = pd.read_excel(carpeta + ruta)

      matrizExcel = datosExcel.shape
      maxCols = matrizExcel[1]
      maxRows = matrizExcel[0]
      arrColumnas = datosExcel.columns
      print("MAX COLS(" + str(maxCols)+"):")
      print("MAX ROWS(" + str(maxRows)+"):")

      # RECORRO LAS COLUMNAS:
      json = "["

      datosCol = ""
      for i in range(maxRows):
            # print(i)
            datosCol += str("{")
            for columnaLoop in arrColumnas:
                  # print(columnaLoop)
                  # print(datosExcel[columnaLoop][i])
                  valorLoop = datosExcel[columnaLoop][i]
                  columnaLoop =  str(columnaLoop).replace('"','\\"')
                  valorLoop = str(valorLoop).replace('"','\\"')
                  datosCol += str("\"" + columnaLoop + "\"")  + str(":") + str("\"") + str( valorLoop ) + str("\"")+ str(",")
            datosCol = datosCol[:-1]
            datosCol += str("},")
            # print(datosCol)
            
            json += datosCol

            datosCol = ""
      json = json[:-1]
      json += "]" 

      print(json)
      archivoSaliente = codecs.open(carpeta + " salida.json", "w" , "utf-8")
      archivoSaliente.write(json)
      archivoSaliente.close()
      # archivoSaliente2 = codecs.open(" salida.json", "w", "utf-8")
      # archivoSaliente2.write(json)
      # archivoSaliente2.close()
      # print(datosExcel['CODIGO'][20])

leerXLSX("C:\TEMP\\","MR-PRECIO.xlsx")