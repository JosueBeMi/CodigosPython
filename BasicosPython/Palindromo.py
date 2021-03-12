def palindromo(palabra):
    #Reemplaza (replace) un caracter por otro
    palabra = palabra.replace(' ', '')
    #pone la palabras en minuscula (lower)
    palabra = palabra.lower()
    #invierte la palabra generada a partir de la oracion escrita
    palabra_invertida = palabra[::-1]
    #Se compara la palabra escrita contra la palabra invertida
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo ==True:
        print ("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()