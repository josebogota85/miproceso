#string es un tipo de dato que es una cadena de texto, se puede usar comillas dobles y comillas sencillas
my_name="Jose"
my_name='Jose'
ejemplo='escrito por "jose rincon"'
print(ejemplo)
print('my_name=>', my_name)
print(type(my_name))

#Entero es un tipo de dato que guarda un numero, no hay que usar comillas solo el número
my_age=37
print("my age=>",my_age)
print(type(my_age))

#Boleanos es un tipo de dato que solo puede tener dos valores True o False
is_single=True
print("is single=> ", is_single)
print(type(is_single))


#Input, los inputs reciben cualquier dato, pero al recibirlo por consola lo convierten automaticamente en un texto

my_age=input("¿Cuál es tu edad?")
my_age=int(my_age)
print(type(my_age))