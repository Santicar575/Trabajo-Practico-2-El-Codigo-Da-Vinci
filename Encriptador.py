from funciones import *
from PIL import Image 
import numpy as np 

def main():
    dic_encriptacion = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, ',': 28,
    '?': 29, '!': 30, '¿': 31, '¡': 32, '(': 33, ')': 34, ':': 35, ';': 36, '-': 37,
    '“': 38, '‘': 39, 'á': 40, 'é': 41, 'í': 42, 'ó': 43, 'ú': 44, 'ü': 45, 'ñ': 46
    }
    imagen_encriptada((encriptado("Mensaje super sercreto", dic_encriptacion)),(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
    # print("≡≡Encriptador≡≡")
    # path = input("Ingrese nombre de la imagen a utilizar como base:") 
    # msg =input("Ingrese el mensaje a esconder: ")
    # name_new_image = ("Ingrese nombre del archivo de salida: ") 
    # imagen = Image.open(path)
    # imagen_array = np.array(imagen)
    # tamaño_imagen_original = len(imagen_array)
    # imagen_array = aplicar_filtro(tamaño_imagen_original, imagen_array)
    # #imagen = Image.fromarray(imagen_array)
    # #imagen.save(name_new_image)
    # #imagen.show()

if __name__ == "__main__":
    main()