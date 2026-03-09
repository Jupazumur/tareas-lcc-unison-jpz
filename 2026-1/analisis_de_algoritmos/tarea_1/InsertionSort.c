#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Esto lo hice antes de saber que se tenia que graficar

void InsertionSort(int arr[], int longitud)
{
    for(int j = 1; j < longitud; ++j)
    {
        int x = arr[j];
        int i = j - 1;

        
        while(x <= arr[i] && i >= 0)
        {
            arr[i+1] = arr[i];
            i = i - 1;
        }
        arr[i+1] = x;
    }
}

void ImprimirArreglo(int arr[], int longitud)
{
    for(int i = 0; i < longitud; ++i)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main()
{
    srand(time(NULL));

    //int mejor_caso[] = {1, 2, 3, 4, 5, 6};
    //int peor_caso[] = {6, 5, 4, 3, 2, 1};

    //int n = 10;
    int caso_promedio[10];

    for(int i = 0; i < 10; ++i)
    {
        caso_promedio[i] = (rand() % 10) + 1;
    }

    int longitud = sizeof(caso_promedio) / sizeof(caso_promedio[0]);
    
    printf("Arreglo original: \n");
    ImprimirArreglo(caso_promedio, longitud);

    InsertionSort(caso_promedio, longitud);
    
    printf("Arreglo ordenado: \n");
    ImprimirArreglo(caso_promedio, longitud);
}