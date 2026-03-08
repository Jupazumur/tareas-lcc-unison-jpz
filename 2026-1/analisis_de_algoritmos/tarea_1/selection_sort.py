import graficas as grf
import benchmark as bm

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):

        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == '__main__':
    
    escala = [10, 50, 100, 200, 500, 800, 1000, 1500, 1800, 2000]

    tiempos_mejor = bm.run_benchmark(bm.lista_ordenada, selection_sort)
    tiempos_peor = bm.run_benchmark(bm.lista_ordenada_inv, selection_sort)
    tiempos_promedio = bm.run_benchmark(bm.lista_aleatoria, selection_sort)

    grf.plot_resultados(escala, tiempos_mejor, 'Selection Sort - Mejor Caso')
    grf.plot_resultados(escala, tiempos_peor, 'Selection Sort - Peor Caso')
    grf.plot_resultados(escala, tiempos_promedio, 'Selection Sort - Caso Promedio')