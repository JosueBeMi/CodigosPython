# Conversor de pesos a dolares

# Definición de la función que convierte de pesos mexicanos a cualquier divisa
def conversor_mxn_divisa(divisa_mxn, divisa_ext):
    # Input de pesos mexicanos
    pesos_mexicanos = float (input ("Escribe la cantidad de pesos " + divisa_mxn + ": "))

    # Input del precio actual de la divisa
    divisa = float (input ("Escribe el precio actual del " + divisa_ext + ": "))

    #Cálculo de la conversión
    conversion_divisa = pesos_mexicanos/divisa
    conversion_divisa = round(conversion_divisa, 2)

    #Conversión para informar
    conversion_divisa = str(conversion_divisa)

    # Impresión de información en pantalla
    print ("Cuentas con: " + conversion_divisa + " de " + divisa_ext)

# Definición de la función que convierte de cualquier divisa a pesos mexicanos
def conversor_divisa_mxn(divisa_ext, divisa_mxn):
    # Input de pesos mexicanos
    divisa = float (input ("Escribe la cantidad de " + divisa_ext + ": "))

    # Input del precio actual de la divisa
    pesos_mexicanos = float (input ("Escribe el precio actual en pesos " + divisa_mxn + ": "))

    #Cálculo de la conversión
    conversion_divisa = pesos_mexicanos*divisa
    conversion_divisa = round(conversion_divisa, 2)

    #Conversión para informar
    conversion_divisa = str(conversion_divisa)

    # Impresión de información en pantalla
    print ("Cuentas con: " + conversion_divisa + " de pesos " + divisa_mxn)

# Creación del menú
menu = """
Bienvenido al Conversor de Pesos Mexicanos, selecciona una de las siguientes opciones: 💲

1 - Pesos Mexicanos a Dólares
2 - Pesos Mexicanos a Euros
3 - Pesos Mexicanos a Yennes
4 - Dólares a Pesos Mexicanos
5 - Euros a Pesos Mexicanos
6 - Yennes a Pesos Mexicanos

Selecciona una opcion: """

opcion = str (input (menu))

if (opcion == "1"):
    conversor_mxn_divisa("mexicanos", "dolar")

elif (opcion =="2"):
    conversor_mxn_divisa("mexicanos", "euro")

elif (opcion =="3"):
    conversor_mxn_divisa("mexicanos", "yenn")

elif (opcion =="4"):
    conversor_divisa_mxn("dólares", "mexicanos")

elif (opcion =="5"):
    conversor_divisa_mxn("euros", "mexicanos")

elif (opcion =="6"):
    conversor_divisa_mxn("yennes", "mexicanos")

else:
    print ("Selección incorrecta, selecciona una opción correcta, Gracias")
