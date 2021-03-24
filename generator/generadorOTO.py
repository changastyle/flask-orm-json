claseHija = input("CLASE HIJA:")
nombreFK = input("NOMBRE FK:")

nombreHijaLower = claseHija.lower()
nombreHijaCap = claseHija.capitalize()
nombreHijaUP = claseHija.upper()

nombreFKLower = nombreFK.lower()
nombreFKCap = nombreFK.capitalize()
nombreFKUP = nombreFK.upper()

nombreTablaSQL = nombreHijaLower 
if nombreHijaLower.endswith('a') or nombreHijaLower.endswith('e') or nombreHijaLower.endswith('i') or nombreHijaLower.endswith('o') or nombreHijaLower.endswith('u'):
      nombreTablaSQL += "s"
else:
      nombreTablaSQL += "es"

nombreClaseHijaSinS = nombreFKCap
if nombreFKCap.endswith('s'):
      nombreClaseHijaSinS = nombreClaseHijaSinS[:-1]
# else:
      # nombreClaseHijaSinS += "es"
      
arrLineas = [
      "import modelo." + nombreHijaCap +"\n"
      "from sqlalchemy import Column, Integer, Float, Text, DateTime , ForeignKey\n"
      "from sqlalchemy.orm import relationship\n"
      "\n"
      "\n"
      "     # " +  nombreHijaUP  + ":\n"
      "     " + nombreFK +" = Column(Integer , ForeignKey('" + nombreTablaSQL + ".id'))\n"
      "     " + nombreHijaLower +" = relationship('" + nombreHijaCap + "' , foreign_keys=[" + nombreFK + "])\n"
      "\n"
]

nombreArchi = "REL-"+ nombreHijaLower + "-"  + nombreFKCap + ""
f = open(nombreArchi + ".py", "w")

strTotal = ""

for lineaLopp in arrLineas:
      strTotal += str("" + lineaLopp)

f.write(strTotal)
f.close()
