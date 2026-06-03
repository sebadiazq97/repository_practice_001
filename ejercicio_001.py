cliente = input("- Hola, ingrese su nombre: ")
tipo_cliente = int(input("- Ingrese su tipo de cliente: 1.Normal / 2.Frecuente / 3.Premium: "))
monto_compra = float(input("- Ingrese su monto de compra: "))

if tipo_cliente == 1:
    tipo_cliente = "Normal"
    if monto_compra >= 50000:
        descuento = 0.05
    else:
        descuento = 0

elif tipo_cliente == 2:
    tipo_cliente = "Frecuente"
    if monto_compra >= 40000:
        descuento = 0.1
    else:
        descuento = 0.03

elif tipo_cliente == 3:
    tipo_cliente = "Premium"
    if monto_compra >= 30000:
        descuento = 0.15
    else:
        descuento = 0.07

    
else:
    tipo_cliente = "Cliente Invalido"
    descuento = 0

descuento_compra = monto_compra * descuento
total = monto_compra - descuento_compra

print ("Cliente: ",cliente)
print ("Tipo de Cliente: ",tipo_cliente)
print ("Descuento: ",descuento*100,"%")
print ("Total a pagar", total, "Pesos")