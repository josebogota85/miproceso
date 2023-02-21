#Para comparar lo números decimales o flotantes debemos tener en cuenta el numero de decimales que hay después del punto ya que pueden ser diferentes.
x=3.3
print(x)
y=1.1 + 2.2
print(y)
print(x==y)

#Para arreglar los decimales de un numero se puede hacer de dos maneras, se le puede dar formato usando la función format, como el siguiente ejemplo, pero ojo esto lo deja en formato string

y_formato_string=format(y,"2g")
print('string => ', y_formato_string)
print(y_formato_string==str(x))

print("_"*20)#Esto se usa como un separador

#Tambíen se puede dar formato al núnmero decimal de una forma más matématica, para no tener que cambiar el formato entero del nuúmero, para usar esta forma matemática es necesario definir una tolerancia, ojo al ejemplo

tolerancia_diferencia=0.00001
print(abs(x-y)<tolerancia_diferencia)
