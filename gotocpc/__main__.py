import argparse
from .build import build
from .create import create_project
from .img2dsk import img2dsk

def main():
    description = 'Ejemplo de argumentos de línea de comandos.'

    parser = argparse.ArgumentParser(description=description)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--project', '-p', help='Nombre del proyecto')
    group.add_argument('--build', '-b', action='store_true', help='Realizar una construcción')

    parser.add_argument('--image', '-i', help='Imagen')
    parser.add_argument('--mode', '-m', type=int, choices=[0, 1, 2], help='Selecciona el modo imagen en CPC (0, 1, 2)')
    parser.add_argument('--cpc', '-c', type=int, choices=[464, 664, 6128], help='Selecciona el modelo CPC (464, 664, 6128)')
    parser.add_argument('--rvm', '-r', type=str, choices=["web", "desktop"], help='Selecciona RVM para probar (web, desktop)')
    
    args = parser.parse_args()

    if args.build:
        build()
    elif args.project:
        create_project(args.project)
    else:
        handle_image_mode(args, parser)

def handle_image_mode(args, parser):
    if args.image is not None and args.mode is not None and args.cpc is not None and args.rvm is not None:
        img2dsk(args.cpc, args.image, args.mode, args.rvm)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
