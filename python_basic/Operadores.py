#Operadores aritmética#

print(1 + 9)
print(5 - 1)
print(2 * 6)
print(4 / 2)
print(10 % 2)
print(20 // 5)
print(2 ** 2)
print(2 ** 4 + 2 - 1 / 1 // 2)


#Cadenas de texto#

print("Hola " + "Que " + "Tal " + "Estas")
print("Hola " + str(5))

#Operacion Mixtas#
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores comparativos #

print(3 > 4)
print(5 > 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Comparaciones cadenas de texto #
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")


# Álgebra de Boole #
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))