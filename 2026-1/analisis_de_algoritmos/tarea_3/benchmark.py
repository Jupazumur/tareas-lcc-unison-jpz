ESCALA_N = [100, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000]
ESCALA_RSUM = [10, 50, 100, 200, 300, 400, 500, 600, 800, 950] # Evita el limite de recursion 1000
ESCALA_N2 = [5, 10, 25, 50, 100, 200, 300, 400, 600, 800]
ESCALA_N3 = [5, 10, 20, 50, 80, 100, 120, 150, 200, 250]
ESCALA_FACTORIAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def run_benchmark(funcion_datos, algoritmo, escala, imprimir_t=False):
    """
    Usa timeit para calcular los tiempos promedio de ejecución para una lista de valores de n.

    funcion_datos: Funcion que genera los datos (la lista de números)
    algoritmo: Algoritmo que se va a utilizar en la prueba
    """
    from timeit import timeit

    tiempos = []
    
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

def datos_fibo(n):
    """
    Para fibonacci(n)
    """
    return (n,)

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
    x = a[n // 2] if n > 0 else 0

    return (a, x, n)