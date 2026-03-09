def run_benchmark(funcion_datos, funcion_sort, imprimir_t=False):
    """
    Usa timeit para calcular los tiempos promedio de ejecución para una lista de valores de n.

    funcion_datos es una función que regresa una lista de datos según el caso (mejor, peor, promedio).
    funcion_sort es la función de ordenamiento a usarse en el benchmark.
    """
    from timeit import timeit

    escala = [10, 50, 100, 200, 500, 800, 1000, 1500, 1800, 2000]
    tiempos = []
    
    factor_repeticion = 50

    for n in escala:
        datos_prueba = funcion_datos(n)
        
        tiempo_total = timeit(
            stmt=lambda: funcion_sort(datos_prueba), 
            number=factor_repeticion,
            globals=globals()
        )
        
        t_promedio = tiempo_total / factor_repeticion

        tiempos.append(t_promedio)
    
    if imprimir_t:
        print(f"{'Tamaño (n)':<10} | {'Tiempo promedio (s)':<20}")
        print("-" * 40)

        for n, t in zip(escala, tiempos):
            print(f"{n:<10} | {t:<20.6f}")

    return tiempos

def lista_aleatoria(n):
    """
    Regresa una lista de longitud n de enteros aleatorios
    entre 1 y 1000
    """
    from random import randint
    return [randint(1, 1000) for _ in range(n)]

def lista_ordenada_inv(n):
    """
    Regresa una lista descendiente (-1) de longitud n
    """
    return list(range(n, 0, -1))

def lista_ordenada(n):
    """
    Regresa una lista ascendiente (+1) de longitud n
    """
    return list(range(0, n, 1))