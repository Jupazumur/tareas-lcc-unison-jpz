import graficas as grf
import benchmark as bm

def _merge(arr, left, mid, right):
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

def _merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        _merge_sort(arr, left, mid)
        _merge_sort(arr, mid + 1, right)
        _merge(arr, left, mid, right)

def merge_sort_wrap(arr):
    """
    Wrapper para poder usar merge sort con el módulo benchmark.py
    """
    datos = arr[:]
    _merge_sort(datos, 0, len(datos) - 1)
    return datos

if __name__ == '__main__':
    
    escala = [10, 50, 100, 200, 500, 800, 1000, 1500, 1800, 2000]

    tiempos_mejor = bm.run_benchmark(bm.lista_ordenada, merge_sort_wrap)
    tiempos_peor = bm.run_benchmark(bm.lista_ordenada_inv, merge_sort_wrap)
    tiempos_promedio = bm.run_benchmark(bm.lista_aleatoria, merge_sort_wrap)

    grf.plot_resultados(escala, tiempos_mejor, 'Merge Sort - Mejor Caso')
    grf.plot_resultados(escala, tiempos_peor, 'Merge Sort - Peor Caso')
    grf.plot_resultados(escala, tiempos_promedio, 'Merge Sort - Caso Promedio')