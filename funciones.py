from PIL import Image
import numpy as np

def agregar_marco(imagen_array):
    """
    Funcion que agrega un marco a una imagen
    Args:
        imagen_array: np.array
    Returns:
        imagen_array: np.array
    """
    npad = ((2,2),(2,2),(0,0))
    imagen_array = np.pad(imagen_array, pad_width=npad, mode='edge')
    return imagen_array

def calc_varianza(lista:np.array) -> tuple[float,float,float]:
    """
    Funcion que calcula la varianza de un array de numpy
    Args:
        lista: list[tuple[int,int,int]]
    Returns:
        varianza: tuple[float,float,float]
    """
    return np.var(lista[:,:,0]), np.var(lista[:,:,1]), np.var(lista[:,:,2])
def promedio_cuadrante(lista:np.array) -> tuple[float,float,float]:
    """
    Funcion que calcula el promedio de un array de numpy
    Args:
        lista: list[tuple[int,int,int]]
    Returns:
        promedio: tuple[float,float,float]
    """
    return np.mean(lista[:,:,0]), np.mean(lista[:,:,1]), np.mean(lista[:,:,2])

def pixel_suavizado(imagen_array, x, y):
    entorno = []
    fila = []
    for i in range(-2,3):
        for j in range(-2,3):
            fila.append(imagen_array[x+i,y+j])
        entorno.append(fila)
        fila = []
    entorno = np.array(entorno)
    #Cuadrantes
    primer_cuadrante= entorno[0:3,0:3]
    segundo_cuadrante = entorno[0:3,2:]
    tercer_cuadrante = entorno[2:,0:3]
    cuarto_cuadrante = entorno[2:,2:]
    dicc_cuadrantes = {
        sum(calc_varianza(primer_cuadrante)): primer_cuadrante,
        sum(calc_varianza(segundo_cuadrante)): segundo_cuadrante,
        sum(calc_varianza(tercer_cuadrante)): tercer_cuadrante,
        sum(calc_varianza(cuarto_cuadrante)): cuarto_cuadrante
    }
    cuadrante_menor_varianza = dicc_cuadrantes[min(dicc_cuadrantes.keys())]
    promedio = promedio_cuadrante(cuadrante_menor_varianza)
    return np.array(promedio)

def aplicar_filtro(tamaño_imagen_original, imagen_array):
    imagen_array_marco = np.copy(agregar_marco(imagen_array))
    for i in range(2, tamaño_imagen_original):
        for j in range(2, tamaño_imagen_original):
            imagen_array[i-2,j-2] = pixel_suavizado(imagen_array_marco, i, j)
    return imagen_array

def encriptado(mensaje,dic_encriptacion): 
    """
    Funcion que encripta un mensaje en base a un diccionario de encriptacion
    Args:
        mensaje: str
    Returns:
        mensaje_encriptado: list 
    """
    mensaje = mensaje.lower()
    mensaje_encriptado = []
    for char in mensaje: 
        if char in dic_encriptacion.keys(): 
            if len(str(dic_encriptacion[char])) > 1:
                for dig in str(dic_encriptacion[char]): 
                    mensaje_encriptado.append(int(dig) + 1)
            else: 
                mensaje_encriptado.append(dic_encriptacion[char]+1)
            mensaje_encriptado.append(-1)
    mensaje_encriptado.append(0)     
    return mensaje_encriptado