# import argparse

# description = 'Ejemplo de argumentos de línea de comandos.'

# parser = argparse.ArgumentParser(description=description)
# group = parser.add_mutually_exclusive_group()

# group.add_argument('--project', '-p', help='Nombre del proyecto')
# group.add_argument('--build', '-b', action='store_true', help='Realizar una construcción')

# args = parser.parse_args()

# if args.build:
#     print('Parámetro --build usado')
# elif args.project:
#     print(f'Parámetro --project usado con el nombre de proyecto: {args.project}')
# else:
#     parser.print_help()


import time

start_time = time.time()  # Registrar el tiempo de inicio

# Tu código aquí
for i in range(1000000):
    pass  # Ejemplo de bucle

end_time = time.time()  # Registrar el tiempo de finalización

execution_time = end_time - start_time
print(f'El script tardó {execution_time:.6f} segundos en ejecutarse.')
