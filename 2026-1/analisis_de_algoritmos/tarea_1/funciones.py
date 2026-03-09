from numpy import log, linspace
import matplotlib.pyplot as plt

def _logaritmica(n):
    return log(n)

def _linearitmica(n):
    return n*log(n)

def _cuadratica(n):
    return n**2

def _cubica(n):
    return n**3

def dibujar_grafica():
    """
    Dibuja todas las funciones en una sola gráfica.
    """
    input = linspace(0.1, 10, 100)

    f_log = _logaritmica(input)
    f_n = input
    f_linearitmica = _linearitmica(input)
    f_n2 = _cuadratica(input)
    f_n3 = _cubica(input)


    plt.plot(input, f_n3, label="Cúbica")
    plt.plot(input, f_n2, label="Cuadrática")
    plt.plot(input, f_linearitmica, label="Linearítimica")
    plt.plot(input, f_n, label="Lineal")
    plt.plot(input, f_log, label="Logarítmica")

    plt.legend()
    plt.grid(True)
    plt.ylim(0,100)

    plt.show()

if __name__ == "__main__":
    dibujar_grafica()