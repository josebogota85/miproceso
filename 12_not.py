#el not sirve para negar una premisa, generalmente se usan con boleanos, sigamos el ejemplo
print(not True)#Mostraría False
print(not False)#Mostraría True

#Podemos usar también not en la practican de la siguiente manera
print("Operador lógico NOT AND")
print("Verdadero y verdadero => ", not(True and True))
print("Verdadero y falso => ", not(True and False))
print("Falso y verdadero => ", not (False and True))
print("False y False => ", not (False and False))

#Ejemplo practico con not and
inventario=int(input("Ingrese el número del producto: "))
print(not(inventario>= 100 and inventario <= 1000))
