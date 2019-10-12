#!/usr/bin/python3

contrasena="12345678"

#capturo datos del teclado
contra = input("Ingrese su contraseña : ")

contra= contra.lower()

if contra == contrasena :
	print( "Es correcta" )
else:
	print( "Es incorrecta" )

