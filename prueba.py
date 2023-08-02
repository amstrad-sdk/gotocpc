import argparse

description = 'Ejemplo de argumentos de línea de comandos.'

parser = argparse.ArgumentParser(description=description)
group = parser.add_mutually_exclusive_group()

group.add_argument('--project', '-p', help='Nombre del proyecto')
group.add_argument('--build', '-b', action='store_true', help='Realizar una construcción')

args = parser.parse_args()

if args.build:
    print('Parámetro --build usado')
elif args.project:
    print(f'Parámetro --project usado con el nombre de proyecto: {args.project}')
else:
    parser.print_help()


