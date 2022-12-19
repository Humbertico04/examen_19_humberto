# PREGUNTA 3

# Si escribimos los dígitos de "60" como palabras en inglés, obtenemos "sixzero"; el número de letras en "sixzero" es siete. El número de letras en "siete" es cinco. El número de letras en "cinco" es cuatro. El número de letras en "cuatro" es cuatro: hemos alcanzado un equilibrio estable.
# Esto es correcto. Cuando escribimos "60" como palabras en inglés, obtenemos "sixzero", que tiene siete letras. El número de letras en "siete" es cinco, y el número de letras en "cinco" es cuatro. Por lo tanto, al escribir el número "60" como palabras en inglés y contando el número de letras de cada palabra resultante, eventualmente llegamos a un equilibrio en el que el número de letras es igual a cuatro.

 
# Nota: para números enteros mayores de 9, escriba los nombres de cada dígito en una sola palabra (en lugar del nombre propio del número en inglés). Por ejemplo, escribe 12 como "unodos" (en lugar de doce) y 999 como "nineninenine" (en lugar de novecientos noventa y nueve).

# Para cualquier número entero entre 0 y 999, devuelva una matriz que muestre la ruta desde ese número entero hasta un equilibrio estable:

# Ejemplos
# numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]

def numbersOfLetters(num):
    if num < 0 or num > 999:
        return "El número debe estar entre 0 y 999"
    num = str(num)
    for i in range(len(num)):
        if num[i] == "0":
            num = "zero" + num[i+1:]
        elif num[i] == "1":
            num = "one" + num[i+1:]
        elif num[i] == "2":
            num = "two" + num[i+1:]
        elif num[i] == "3":
            num = "three" + num[i+1:]
        elif num[i] == "4":
            num = "four" + num[i+1:]
        elif num[i] == "5":
            num = "five" + num[i+1:]
        elif num[i] == "6":
            num = "six" + num[i+1:]
        elif num[i] == "7":
            num = "seven" + num[i+1:]
        elif num[i] == "8":
            num = "eight" + num[i+1:]
        elif num[i] == "9":
            num = "nine" + num[i+1:]
    return num

print(numbersOfLetters(34))
num = str(10)
for i in range(len(num)):
    if num[i] == "0":
        nuevonum ="zero" + num[i+1:]
    elif num[i] == "1":
        nuevonum = "one" + num[i+1:]
print(nuevonum)