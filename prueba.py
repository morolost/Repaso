import os
os.system("cls")
#1 imprimir en pantalla "hola mundo"

print("hola mundo")

#2 imprimir en pantalla "hola mundo" utilizando una palabra por argumento

print("hola", "mundo")

#3 imprimir en pantalla "hola mundo" concatenando 2 argumentos

print("hola" + "  " + "mundo")

#4 solicitar el nombre al usuario y realizar un saludo personalizado

nombre=input("poner nombre de usuario: ")
print("hola", nombre)

#5 solicitar la edad al usuario e informarle si es o no es mayor de edad

edad=int(input("poner edad: "))
if edad >= 18:
    print("soy mayor")
else:
    print("soy menor")

#6 crear un nuevo programa reutilizando algunos de los anteriores, para obtener la salida: hola, nombre. tienes x años.
#hola, nombre debe ser un argumento; y el punto que le sige no puede estar como cadena en ningun argumento

print("hola"+" "+nombre,"Tienes"+" "+str(edad)+" "+"años")

#7 de acuerdo a la edad ingresada, imprimir una cuenta regresiva hasta el 0

for i in range(edad,-1,-1):
    print(i)

#8 solicitar otro numero hasta que sea menor que la edad del usuario. luego imprimir los valores impares desde la edad hasta el ultimo numero ingresado.

numero=int(input("poner un numero: "))

while edad > numero:
    if numero / 2:
        print(numero)
    numero=int(input("poner otro numero: "))

#9 implementar en todos los ejercicios anteriores todas las funciones que sean necesarias.