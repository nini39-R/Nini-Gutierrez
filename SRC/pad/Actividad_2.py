import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class ejercicios:
    def __init__(self):
        datos = [(i, None) for i in range(1, 22)] 
        self.df= pd.DataFrame(data=datos,columns=["#ejercicios", "valor"])
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_actividad_2 = "{}/SRC/pad/Entregables_actividad_2/".format(self.ruta_raiz)


    def ejercicio_1(self):
        # Generar un array con valores desde 10 hasta 29
        array_10_29 = np.arange(10,30)
        self.df.iloc[0, 1] = ', '.join(map(str, array_10_29.tolist()))

    def ejercicio_2(self):
        # 2. Suma de una matriz 10x10 de unos.
        X = np.ones((10, 10))
        suma = np.sum(X)
        self.df.iloc[1,1]=str(suma)
        print("ejercicio_2", suma)
        
    def ejercicio_3(self):
        # Generar dos arrays de tamaño 5 con números aleatorios entre 1 y 10
        X = np.random.randint(1, 11, 5)
        Y = np.random.randint(1, 11, 5)
        producto = X * Y
        self.df.iloc[2,1]=str(producto)
        #print("Array 1:", array1)
        #print("Array 2:", array2)
        print("ejercicio_3", producto)

    def ejercicio_4(self):
         # Crear una matriz diagonal dominante para garantizar que sea invertible
        matriz = np.fromfunction(lambda i, j: np.where(i == j, i + j + 10, i + j), (4, 4), dtype=int)
        inversa = np.linalg.inv(matriz)
        self.df.iloc[3, 1] = str(inversa)
        print("\nMatriz inversa:\n", inversa)

    def ejercicio_5(self):
        #Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices.
        array5 = np.random.rand(100)
        max_val = np.max(array5)
        min_val = np.min(array5)
        indice_max = np.argmax(array5)
        indice_min = np.argmin(array5)
        self.df.iloc[4, 1] = f"Max: {max_val}, IndMax: {indice_max}, Min: {min_val}, IndMin: {indice_min}"
        print(f'Máximo: {max_val} en índice {indice_max}')
        print(f'Mínimo: {min_val} en índice {indice_min}')

    #Broadcasting e indexado de Arrays:
    def ejercicio_6(self):
        #Crea un array de tamaño 3x1 y uno de 1x3, y súmalos utilizando broadcasting para obtener un array de 3x3.
        X = np.arange(3).reshape(3, 1)
        Y = np.arange(3).reshape(1, 3)
        resultado = X + Y
        self.df.iloc[5, 1] = f"Array 3x1:\n{np.array_str(X)}\n\nArray 1x3:\n{np.array_str(Y)}\n\nSuma (3x3):\n{np.array_str(resultado)}" 
        print("ejercicio_6", resultado)

    def ejercicio_7(self):
        #De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna.
        matriz5x5 = np.random.randint(1, 10, (5, 5))
        submatriz = matriz5x5[1:3, 1:3]
        self.df.iloc[6, 1] = f"Matriz 5x5:\n{np.array_str(matriz5x5)}\n\nSubmatriz 2x2:\n{np.array_str(submatriz)}"
        print("ejercicio_7", submatriz)
    
    def ejercicio_8(self):
        #Crea un array de ceros de tamaño 10 y usa indexado para cambiar el valor de los elementos en el rango de índices 3 a 6 a 5
        array8 = np.zeros(10)
        array8[3:7] = 6
        self.df.iloc[7, 1] = str(array8)
        print("ejercicio_8", array8)

    def ejercicio_9(self):
        #Dada una matriz de 3x3, invierte el orden de sus filas
        matriz = np.random.randint(1, 10, (3, 3))
        matriz_invertida = matriz[::-1]
        self.df.iloc[8, 1] = f"Matriz original:\n{str(matriz.tolist())}\n\nMatriz invertida:\n{str(matriz_invertida.tolist())}"
        print("ejercicio_9", matriz_invertida)

    def ejercicio_10(self):
        #Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 0.5.
        array10 = np.random.rand(10)
        mayores_05 = array10[array10 > 0.5]
        self.df.iloc[9, 1] = f"Array:\n{str(array10)}\n\nMayores a 0.5:\n{str(mayores_05)}"
        print("ejercicio_10", mayores_05)

    #Gráficos de dispersión, densidad y contorno:
    def ejercicio_11(self):
        #Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.
        X = np.random.rand(100)
        Y = np.random.rand(100)
        plt.figure() 
        plt.scatter(X, Y)
        plt.title("Gráfico de dispersión")
        plt.xlabel("X")
        plt.ylabel("Y")
        ruta = "{}ejercicio_11.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_11", "Gráfico de dispersión")
        

    def ejercicio_12(self):
        #Genera un gráfico de dispersión las variables 𝑥 y 𝑦 = 𝑠𝑖𝑛(𝑥)+ ruido Gaussiano. Donde x es un array con númereos entre -2𝜋 𝑦 2𝜋. Grafica también los puntos 𝑦 = 𝑠𝑖𝑛(𝑥) en el mismo plot
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.sin(x) + np.random.normal(0, 0.1, 100)
        plt.figure()
        plt.scatter(x, y, label="sin(x) + ruido")
        plt.plot(x, np.sin(x), label="sin(x)", color="red")
        plt.legend()
        plt.title("Gráfico de dispersión con ruido")
        plt.xlabel("x")
        plt.ylabel("y")
        ruta = "{}ejercicio_12.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_12", "Gráfico de dispersión con ruido")

    def ejercicio_13(self):
        #Utiliza la función np.meshgrid para crear una cuadrícula y luego aplica la función z = np.cos(x) + np.sin(y) para generar y mostrar un gráfico de contorno.
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.linspace(-2*np.pi, 2*np.pi, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.cos(X) + np.sin(Y)
        plt.figure()
        plt.contourf(X, Y, Z)
        plt.colorbar()
        plt.title("Gráfico de contorno")
        plt.xlabel("x")
        plt.ylabel("y")
        ruta= "{}ejercicio_13.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_13", "Gráfico de contorno")

    def ejercicio_14(self):
        #Crea un gráfico de dispersión con 1000 puntos aleatorios y utiliza la densidad de estos puntos para ajustar el color de cada punto.
        x = np.random.rand(1000)
        y = np.random.rand(1000)
        plt.figure()
        plt.scatter(x, y, c=x, cmap="viridis")
        plt.colorbar()
        plt.title("Gráfico de dispersión con densidad de puntos")
        plt.xlabel("x")
        plt.ylabel("y")
        rura= "{}ejercicio_14.png".format(self.ruta_actividad_2)
        plt.savefig(rura)
        plt.close()
        print("ejercicio_14", "Gráfico de dispersión con densidad de puntos")

    def ejercicio_15(self):
        #A partir de la misma función del ejercicio 12, genera un gráfico de contorno lleno.
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.linspace(-2*np.pi, 2*np.pi, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.cos(X) + np.sin(Y)
        plt.figure()
        plt.contour(X, Y, Z)
        plt.colorbar()
        plt.title("Gráfico de contorno lleno")
        plt.xlabel("x")
        plt.ylabel("y")
        ruta= "{}ejercicio_15.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_15", "Gráfico de contorno lleno")

    def ejercicio_16(self):
        #Añade etiquetas para el eje X (‘Eje X’), eje Y (‘Eje Y’) y un título (‘Gráfico de Dispersión’) a tu gráfico de dispersión del ejercicio 12 y crea leyendas para cada gráfico usando código LaTex
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.sin(x) + np.random.normal(0, 0.1, 100)   
        plt.figure()
        plt.scatter(x, y, label=r"$\sin(x) + ruido$")
        plt.plot(x, np.sin(x), label=r"$\sin(x)$", color="red")
        plt.legend()
        plt.title("Gráfico de dispersión")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        ruta= "{}ejercicio_16.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_16", "Gráfico de dispersión con etiquetas")

     #Histogramas
    def ejercicio_17(self):
        #Crea un histograma a partir de un array de 1000 números aleatorios generados con una distribución normal.
        array17 = np.random.normal(0, 1, 1000)
        plt.figure()
        plt.hist(array17, bins=30)
        plt.title("Histograma")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_17.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_17", "Histograma")

    def ejercicio_18(self):
        #Genera dos sets de datos con distribuciones normales diferentes y muéstralos en el mismo histograma.
        array18_1 = np.random.normal(0, 1, 1000)
        array18_2 = np.random.normal(2, 1, 1000)
        plt.figure()
        plt.hist(array18_1, bins=30, alpha=0.5, label="Array 1")
        plt.hist(array18_2, bins=30, alpha=0.5, label="Array 2")
        plt.legend()
        plt.title("Histograma con dos distribuciones")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_18.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_18", "Histograma con dos distribuciones")

    def ejercicio_19(self):
        #Experimenta con diferentes valores de bins (por ejemplo, 10, 30, 50) en un histograma y observa cómo cambia la representación.
        array19 = np.random.normal(0, 1, 1000)
        plt.figure()
        plt.hist(array19, bins=10, alpha=0.5, label="Bins 10")
        plt.hist(array19, bins=30, alpha=0.5, label="Bins 40")
        plt.hist(array19, bins=50, alpha=0.5, label="Bins 70")
        plt.legend()
        plt.title("Histograma con diferentes bins")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_19.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_19", "Histograma con diferentes bins")

    def ejercicio_20(self):
        #Añade una línea vertical que indique la media de los datos en el histograma.
        array20 = np.random.normal(0, 1, 1000)
        plt.figure()
        plt.hist(array20, bins=30, alpha=0.5)
        plt.axvline(np.mean(array20), color="green", linestyle="--", label="Media")
        plt.legend()
        plt.title("Histograma con media")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_20.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_20", "Histograma con media")

    def ejercicio_21(self):
        #Crea histogramas superpuestos para los dos sets de datos del ejercicio 17, usando colores y transparencias diferentes para distinguirlos.
        array21_1 = np.random.normal(0, 1, 1000)
        array21_2 = np.random.normal(2, 1, 1000)
        plt.figure()
        plt.hist(array21_1, bins=30, alpha=0.5, color="blue", label="Array 1")
        plt.hist(array21_2, bins=30, alpha=0.5, color="red", label="Array 2")
        plt.legend()
        plt.title("Histograma con dos distribuciones")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        ruta= "{}ejercicio_21.png".format(self.ruta_actividad_2)
        plt.savefig(ruta)
        plt.close()
        print("ejercicio_21", "Histograma con dos distribuciones superpuestas")


    def ejecutar(self):
        self.ejercicio_1()
        self.ejercicio_2()
        self.ejercicio_3()
        self.ejercicio_4()
        self.ejercicio_5()
        self.ejercicio_6()
        self.ejercicio_7()
        self.ejercicio_8()
        self.ejercicio_9()
        self.ejercicio_10()
        self.ejercicio_11()
        self.ejercicio_12()
        self.ejercicio_13()
        self.ejercicio_14()
        self.ejercicio_15()
        self.ejercicio_16()
        self.ejercicio_17()
        self.ejercicio_18()
        self.ejercicio_19()
        self.ejercicio_20()
        self.ejercicio_21()
        
        self.df.to_csv(f"{self.ruta_actividad_2}/Actividad_2.csv", index=False)
ene= ejercicios()
ene.ejecutar()

        