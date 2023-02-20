name="Jose"
print(type(name))
name=12
print(type(name))
name=True
print(type(name))

#Tenngo que tener en cuenta que si no tenemos los mismos tipos de datos en ocaciones habrán operaciones que no se podrán hacer.

"""
print("Jose"+ 27)
este código va a generar un error debido a que no es posible concatenar un número con un strin
"""

#En este ejemplo si vamos a poder ejecutar el programa por que los datos son de la misma naturaleza

print("jose "+"Rincon")
print(10+20)
#En este último caso se cambio el formato del número para que se pueda concatenar con el dato de string
print("Jose"+ " 37")

age=37
#De esta forma podemos citar un dato en string, que esta dentro de una variable, sin que cambie su valor 
print("Mi edad es: "+ str(age))
# También podemos usar el f antes de las comillas del string para cambiar el formato a la variable por string automáticamente.
print(f"Mi edad es: {age}")

#También puedo transformar el valor de un input, debido a que este viene siempre en formato string
age=int(input("Calcula cuantos años tendrás en 13 años, ingresa tu edad: "))
age+=13
print(f"Tu edad en 13 años sera:  {age}")




