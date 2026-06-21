import matplotlib.pyplot as plt

def plot_resultados(escala, tiempos, titulo):
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(escala, tiempos, marker='o', linestyle='-', color='b', label=titulo)
    
    plt.title(titulo, fontsize=14)
    plt.xlabel('Escala (n)', fontsize=12)
    plt.ylabel('Tiempo de ejecución promedio (s)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.show()

def ajustar_y_graficar(escala, tiempos, titulo):
    """
    Realiza el ajuste lineal y cuadrático usando funciones de numpy,
    luego lo grafica.
    """
    import numpy as np

    x = np.array(escala)
    y = np.array(tiempos)

    # 1. Ajuste Lineal: T(n) = an + b (Polinomio de grado 1)
    # np.polyfit devuelve los coeficientes [a, b]
    coef_lin = np.polyfit(x, y, 1)
    
    # 2. Ajuste Cuadrático: T(n) = an^2 + bn + c (Polinomio de grado 2)
    # np.polyfit devuelve los coeficientes [a, b, c]
    coef_cuad = np.polyfit(x, y, 2)

    # Generar un eje X con muchos puntos para que las curvas se vean suaves en la gráfica
    x_suave = np.linspace(min(x), max(x), 100)
    
    # Calcular los valores de Y para las curvas ajustadas evaluando los polinomios
    y_lin = np.polyval(coef_lin, x_suave)
    y_cuad = np.polyval(coef_cuad, x_suave)

    plt.figure(figsize=(10, 6))

    plt.plot(x, y, 'ko', label='Datos reales $(n_i, T(n_i))$')

    etiqueta_lin = f'Ajuste Lineal: {coef_lin[0]:.2e}n + {coef_lin[1]:.2e}'
    plt.plot(x_suave, y_lin, 'b--', label=etiqueta_lin)

    etiqueta_cuad = f'Ajuste Cuadrático: {coef_cuad[0]:.2e}$n^2$ + {coef_cuad[1]:.2e}n + {coef_cuad[2]:.2e}'
    plt.plot(x_suave, y_cuad, 'r-', label=etiqueta_cuad)

    plt.title(f'Ajuste de Mínimos Cuadrados: {titulo}', fontsize=14)
    plt.xlabel('Tamaño de entrada (n)', fontsize=12)
    plt.ylabel('Tiempo de ejecución T(n) [segundos]', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.show()