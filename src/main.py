# Resolve the problem!!
import re

def run():
    # Abrimos el archivo
    file = open('encoded.txt', 'r', encoding='utf-8')
    # Validamos que el archivo se abre, con .read() vemos su contenido
    # print(file.read())
    # Creamos un patron de letras minusculas
    patron = re.compile('[a-z]')
    # Buscamos el patron en el archivo
    matches = patron.findall(file.read())
    # Imprimimos los matches
    print(matches)
    # Convertimos el arreglo en string
    palabra = "".join(matches);
    # Imprimimos el string
    print(palabra)
    


if __name__ == '__main__':
    run()
