print "SITUACION 1"

var = input ("ingrese valor")
if (var % 2) == 0:
	print "el valor ingresado es par"

#--------------------------------------

var1 = input ("ingrese un valor")
var2 = input ("ingrese un valor")
var3 = input ("ingrese un valor")
prom = (var1 + var2 + var3) / 3
if var1 >= prom:
	if var1 == prom:
		print ("el valor uno es igual al promedio")
	else: 
		print ("el valor uno es mayor al promedio")
if var2 >= prom:
	if var2 == prom:
		print ("el valor dos es igual al promedio")
	else: 
		print ("el valor dos es mayor al promedio")
if var3 >= prom:
	if var3 == prom:
		print ("el valor tres es igual al promedio")
	else: 
		print ("el valor tres es mayor al promedio")

#----------------------------------------------------

valor1 = input ("ingrese un valor: ")
valor2 = input ("ingrese un valor: ")
valor3 = input ("ingrese un valor: ")
if valor1 < valor2 and valor1 < valor3:
	print valor1
	if valor2 < valor3:
		print valor2
		print valor3
	else:
		print valor3
		print valor2
elif valor2 < valor1 and valor2 < valor3:
	print valor2
	if valor1 < valor3:
		print valor1
		print valor3
	else:
		print valor3
		print valor1
else:
	print valor3
	if valor1 < valor2:
		print valor1
		print valor2
	else:
		print valor2
		print valor1

#-----------------------------------------------------

print "Situacion 4"
print "--------------------------"
impTotal = input (" ingrese impuesto total" )
impApli = input ("ingrese impuesto aplicados")
imN = impTotal - impApli
if (impApli > impTotal):
	print " el impuesto aplicado no puede ser mayor que el impuesto total :"
imN = impTotal - impApli
if (imN == 0):
	print "Su Importe es 0"
if (imN > 0 and impTotal > 5000):
	print "Monto Superado para Consumidor Final :"
	print imN

print "Situacion 5"
print "Clasificacion de Personas segun la edad"
print "--------------------------"
edad input ("Ingrese su edad :")
aniosE = input ("Ingrese los anio")
if (edad >= 60 and aniosE <25):
	print ("Usted esta en la categoria de jubilacion por edad :")
elif( edad < 60 and aniosE >= 25):
	print ("Usted esta en la categoria de Antiguedad Joven :")
elif( edad >=60 and aniosE >=25):
	print "Usted esta en la categoria de Antiguedad Adulta "
else:
	print " Usted no esta incluido en ninguna categoria"

print "Situacion 6"
print "--------------------------"
num = input ("introduce un anio para saber si es bisiesto: ")
if num % 400 == 0 and num % 4 == 0:
	print num, "es bisiesto, porque es mulstiplo de 400"
elif num % 100 == 0 and num % 4 == 0 and anio % 400!= 0:
	print num, "no es bisiesto porque es multiplo de 4 y 100 pero no de 400"
elif num % 4 == 0 and num % 100!= 0:
	print num, "es bisiesto porque es multiplo de 4"
else:
	print num, "no es bisiesto porque no es multiplo de 4 ni de 400"

#----------------------------------------------------------------------
import math
print "Situacion 7"
print "--------------------------"
print "Calculo de areas - Elija una figura geometrica"
print "a) Triangulo"
print "b) Circulo"
print ""
x = raw_input ("Que figura quiere calcular (Escriba T o C)? ")
if x == "T" or x == "t":
	base = float(input ("Escriba la base: "))
	altura = float(input ("Escriba la altura: "))
	area = altura * base / 2
	print "Un triangulo de base", base, "y altura", altura, "tiene un area de", area
elif x == "C" or x == "c":
	radio = input ("Escriba el radio: ")
	area = math.pi * (radio * radio)
	print "Un circulo de radio", radio, "tiene un area de", area
else:
	print "Opcion incorrecta, vuelva a intentarlo"
	print ""


print "Situacion 11"
print "Pago de Sueldo"
print "--------------------------"
res = raw_input ("El empleado asistio todo el mes al trabajo ? Responda con S o N ")
if (res == "S"):
	horaD = (" El empleado cuantas horas trabajo el domingo ")
 	if (horaD >= 3 and horaD <= 5):
		print " El empleado tendra un adicional del 3% "
	elif(horaD >= 6 and horaD <=10):
		print " El empleado tendra un adicional del 10% "
	else:
		print (" El empleado no cuenta con un aumento adicional a su sueldo ")
elif (res == "N"):
	horaD = (" El empleado cuantas horas trabajo el domingo ")
	if (horaD >= 3 and horaD <= 10):
		print (" El empleado tendra un adicional del 2% ")
	else:
		print " El empleado no cuenta con un aumento adicional a su sueldo "
