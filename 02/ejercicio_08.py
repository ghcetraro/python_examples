#!/usr/bin/python3

#capturo datos del teclado
numero1 = input("Ingrese el primer numero : ")
numero2 = input("Ingrese el segundo numero : ")

#convierto de texto a numerico
numero1 = int(numero1)
numero2 = int(numero2)

#hago los calculos
cociente = numero1 // numero2
resto = numero1 % numero2

#muestro por pantalla
print( str(numero1) + " entre "  + str(numero2) + " da un cociente " +  str(cociente) + " y un resto "  + str(resto))
