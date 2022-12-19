def numberToWord(n):
  # Crear un diccionario que mapee cada número con su nombre en inglés
  numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
  }
  return numbers[n]

def numbersOfLetters(n):
    # Convertir el número a una lista de dígitos
    digits= []
    for i in str(n):
        digits[i] = int(i)

  # Escribir cada dígito como palabras en inglés y agregarlo a la lista
    result = []
    for i in digits:
        result.append(numberToWord(i))

  # Iterar hasta que la longitud de la lista sea 4
    while len(result) != 4:
    # Sumar el número de letras de cada elemento de la lista
        total = 0
        for word in result:
            total += len(word)

    # Escribir el resultado como palabras en inglés y agregarlo a la lista
    result.append(numberToWord(total))

    return result



print(numbersOfLetters(60))
