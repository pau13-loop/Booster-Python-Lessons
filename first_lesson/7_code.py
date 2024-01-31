# Ejercicios CodeWars
# Sum The strings https://codewars.com/kata/5966e33c4e686b508700002d
# Remove las exclamation https://www.codewars.com/kata/57fae964d80daa229d000126
# Simple multiplication https://www.codewars.com/kata/583710ccaa6717322c000105
# Is it even? https://www.codewars.com/kata/555a67db74814aa4ee0001b5
# Even or Odd https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

# Ejemplo Ejercicio 1

def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"

    aInt = int(a) 
    bInt = int(b)

    print(str(aInt + bInt))
    return str(aInt + bInt)

sum_str("4","5") # 9
# sum_str("34","5") # 39

# Porque comprobamos si las variables a o b son iguales a una string vacia?

# if a == "":

#  Falla porque tratamos de convertir una string vacia a un integro y esta no puede ser convertida, 
# por esa razon si la variable a esta vacia le asignamos a la variable a una string, "0"
# y haremos lo mismo con la variable b en el caso de que tambien sea una string vacia
# y ahora si que podremos convertir la string "0" a un integro