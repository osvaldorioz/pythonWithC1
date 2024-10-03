import random

def generar_lista_flotantes_aleatorios(tamano, minimo, maximo):
    """
    Genera una lista de números flotantes aleatorios.

    Parámetros:
    tamano (int): Número de elementos en la lista.
    minimo (float): Valor mínimo para los números aleatorios.
    maximo (float): Valor máximo para los números aleatorios.

    Retorna:
    list: Lista de números flotantes aleatorios.
    """
    return [random.uniform(minimo, maximo) for _ in range(tamano)]

# Ejemplo de uso
tamano_lista = random.randint(5, 100)
minimo = 1.0
maximo = 1000.0

lista_aleatoria = generar_lista_flotantes_aleatorios(tamano_lista, minimo, maximo)
print(lista_aleatoria)

