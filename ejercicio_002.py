num1 = int(input("Ingrse el primer num: "))
num2 = int(input("Ingrese el segundo num: "))
num3 = int(input("Ingrese el tercer num: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1

elif num2 >= num1 and num2 >= num3:
    mayor = num2

else:
    mayor = num3

if num1 == num2 and num2 == num3:
    relacion = "Los 3 numeros son iguales"

elif num1 == num2 or num1 == num3 or num2 == num3:
    relacion = "Hay 2 numeros que son iguales"

else:
    relacion = "Los 3 numeros son diferentes"




   