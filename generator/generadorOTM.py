nombrePadre = input("CLASE PADRE:")
nombreArr = input("NOMBRE ARRAY (CON S):")

nombrePadreLower = nombrePadre.lower()
nombrePadreCap = nombrePadreLower.capitalize()
nombrePadreUP = nombrePadre.upper()

nombreArrLower = nombreArr.lower()
nombreArrCap = nombreArrLower.capitalize()
nombreArrUP = nombreArr.upper()

nombreTablaSQL = nombrePadreLower 
if nombrePadreLower.endswith('a') or nombrePadreLower.endswith('e') or nombrePadreLower.endswith('i') or nombrePadreLower.endswith('o') or nombrePadreLower.endswith('u'):
      nombreTablaSQL += "s"
else:
      nombreTablaSQL += "es"

nombreClaseHijaSinS = nombreArrCap
if nombreArrCap.endswith('s'):
      nombreClaseHijaSinS = nombreClaseHijaSinS[:-1]
# else:
      # nombreClaseHijaSinS += "es"
      
nombreArrCap

arrLineas = [
      "from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey\n"
      "from sqlalchemy.orm import relationship\n"
      "\n"
      "\n"
      "#" + nombrePadreUP + ":\n"
	"arr" + nombreArrCap + " = relationship('" + nombreClaseHijaSinS + "' ,back_populates='_" + nombrePadreLower + "')\n"
      "\n"
	"#" + nombreArrUP + ":\n"
	"fk" + nombrePadreCap + "  = Column(Integer , ForeignKey('" + nombreTablaSQL + ".id'))\n"
	"_" + nombrePadreLower + " = relationship('" + nombrePadreCap + "', back_populates='arr" + nombreArrCap + "')\n"
]

nombreArchi = "REL-"+ nombrePadreCap + "-arr"  + nombreArrCap + ""
f = open(nombreArchi + ".py", "w")

strTotal = ""

for lineaLopp in arrLineas:
      strTotal += str("" + lineaLopp)

f.write(strTotal)
f.close()
