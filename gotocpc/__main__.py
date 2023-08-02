import argparse
from .build import build
from .create import create

def main():
    description = 'Ejemplo de argumentos de línea de comandos.'

    parser = argparse.ArgumentParser(description=description)
    group = parser.add_mutually_exclusive_group()

    group.add_argument('--project', '-p', help='Nombre del proyecto')
    group.add_argument('--build', '-b', action='store_true', help='Realizar una construcción')

    args = parser.parse_args()

    if args.build:
        build()
    elif args.project:
        create(args.project)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
