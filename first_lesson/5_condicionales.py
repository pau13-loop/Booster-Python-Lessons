#  Ejemplo mediante leguaje natural de un condicional:

# Maria es una mujer --> Variable
# Maria tiene el pelo marron --> Variable

# Si maria tiene el pelo marron entonces:
#    Maria es morena.
#    Si Maria es morena entonces:
#        Maria me gusta.
#        Si Maria me gusta entonces:
#           Tengo verguenza.
# Maria es rubia.

# Condicional en Python

# if <condicion>:
#    <instruccion>
# else:
#    <instruccion>

genero_maria = "hombre"
color_pelo_maria = 'marron' # "rubio"


if color_pelo_maria == "marron":
    print("Maria es morena.")
    if genero_maria == "mujer":
        print("Maria me gusta.")
        if color_pelo_maria == "marron":
            print("Tengo verguenza.")
else:
    print("Maria tiene otro color de.")