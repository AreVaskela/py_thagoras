# Laskee suorakulmaisen kolmion hypotenuusan kahdesta sivusta.
# Tehty python 2.7:lla, joka asennettu PATHiin ja ajetaan "python .\pytarogoras.py input.txt output.txt"
# input tulee py_input.txt filusta ja on otsikkorivi ja kahden floatin riveja
# output menee py_output.txt filuun ja on otsikkorivi, eka sivu metrina, toka sivu metrina ja hypotenuusa

import math
import sys

# hypotenuusan lasku
def laskePythagoras(sivu1, sivu2):
	neliot=(sivu1*sivu1) + (sivu2*sivu2)
	return math.sqrt(neliot)

def toMeter(feet):
	f = float(feet)
	return float(f*0.3048)

#input rivi kerrallaan, eka rivi pois, autoclose, eka argumentti
with open(str(sys.argv[1]), "r") as input_file:
	lines=input_file.readlines()
	lines.pop(0)

#output, eka rivi valmiiksi, toka argumentti
output_file = open(str(sys.argv[2]), "w")
output_file.write("legA legB hypotenuse\n")

#rivien splittaus
for line in lines:
	n1, n2 = line.split()
	output_file.write("%.2f " % toMeter(n1))
	output_file.write("%.2f " % toMeter(n2))
	output_file.write("%.4f" % laskePythagoras(toMeter(n1),toMeter(n2)))
	output_file.write("\n")

#suljetaa tiedostot
output_file.close()
