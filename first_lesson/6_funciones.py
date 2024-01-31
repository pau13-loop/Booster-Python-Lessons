# Funciones

# Para definir una funcion se usa la palabra reservada def
# def 

# Qué quiere decir palabra reservada?

# Al igual que print, if, else, etc. def es una palabra reservada de Python. 
# Esto quiere decir que no podemos usar def como nombre de variable,
# ya que Python lo tiene reservado para definir funciones.

pelo_maria = "marron" # "rubio"
genero_maria = "mujer"

# Declaracion de una funcion 

# Que quiere decir declarar una funcion?

# Declarar una funcion es definir una funcion.
# En este caso, estamos definiendo una funcion llamada my_function
# que no recibe ningun parametro.

def my_function():
    if pelo_maria == "marron":
        print("Maria es morena.")
        if genero_maria == "mujer":
            print("Maria es una mujer")
    else:
        print("Maria no tiene el color de pelo marron")

# Llamada a la funcion
my_function()

# Que quiere decir llamar a una funcion?

# Llamar a una funcion es ejecutar el codigo que hay dentro de la funcion.
# En este caso, cuando llamamos a my_function() estamos ejecutando el codigo
# que hay dentro de la funcion.


# Ejemplo de funcion con parametros

def my_function_con_pase_parametros(genero, color_pelo):
    if color_pelo == 'marron':
        print("Esta persona es morena.")
        if genero == "mujer":
            print("Esta persona es una mujer.")
    else:
        print("Esta persona no tiene el color de pelo marron.")

my_function_con_pase_parametros('hombre', 'rubia')
# my_function_con_pase_parametros('mujer', 'rubia')


# Ejemplo de funcion con parametros y retorno de valor

def my_function_con_pase_parametros_y_retorno(genero):
    if genero == "mujer":
        print("Esta persona es una mujer.")
        return True
    else:
        print("Esta persona no es una mujer.")
        return False

# Llamada a la funcion
my_function_con_pase_parametros_y_retorno('hombre')



# Porque queremos pasar parametros a una funcion?

# Queremos pasar parametros a una funcion para poder reutilizar el codigo
# que hay dentro de la funcion. En el ejemplo anterior, hemos definido una
# funcion que nos dice si una persona es mujer o no. Si no pasamos parametros
# a la funcion, la funcion siempre nos va a decir que la persona no es una mujer.

# Porque queremos retornar un valor en una funcion?

# Queremos retornar un valor en una funcion para poder reutilizar el valor
# que retorna la funcion. En el ejemplo anterior, hemos definido una funcion
# que nos dice si una persona es mujer o no. Si no retornamos un valor en la
# funcion, no podremos usar el valor que retorna la funcion.

