import graficas as grf
import benchmark as bm

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

if __name__ == '__main__':
    
    escala = [10, 50, 100, 200, 500, 800, 1000, 1500, 1800, 2000]

    tiempos_mejor = bm.run_benchmark(bm.lista_ordenada, insertion_sort)
    tiempos_peor = bm.run_benchmark(bm.lista_ordenada_inv, insertion_sort)
    tiempos_promedio = bm.run_benchmark(bm.lista_aleatoria, insertion_sort)

    grf.plot_resultados(escala, tiempos_mejor, 'Insertion Sort - Mejor Caso')
    grf.plot_resultados(escala, tiempos_peor, 'Insertion Sort - Peor Caso')
    grf.plot_resultados(escala, tiempos_promedio, 'Insertion Sort - Caso Promedio')