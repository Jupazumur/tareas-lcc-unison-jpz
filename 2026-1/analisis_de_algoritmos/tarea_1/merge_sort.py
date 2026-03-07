from timeit import timeit
import random as rand
import matplotlib.pyplot as plt

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def lista_aleatoria(n):

    return [rand.randint(1, 1000) for _ in range(n)]

def benchmark_caso_promedio():
    escala = [10, 50, 100, 200, 500, 800, 1000, 1500, 1800, 2000]
    tiempos = []
    
    print(f"{'Tamaño (n)':<10} | {'Tiempo promedio (s)':<20}")
    print("-" * 40)

    factor_repeticion = 50

    for n in escala:
        datos_prueba = lista_aleatoria(n)
        
        tiempo_total = timeit(
            stmt=lambda: merge_sort(datos_prueba, 0, len(datos_prueba)-1), 
            number=factor_repeticion,
            globals=globals()
        )
        
        t_promedio = tiempo_total / factor_repeticion

        tiempos.append(t_promedio)
        print(f"{n:<10} | {t_promedio:<20.6f}")

    plot_resultados(escala, tiempos)

def benchmark_peor_caso():
    escala = [10, 50, 100, 200, 500, 800, 1000, 1500, 1800, 2000]
    tiempos = []
    
    print(f"{'Tamaño (n)':<10} | {'Tiempo promedio (s)':<20}")
    print("-" * 40)

    factor_repeticion = 50

    for n in escala:
        datos_prueba = list(range(n, 0, -1))
        
        tiempo_total = timeit(
            stmt=lambda: merge_sort(datos_prueba, 0, len(datos_prueba)-1), 
            number=factor_repeticion,
            globals=globals()
        )
        
        t_promedio = tiempo_total / factor_repeticion

        tiempos.append(t_promedio)
        print(f"{n:<10} | {t_promedio:<20.6f}")

    plot_resultados(escala, tiempos)

def benchmark_mejor_caso():
    escala = [10, 50, 100, 200, 500, 800, 1000, 1500, 1800, 2000]
    tiempos = []
    
    print(f"{'Tamaño (n)':<10} | {'Tiempo promedio (s)':<20}")
    print("-" * 40)

    factor_repeticion = 50

    for n in escala:
        datos_prueba = list(range(0, n, 1))
        
        tiempo_total = timeit(
            stmt=lambda: merge_sort(datos_prueba, 0, len(datos_prueba)-1),
            number=factor_repeticion,
            globals=globals()
        )
        
        t_promedio = tiempo_total / factor_repeticion

        tiempos.append(t_promedio)
        print(f"{n:<10} | {t_promedio:<20.6f}")

    plot_resultados(escala, tiempos)

def plot_resultados(escala, tiempos):
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(escala, tiempos, marker='o', linestyle='-', color='b', label='Insertion Sort')
    
    plt.title('Insertion Sort', fontsize=14)
    plt.xlabel('Escala (n)', fontsize=12)
    plt.ylabel('Tiempo de ejecución promedio (s)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.show()

if __name__ == '__main__':
    benchmark_mejor_caso()
    benchmark_peor_caso()
    benchmark_caso_promedio()