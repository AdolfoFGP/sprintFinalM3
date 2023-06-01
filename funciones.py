import re
import random
import string

def generar_contrasena(longitud=8):
    '''
    Esta función tiene por objetivo crear una contraseña de longitud por defecto 8 caracteres, entre ellos deben
    existir al menos una letra mayúscula, minúscula y un numero.
    
    Params:
        longitud: Por defecto tiene el valor 8. Corresponde al largo de caracteres 
        que se desea tener en la contraseña generada.
    Retorna:
        Contraseña generada

    '''
    while True:
        # ascii_letters de la libreria string, contiene todas las letras ASCII en mayus y minusculas
        # Por su parte, digits con tiene los digitos numericos del 0 al 9
        # Estos dos se concatenan y se guardan en la variable caracteres
        caracteres = string.ascii_letters + string.digits
        # se crea la varible contrasena vacía y se le asigna valores random del string caracteres
        contrasena = ''
        for i in range(longitud):
            contrasena += random.choice(caracteres)
        # Se utilizan expresiones regulares para validar que exista al menos una letra mayus, una letra minus y un numero
        # en la contraseña generada.
        patron = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'
        coincidencia = re.match(patron, contrasena)
        if bool(coincidencia):
            break

    return contrasena


def creacion_cuenta(lista_usuarios):
    '''
    Esta funcion crea un diccionario con un usuario de la lista entregada como parámetro como clave, y como valor,
    un diccionario con la contraseña generada con la funcion "generar_contrasena", y una clave telefono con valores vacíos.
    Params:
        lista_usuarios: Lista de usuarios con los que se creará el diccionario.

    Retorna:
        Diccionario con datos por usuario, contraseña y telefono como clave con valores vacíos.
    '''
    cuentas_usuarios = {}  # Crear un diccionario vacío

    #Se crea diccionario con el foor loop
    for usuario in lista_usuarios:
        cuentas_usuarios[usuario] = {'contraseña': generar_contrasena(), 'telefono': {}}

    return cuentas_usuarios

