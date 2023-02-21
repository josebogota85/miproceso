#AND este operador lógico se traduce como y, cuando los dos datos son verdadores, el resultado final es verdadero, por el conotrario y si uno de los datos es falso, o los dos datos son falson, entonces el resultado final es falso.


#Podemos usar un ejemplo con números
print(10>5 and 5<10)# como las condiones son las dos verdaderas entonces el resultado es True
print(10<5 and 5>10)# En este ejemplo el resultado será falso debido a que las dos condiciones son falsas

#Acá haremos un ejemplo practico de con un inventario
inventario=int(input("Ingrese el número del producto: "))
print(inventario>= 100 and inventario <= 1000)

print("_"*100)#Esto es un serparador


#En el caso del operador lógico or las condiciones para que sea verdadero son diferentes, por emeplo acá basta con que una de las condiciones sea verdadera, para que la sentendica total sea verdadera, ejemplo
print("Operador lógico or")
print("Verdadero o verdadero => ", True or True)
print("Verdadero o falso => ", True or False)
print("Falso o verdadero => ", False or True)
print("False o False => ", False or False)

print(10>5 or 5==10)# como las condiones son las dos verdaderas entonces el resultado es True
print(10<5 or 5>10)# En este ejemplo el resultado será falso debido a que las dos condiciones son falsas

role=input('Digita el rol: ')
print(role=='admin' or role=='seller')


