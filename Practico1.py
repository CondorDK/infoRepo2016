#! /usr /bin/env python
# -*- coding: utf-8 -*-

nac = input ("ingrese su fecha de nacimiento:")
anio = input ("ingrese el año a calcular:")
edad = anio - nac
print "su edad en el anio: ", anio, "seria:", edad

#---------------------------------------------------

IVA = 0.21
precio = input ("ingrese un precio:")
total = precio + precio * IVA
print "el precio con IVA incluido es: ", total

#---------------------------------------------------

volumen = input ("ingrese el volumen:")
presion = input ("ingrese la presion:")
t = input ("ingrese la temperatura:")
masa = (presion * volumen) / (( 0.37 ) * (t + 460))
print " la masa es:","%.2f"% masa
	
#---------------------------------------------------

salario = input ("ingrese el salario anterior:")
inc = 0.25
salario = salario + salario*inc
print "su nuevo salario es: $", salario

#---------------------------------------------------

var1 = input ("ingrese un presupuesto: ")
odon = 40 % 100
trau = 30 % 100
pedia = 30 % 100
print "para odontologia se destina:", (var1 * odon)
print "para traumatologia se destina:", (var1 * trau)
print "para pediatria se destina:", (var1 * pedia)

#-----------------------------------------------------

var1 = input ("ingrese el precio del articulo: $")
porc = 0.3 * var1
Total = var1 + porc
print "la ganancia que obtubo es de: $", porc, "\nSi vende el articulo a: $", Total

#------------------------------------------------------

per1 = input ("ingrese el dinero que desea invertir: $")
per2 = input ("ingrese el dinero que desea invertir: $")
per3 = input ("ingrese el dinero que desea invertir: $")
Total = per1 + per2 + per3
porc1 = per1 * 100 / Total
porc2 = per2 * 100 / Total
porc3 = per3 * 100 / Total
print "El Total invertido: $", Total
print "Eduardo invirtio un: ", porc1,"%"
print "Julio invirtio un: ", porc2,"%"
print "Augusto invirtio un: ", porc3,"%"

#-------------------------------------------------------

print "---------MATEMATICAS-----------"
mateExamen = input ("ingrese nota del examen de Matematicas:" )
mateTar1 = input ("ingrese nota de la primera tarea de Matematicas:" )
mateTar2 = input ("ingrese nota de la segunda tarea de Matematicas:" )
mateTar3 = input ("ingrese nota de la tercera tarea de Matematicas:" )
mateTareas = (mateTar1 + mateTar2 + mateTar3) / 3
mate = mateExamen * 0.9 + mateTareas * 0.1
print "Su Promedio en Matematicas es de :", mate

print "---------FISICA-----------"
fisiExamen = input ("ingrese nota del examen de Fisica:" )
fisiTar1 = input ("ingrese nota de la primera tarea de fisica:" )
fisiTar2 = input ("ingrese nota de la segunda tarea de fisica:" )
fisiTareas = (fisiTar1 + fisiTar2) / 2
fisi = fisiExamen * 0.8 + fisiTareas * 0.2
print "Su Promedio en Fisica es de :", fisi

print "---------QUIMICA-----------"
quimExamen = input ("ingrese nota del examen de Quimica:" )
quimTar1 = input ("ingrese nota de la primera tarea de Quimica:" )
quimTar2 = input ("ingrese nota de la segunda tarea de Quimica:" )
quimTar3 = input ("ingrese nota de la tercera tarea de Quimica:" )
quimTareas = (quimTar1 + quimTar2 + quimTar3) / 3
quimi = quimExamen * 0.85 + quimTareas * 0.15
print "Su Promedio de Quimica es de :", quimi

print "---------PROMEDIO GENERAL-----------"
print "Su Promedio General es de:","%.2f"% ((mate + fisi + quimi) / 3)