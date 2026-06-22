ESCALA_LINEAL_LOG = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000]
ESCALA_CUADRATICA = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
ESCALA_CUBICA = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
ESCALA_RECURSIVA = [100, 200, 300, 400, 500, 600, 700, 800, 900, 950] # Evita el limite de recursion 1000
ESCALA_FACTORIAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def run_benchmark(funcion_datos, algoritmo, escala, imprimir_t=False):
    """
    Usa timeit para calcular los tiempos promedio de ejecución para una lista de valores de n.

    funcion_datos: Funcion que genera los datos (la lista de números)
    algoritmo: Algoritmo que se va a utilizar en la prueba
    """
    from timeit import timeit

    tiempos = []
    
    if escala == ESCALA_LINEAL_LOG:
        factor_repeticion = 1000
    elif escala == ESCALA_RECURSIVA:
        factor_repeticion = 1000
    elif escala == ESCALA_CUADRATICA:
        factor_repeticion = 50
    elif escala == ESCALA_CUBICA:
        factor_repeticion = 5
    elif escala == ESCALA_FACTORIAL:
        factor_repeticion = 1
    else:
        factor_repeticion = 50

    for n in escala:
        args = funcion_datos(n)
        
        tiempo_total = timeit(
            stmt=lambda: algoritmo(*args), 
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

# GENERADORES DE DATOS #
from random import randint
def datos_arreglo_1d(n):
    """
    Para sum(a, n) y r_sum(a, n)
    """
    
    # Se agrega [0] para alinear con índice 1
    a = [0] + [randint(1, 1000) for _ in range(n)]
    
    return (a, n)

def datos_matrices_add(n):
    """
    Para add(a, b, c, m, n)
    Asume matrices cuadradas m=n para la prueba
    """

    a = [[randint(1, 100) for _ in range(n+1)] for _ in range(n+1)]
    
    b = [[randint(1, 100) for _ in range(n+1)] for _ in range(n+1)]
    
    c = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    return (a, b, c, n, n)

def datos_matriz_trasp(n):
    """
    Para trasp(a, n)
    """

    a = [[randint(1, 100) for _ in range(n+1)] for _ in range(n+1)]
    
    return (a, n)

def datos_matrices_mult_rectangular(n):
    """
    Para mult(a, b, c, m, n, p) versión 1
    NOTA: m = n = p
    """
    # Matriz a, n * n
    a = [[randint(1, 100) for _ in range(n+1)] for _ in range(n+1)]
    
    # Matriz b, n * n
    b = [[randint(1, 100) for _ in range(n+1)] for _ in range(n+1)]
    
    # Matriz c, n * n
    c = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    return (a, b, c, n, n, n)

def datos_matrices_mult_cuadrada(n):
    """
    Para mult(a, b, c, n) versión 2
    """

    a = [[randint(1, 100) for _ in range(n+1)] for _ in range(n+1)]
    
    b = [[randint(1, 100) for _ in range(n+1)] for _ in range(n+1)]
    
    c = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    return (a, b, c, n)

def datos_perm(n):
    """
    Para perm(a, k, n)
    Inicia k=1
    """

    a = [0] + [randint(1, 100) for _ in range(n)]
    return (a, 1, n)

def datos_seqsearch(n):
    """
    Para seqsearch(a, x, n)
    Garantiza que 'x' esté en el arreglo
    """

    a = [0] + [randint(1, 1000) for _ in range(n)]
    x = -999 # Recorre todo el arreglo

    return (a, x, n)

def datos_polinomios(n):
    """
    Genera los datos para los algoritmos de polinomios.
    Retorna grado (n) y valor x para evaluar.
    """
    x = 1.5  # Valor arbitrario pequeño para evitar desbordamientos
    return (n, x)

## EXTRAS ####################################################################

def datos_fibo(n):
    """
    Para fibonacci(n)
    """
    return (n,)