name="Jose"
last_name="Rincón Ortiz"
print(name)
print(last_name)
full_name=name+last_name
print(full_name)
full_name=name+ " " +last_name
print(full_name)

quote="I'am Jose Luis Rincon."
print(quote)


#Format, se puede dar formato a los estring usando variables con concatenación

template="Hola mi nombre es: " + name + " y mi apellido es: " + last_name
print("V1", template)

#Con la función .format podemos incluir un texto usando llaves {} dentro del string
template="Hola mi nombre es: {} y mi apeliido es: {}".format(name, last_name)
print("V2", template)

#Otra forma de darle formato al texto es usando una f justo antesd e las comillas del string, luego en el sitio que quiero colocar las variables uso {} con el nombre de la variable dentro 

template= f"Hola mi nombre es: {name} y mi apellido es: {last_name}"
print("V3", template)

