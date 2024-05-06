from funciones import *
from PIL import Image 
import numpy as np 

def main():
    dic_desencriptacion = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' ', 28: '.',
        29: ',', 30: '?', 31: '!', 32: '¿', 33: '¡', 34: '(', 35: ')', 36: ':', 37: ';',
        38: '-', 39: '“', 40: "'" , 41: 'á', 42: 'é', 43: 'í', 44: 'ó', 45: 'ú', 46: 'ü', 47: 'ñ'
    }

    print("≡≡Desencriptador≡≡")
    path = input("Ingrese nombre del archivo encriptado: ")
    imagen = Image.open(path)
    imagen_array = np.array(imagen)
    lista_msg_encriptado = desencriptar_imagen(imagen_array)
    print(lista_msg_encriptado)
    msg_desencriptado = desencriptar_mensaje(lista_msg_encriptado,dic_desencriptacion)
    print("El mensaje oculto es: ", msg_desencriptado)

if __name__ == '__main__':
    main()