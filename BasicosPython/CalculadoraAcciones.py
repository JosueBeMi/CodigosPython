# Calculadora de Acciones
print ("Bienvenido a la calculadora de acciones:")

# Input del precio por acción y cantidad de acciones a comprar
precio_x_accion = float(input("Escribe el precio que vale la acción: "))
cantidad = int(input("Escribe el numero de acciones a comprar: "))
# Obtener comisión
comision = (.25/100)
# Obtener IVA del 0.16%
iva = (comision*.16)

# Bloque de cálculos
comision_x_accion = (comision*precio_x_accion)
totalaccion = (iva+comision_x_accion+precio_x_accion)*cantidad
totalaccion = round(totalaccion, 2)

# Conversión a cadenas para informar
precio_x_accion = str(precio_x_accion)
cantidad = str(cantidad)
totalaccion =str(totalaccion)

# Impresiones a pantalla del resultado de las transacciones
print ("***************************")
print ("Resumen de la transaccion: ")

print ("Precio por accion: "+ precio_x_accion)
print ("Total de acciones a comprar: "+ cantidad)
print ("Costo total de la transaccion: "+ totalaccion)
