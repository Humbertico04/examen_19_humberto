# PREGUNTA 6

# El Rey y la Reina de FarFarAway van a visitar a Shrek y Fiona en su pantano. Sin embargo, Shrek tiene miedo de que Burro vuelva a hacer travesuras, por lo que decide atarlo para que no moleste en la cena real. Shrek cultiva un parche circular de hierba deliciosa y decide atar a Burro a un poste de la cerca en su borde. Sin embargo, teme que cuando Burro tenga hambre, se coma toda la hierba, y Shrek necesita la hierba para preparar un plato de sabrosa ensalada de hierba de ogro para la cena. La cuerda debe ser corta para que el burro no pueda comer (o, peor aún, fertilizar) demasiada hierba.



# Shrek puede resolver este problema de varias maneras. Una opción sería colocar una cuerda larga y suficientemente resistente en el poste y enlazarla a un collar o una correa que se coloque alrededor del cuello de Burro. De esta manera, Shrek podrá controlar la distancia que Burro puede recorrer y asegurarse de que no se acerque demasiado a la hierba deliciosa.

# Otra opción sería colocar una cerca alrededor del parche circular de hierba y asegurarse de que Burro no pueda acceder a él. De esta manera, Shrek podrá proteger su preciada hierba y asegurarse de que esté disponible para la cena.

# En cualquier caso, es importante que Shrek sea cuidadoso y no permita que Burro se acerque demasiado a la hierba, ya que de lo contrario podría terminar comiéndola o causando daños en el parche. Además, es crucial que Shrek mantenga una buena comunicación con Burro y le haga entender que su comportamiento no es aceptable, para evitar que vuelva a suceder en el futuro.

 

# Dado el diámetro del parche circular de pasto (medido en pasos de ogro), calcule la longitud máxima de la cuerda para que Burro no pueda comer más del porcentaje de pasto dado (dado como proporción en el rango 0 <= percentage <= 1, es decir, 0.5significa 50%). Como Shrek es solo un ogro y no está muy familiarizado con las fracciones, la longitud debe devolverse como pasos de ogro enteros. 

# Para resolver este problema, primero necesitamos calcular el área del parche circular de hierba. Luego, podemos calcular la longitud de la cuerda necesaria para que Burro no pueda acceder a más del porcentaje dado de esa área.

# El área de un círculo se puede calcular usando la fórmula:

# Área = pi * radio^2

# Dado que el diámetro del parche circular de hierba se nos da en pasos de ogro, podemos calcular el radio en pasos de ogro usando la fórmula:

# radio = diámetro / 2

# Una vez que tenemos el radio, podemos calcular el área del parche circular de hierba:

# Área = pi * radio^2 = pi * (diámetro / 2)^2

# Ahora que sabemos el área del parche circular de hierba, podemos calcular la longitud máxima de la cuerda necesaria para que Burro no pueda acceder a más del porcentaje dado de esa área. Para hacerlo, primero necesitamos calcular el área que queremos proteger. Podemos hacerlo multiplicando el área total del parche por el porcentaje dado:

# Área protegida = Área total * porcentaje dado

# La longitud máxima de la cuerda necesaria para proteger esa área será la circunferencia del círculo que tiene esa área. La fórmula para calcular la circunferencia de un círculo es:

# Circunferencia = 2 * pi * radio

# Cuidado: en Fairy Land, ¡los parches de hierba pueden crecer mucho!

def max_cord_length(diametro, porcentage):
    # Calcular el área del parche circular de hierba en pasos de ogro cuadrados
    area = (diametro / 2)**2 * 3.14
  
    # Calcular el área que queremos proteger en pasos de ogro cuadrados
    protegido = area * porcentage
  
    # Calcular la longitud máxima de la cuerda en pasos de ogro
    cuerda = 2 * (protegido * 3.14)**0.5
  
    # Devolver la longitud máxima de la cuerda como un entero
    return int(cuerda)
  
print(max_cord_length(23, 0.5))
