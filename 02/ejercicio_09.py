#!/usr/bin/python3

#capturo datos del teclado
inversion = int(input("Iversion : "))
interes = int(input("Interes : "))
anos = int(input("Años : "))

result = inversion * ( ( 1 + ( interes / 100 ) ) **anos )

print( result )
