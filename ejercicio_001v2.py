#datos basicos
nombre = input("Hola,ingrese su nombre: ")
print("")
print ("Seleccione su tipo de Cliente: ")
print ("1. Normal")
print ("2. Frecuente")
print ("3. Premium") 

cliente = int(input("Opcion: "))

while cliente < 1 or cliente > 3:

    
    print("")
    print (" Tipo de Cliente Invalido")
    print(" Reintente")
    print("")
    print ("Seleccione su tipo de Cliente: ")
    print ("1. Normal")
    print ("2. Frecuente")
    print ("3. Premium")
    cliente = int(input("Opcion: "))

monto = float(input("Ingrese su monto de compra: "))

while monto <= 0:
    print("Monto invalido")
    
    monto = float(input("Ingrese su monto de compra nuevamente: "))

if cliente == 1:
    cliente = "Normal"
    if monto >= 50000:
        dcto = 0.05
    else:
        dcto = 0

elif cliente == 2:
    cliente = "Frecuente"
    if monto >= 40000:
        dcto = 0.1
    else:
        dcto = 0.03
    
elif cliente == 3:
    cliente = "Premium"
    if monto >= 30000:
        dcto = 0.15
    else:
        dcto= 0.07

dcto_compra = monto * dcto 
total = monto - dcto_compra

print ("Cliente: ", nombre)
print ("Tipo de Cliente: ", cliente)
print ("Descuento: ",dcto*100,"%")
print ("Total a pagar: ", total,"Pesos")


