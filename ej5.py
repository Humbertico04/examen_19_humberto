# PREGUNTA 5

# Cree una función hollow_triangle(altura) que devuelva un triángulo hueco de la altura correcta. La altura se pasa a través de la función y la función debe devolver una lista que contiene cada línea del triángulo hueco.

# hollow_triangle(6)

#  should return : ['_____#_____', '____#_#____', '___#___#___', '__#_____#__', '_#_______#_', '###########']

# hollow_triangle(9)

#  should return : ['________#________', '_______#_#_______', '______#___#______', '_____#_____#_____', '____#_______#____', '___#_________#___', '__#___________#__', '_#_____________#_', '#################']

 

# La idea final es que el triángulo hueco se vea así si decides imprimir cada elemento de la lista:

# hollow_triangle(6)

# will result in:

# _____#_____              1

# ____#_#____              2

# ___#___#___              3

# __#_____#__              4

# _#_______#_              5

# ###########              6

# ---- Final Height

 

# hollow_triangle(9)

# will result in:

# ________#________        1

# _______#_#_______        2

# ______#___#______        3

# _____#_____#_____        4     

# ____#_______#____        5

# ___#_________#___        6

# __#___________#__        7

# _#_____________#_        8

# #################        9

# ---- Final Height

# Rellene los espacios con guiones bajos, es decir, _ para que cada línea tenga la misma longitud. ¡Buena suerte y diviértase codificando!

def hollow_triangle(n):
    # Loop through each row of the pyramid
    for i in range(n):
    # Print the required number of spaces before the # symbols
        print("_" * (n - i - 1), end="")
    # Print the required number of # symbols
        print("# ", end="")
        print("_" * (i + 2), end="")
        print("# ", end="")
        print("_" * (n - i - 1))

hollow_triangle(15)
