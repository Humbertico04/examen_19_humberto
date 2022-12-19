# PREGUNTA 3

# Si escribimos los dígitos de "60" como palabras en inglés, obtenemos "sixzero"; el número de letras en "sixzero" es siete. El número de letras en "siete" es cinco. El número de letras en "cinco" es cuatro. El número de letras en "cuatro" es cuatro: hemos alcanzado un equilibrio estable.
# Esto es correcto. Cuando escribimos "60" como palabras en inglés, obtenemos "sixzero", que tiene siete letras. El número de letras en "siete" es cinco, y el número de letras en "cinco" es cuatro. Por lo tanto, al escribir el número "60" como palabras en inglés y contando el número de letras de cada palabra resultante, eventualmente llegamos a un equilibrio en el que el número de letras es igual a cuatro.

 
# Nota: para números enteros mayores de 9, escriba los nombres de cada dígito en una sola palabra (en lugar del nombre propio del número en inglés). Por ejemplo, escribe 12 como "unodos" (en lugar de doce) y 999 como "nineninenine" (en lugar de novecientos noventa y nueve).

# Para cualquier número entero entre 0 y 999, devuelva una matriz que muestre la ruta desde ese número entero hasta un equilibrio estable:

# Ejemplos
# numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]

from ast import main

def numbersOfLetters(n):
  # Convertimos el número a su representación en palabras en inglés
  num_as_words = convertToWords(n)

  # Si el número de letras es igual a cuatro, devolvemos la matriz con la ruta desde el número original hasta el equilibrio estable
  if num_as_words == "four":
    return [num_as_words]

  # Si el número de letras no es igual a cuatro, llamamos recursivamente a la función con el número de letras como argumento y agregamos el resultado a la matriz de resultados
  else:
    return [num_as_words] + numbersOfLetters(len(num_as_words))

def convertToWords(n):
  # Si el número es cero, devolvemos "zero"
  if n == 0:
    return "zero"

  # Si el número es menor que diez, devolvemos el nombre del número
  if n < 10:
    return {
      1: "one",
      2: "two",
      3: "three",
      4: "four",
      5: "five",
      6: "six",
      7: "seven",
      8: "eight",
      9: "nine",
    }[n]

  # Si el número es mayor o igual a diez, escribimos cada dígito como palabras en inglés y los unimos
  digits = []
  while n > 0:
    digit = n % 10
    digits.append(convertToWords(digit))
    n = n // 10

  # Invertimos la lista de dígitos para obtener el número en el orden correcto
  digits = digits[::-1]

  # Unimos los dígitos
  return "".join(digits)

print(numbersOfLetters(60))

if __name__ == "__main__":
  main()