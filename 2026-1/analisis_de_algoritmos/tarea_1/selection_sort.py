from timeit import timeit
import random as rand
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):

        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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
            stmt=lambda: selection_sort(datos_prueba), 
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
            stmt=lambda: selection_sort(datos_prueba), 
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
            stmt=lambda: selection_sort(datos_prueba), 
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