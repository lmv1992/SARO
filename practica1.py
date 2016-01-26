#!/usr/bin/python
print "\nTABLA DE MULTIPLICAR"


for N1 in range(1,11):
	print "\n" + "tabla del "+str(N1) + "\n"
	for N2 in range(1,11):
		print str(N1) + " * " + str(N2) + " igual = " + str(int(N1)*int(N2)) 

#C1 = 1
#while C1 < 11:
#	print "Tabla del " + str(C1)
#	C2 = 1 
#	while C2 <11:
#		print str(C1) + " * " + str(C2) + " = " + str(int(C1*C2))
#		C2 = C2+1 
#	C1 = C1+1		
