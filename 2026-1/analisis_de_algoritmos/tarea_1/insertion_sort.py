from timeit import timeit
import random as rand
import matplotlib.pyplot as plt

def insertion_sort(arr):

    datos = arr[:]
    for j in range(1, len(datos)):
        x = datos[j]
        i = j - 1
        while(i >= 0 and x < datos[i]):
            datos[i+1] = datos[i]
            i -= 1
        datos[i+1] = x

    return datos

def lista_aleatoria(n):

    return [rand.randint(1, 1000) for _ in range(n)]

def benchmark():
    escala = [10, 100, 500, 1000, 1500, 2000]
    tiempos = []
    
    print(f"{'Tamaño (n)':<10} | {'Tiempo promedio (s)':<20}")
    print("-" * 40)

    factor_repeticion = 50

    for n in escala:
        datos_prueba = lista_aleatoria(n)
        
        tiempo_total = timeit(
            stmt=lambda: insertion_sort(datos_prueba), 
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
    benchmark()