## Strings ##

primera_palabra = "Hola"
segunda_palabra = "Que tal"

print(len(primera_palabra))
print(len(segunda_palabra))
print(primera_palabra + " " + segunda_palabra)

nueva_frase = "Esta es una frase\ncon salto de linea"
print(nueva_frase)

tab_frase = "\tEste es una frase con tabulación"
print(tab_frase)

scape_frase = "\\tEste es una frase \\n escapado"
print(scape_frase)

## Formateo ##

nombre, apellido, anios = "Bryan", "Caguana", 20
print("Mi nombre es {} {} y mi edad es {}". format(nombre, apellido, anios))
print("Mi nombre es %s %s y mi edad es %d" % (nombre, apellido, anios))
print("Mi nombre es " + nombre + " " + apellido + "y mi edad es" + str(anios))
print(f"Mi nombre es {nombre} {apellido} y mi edad es {anios}")

## Desempaqueado de caracteres##

language = "bryan"
a, b, c, d, e = language #Guarda cada letra en un array#
print(a)
print(e)

## Division ##

Imprimir = language[0:6:2]
print(Imprimir)

## Reverse ##

reversed_language = language[::-1]
print(reversed_language) #Muestra la palabra revertida#

## Funciones del lenguaje##

print(language.capitalize()) #Monstrar la primera palabra en Mayúsculas#
print(language.upper()) # Mosntrar toda la palabra en mayúsculas#
print(language.count("B")) # Contar cuantas palabras hay de las indicadas#
print(language.isnumeric()) # Indica si la palabra es un número#
print("1".isnumeric()) # Indica si el dato es un número#
print(language.lower()) # Muestra la palabra entera en minúsculas#
print(language.lower().isupper()) # Indica si la palabra en minusculas es mayúsculas#
