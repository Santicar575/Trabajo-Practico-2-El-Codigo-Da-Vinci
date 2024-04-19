from PIL import Image
import numpy as np
dic_encriptacion = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, ',': 28,
    '?': 29, '!': 30, '¿': 31, '¡': 32, '(': 33, ')': 34, ':': 35, ';': 36, '-': 37,
    '“': 38, '‘': 39, 'á': 40, 'é': 41, 'í': 42, 'ó': 43, 'ú': 44, 'ü': 45, 'ñ': 46
}
imagen = Image.open("baboon.png")
imagen_array = np.array(imagen)
tamaño_imagen = len(imagen_array)
print(tamaño_imagen)

def agregar_marco(imagen_array):
    npad = ((2,2),(2,2),(0,0))
    imagen_array = np.pad(imagen_array, pad_width=npad, mode='edge')
    return imagen_array

def aplicar_filtro(tamaño_iamgen, imagen_array):
    imagen_array = agregar_marco(imagen_array,tamaño_iamgen)
    imagen_array_filtro = np.copy(imagen_array)
    for i in range(2, tamaño_imagen):
        for j in range(2, tamaño_imagen):
            imagen_array[i][j] = imagen_array[i-2][j-2]

imagen_array = agregar_marco(imagen_array)
print(imagen_array.shape)
imagen = Image.fromarray(imagen_array)
imagen.save("baboon_marco.png")
