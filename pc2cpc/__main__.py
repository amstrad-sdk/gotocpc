import json
import subprocess
import click
import shutil
import os
import sys
import configparser

from .common import consoleMessage, ConsoleColor, getFileExt, checkProjectValue
from .project import readProjectIni

@click.command()
@click.option('-f', '--file', required=False, help='Input file name')
@click.option('-m', '--mode', type=click.Choice(['0', '1', '2']), default='0', help='Image Mode')

def main(file, mode):
    
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    PWD            = os.getcwd() + "/"
    PROJECT_FILE   = "project.ini"


    # check if the project.ini file necessary for the execution of the program exists
    if not os.path.isfile(PROJECT_FILE):
        print(consoleMessage("\nERROR: The " + PROJECT_FILE + " file does not exist.",ConsoleColor.RED))
        sys.exit(1)
    
    ##
    # Define Variables
    ##
    
    PROJECT_DATA          = readProjectIni(PROJECT_FILE)
    PROJECT_NAME          = PROJECT_DATA.get('PROJECT', {}).get('name')
    PROJECT_CONCAT_SOURCE = PROJECT_DATA.get('CONCATENATE', {}).get('source')
    PROJECT_CONCAT_OUT    = PROJECT_DATA.get('CONCATENATE', {}).get('out')
    PROJECT_RVM_SYSTEM    = PROJECT_DATA.get('RVM', {}).get('system')
    PROJECT_RVM_MODEL     = PROJECT_DATA.get('RVM', {}).get('model')
    PROJECT_RVM_RUN       = PROJECT_DATA.get('RVM', {}).get('run')
    PROJECT_DISC          = "disc"

    ##
    # Check the project values
    ##
    
    checkProjectValue("Project --> name",PROJECT_NAME)
    checkProjectValue("Project --> system",PROJECT_RVM_SYSTEM)
    checkProjectValue("Project --> model",PROJECT_RVM_MODEL)
    
    ##
    # Check the disc folder
    ##
    if not os.path.exists(PROJECT_DISC):
            os.makedirs(PROJECT_DISC)

    config = configparser.ConfigParser()
    
    # Leer el archivo INI
    config.read(PROJECT_FILE)
    
    # Recorrer las secciones del archivo INI
    for section in config.sections():
        # Imprimir el nombre de la sección
        if section != "project".upper() or section != "concatenate".upper() or section != "rvm".upper():
            print(f"[{section}]")
        
        # Recorrer las claves y valores de cada sección
        for clave, valor in config.items(section):
            print(f"{clave} = {valor}")
        
        print()  # Imprimir una línea en blanco entre secciones

    # if file is not None and mode is not None:
    #     # Se pasaron los parámetros -f y -m
    #     # Hacer algo con file y mode
    #     click.echo(f'Se pasaron los parámetros -f {file} y -m {mode}')
    # else:
    #     # No se pasaron los parámetros -f y -m
    #     # Hacer algo diferente
    #     click.echo('No se pasaron los parámetros -f y -m')



if __name__ == '__main__':
    main()
