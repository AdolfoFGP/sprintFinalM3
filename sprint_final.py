import pprint
import funciones as fx

# Se tienen los siguientes 10 usuarios:
nombres_usuarios = ['Pablo', 'Andres', 'Martina', 'Julia', 'Catalina',
                    'Raul', 'Freddy', 'Liz', 'Julieta', 'Jose']

# Se crea cuenta con la funcion "creacion_cuenta", entregandole como parámetro la lista de usuarios.
# Esta funcion retorna un diccionario con los datos de los usuarios y se asigna a la varible datos.
datos = fx.creacion_cuenta(nombres_usuarios)

# For loop para registrar numero telefonico para cada uno de los usuarios en el diccionario "datos" creado.
for usuario in nombres_usuarios:
    while True:
        num_telefono = input(f"Ingrese número telefónico para el usuario '{usuario}': ")
        # Se valida que el valor ingresado sea numerico y tenga un largo de 8 caracteres
        if num_telefono.isdigit() and len(num_telefono) == 8:
            # Se agrega al diccionario "datos" creado con anterioridad
            datos[usuario]['telefono'] = num_telefono
            break
        else:
            print("El número telefónico debe contener 8 dígitos numéricos")

# Se muestra la bd de las cuentas de los usuarios en la terminal:
# print(datos)
pprint.pprint(datos)

                



