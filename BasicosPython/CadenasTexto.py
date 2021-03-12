#Cadenas de texto

# Obtiene nombre y apellidos / uppercase (Pone en mayuscula) / strip (quita espacios)
nombre = input ("Escribe tu(s) nombres(s): ")
nombre_upper = nombre.upper()
nombre_strip = nombre_upper.strip()

ape_paterno = input ("Escribe tu apellido paterno: ")
ape_paterno_upper = ape_paterno.upper()
ape_paterno_strip = ape_paterno_upper.strip()

ape_materno = input ("Escribe tu apellido materno: ")
ape_materno_upper = ape_materno.upper()
ape_materno_strip = ape_materno_upper.strip()

#Obtiene nombre completo
nombre_completo = nombre_strip + " " + ape_paterno_strip + " " + ape_materno_strip

# Imprime el nombre completo
print ("El nombre completo es: " + nombre_completo)