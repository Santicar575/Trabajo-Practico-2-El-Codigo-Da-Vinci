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

def calc_varianza(lista:list[tuple[int,int,int]]) -> tuple[float,float,float]:
    """
    Funcion que calcula la varianza de una lista de tuplas
    Args:
        lista: list[tuple[int,int,int]]
    Returns:
        varianza: tuple[float,float,float]
    """
    pass

def pixel_suavisado(imagen_array, x, y):
    entorno = []
    for i in range(-2,3):
        for j in range(-2,3):
            entorno.append(imagen_array[x+i][y+j])
    entorno = np.array(entorno)
    #Cuadrantes 
    for i in range(-2,3): 
        for j in range(-2,3):
            primer_cuadrante =[entorno[x+i:x][y+j:y]]
            segundo_cuadrante = [entorno[x:x+i][y+j:y]]
            tercer_cuadrante = [entorno[x+i:x][y:y+j]]
            cuarto_cuadrante = [entorno[x:x+i][y+i:y]]
    
    # print(entorno)
    # print(entorno[24][0])
    pass

def aplicar_filtro(tamaño_imagen_original, imagen_array):
    imagen_array_marco = np.copy(agregar_marco(imagen_array))
    for i in range(2, tamaño_imagen_original):
        for j in range(2, tamaño_imagen_original):
            imagen_array[i-2][j-2] = pixel_suavisado(imagen_array_marco, i, j)

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

def main():
    dic_encriptacion = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, ',': 28,
    '?': 29, '!': 30, '¿': 31, '¡': 32, '(': 33, ')': 34, ':': 35, ';': 36, '-': 37,
    '“': 38, '‘': 39, 'á': 40, 'é': 41, 'í': 42, 'ó': 43, 'ú': 44, 'ü': 45, 'ñ': 46
    }
    imagen = Image.open("baboon.png")
    imagen_array = np.array(imagen)
    tamaño_imagen_original = len(imagen_array)
    print(tamaño_imagen_original)
    pixel_suavisado(agregar_marco(imagen_array), 2, 2)
    # imagen_array = agregar_marco(imagen_array)
    # print(imagen_array.shape)
    # imagen = Image.fromarray(imagen_array)
    # imagen.save("baboon_marco.png")

if __name__ == "__main__":
    main()