import click
import os
import sys
import configparser
from rich import print
from .common import consoleMessage, ConsoleColor, removeComments, convert2Dos, concatBasFiles, \
    messageError, messageWarning, messageInfo, endCompilation, beginCompilation,concatFile, fileExist
from .project import readProjectIni
from rich.console import Console
from rich.text import Text
from .idsk import createDskFile, addBasFileDsk, addBinaryFileDsk, addBinFileDsk
import yaml

console = Console()


@click.command()
@click.option('-f', '--file', required=False, help='Input file name')
@click.option('-m', '--mode', type=click.Choice(['0', '1', '2']), default='0', help='Image Mode')
def main(file, mode):
    

    # PWD = os.getcwd() + "/"
    PROJECT_FILE = "project.yaml"

    # check if the project.ini file necessary for the execution of the program exists
    fileExist(PROJECT_FILE)

    ##
    # Define Variables
    ##
    
    with open(PROJECT_FILE, 'r') as file:
        data = yaml.safe_load(file)
    
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    NUMBER_CONCAT_FILES = sum(1 for item in data['spec']['files'] if item.get('kind') == 'bas' and item.get('concat') == True)
    COUNT = 0
    PATH_DISC = "disc"
    PATH_SRC = "src"
    PATH_DSK = "dsk"
    PATH_ASSETS = "assets"
    PROJECT_NOT_SECTIONS = ["PROJECT", "CONCATENATE", "RVM"]
    PROJECT_NAME = data['project']['data'].get('name', 'No project mame')
    PROJECT_AUTHOR = data['project']['data'].get('author', 'No author mame')
    PROJECT_RVM_SYSTEM = data['project']['rvm'].get('system', 'web')
    PROJECT_RVM_MODEL = data['project']['rvm'].get('model', '6128')
    PROJECT_RVM_RUN = data['project']['rvm'].get('name', 'run"main.bas"')
    PROJECT_CONCAT_OUT = PATH_DISC + "/" + data['project']['concatenate'].get('out', 'PROJECT.BAS')
    PROJECT_DSK_FILE = f"{PATH_DSK}/{PROJECT_NAME}.DSK"

    ##
    # Check the disc folder
    ##
    if not os.path.exists(PATH_DISC):
        os.makedirs(PATH_DISC)
    if not os.path.exists(PATH_DSK):
        os.makedirs(PATH_DSK)
        
    ##
    # Show begin compilation
    ##  
    beginCompilation(PROJECT_NAME)
    
    ##
    # Create image DSK
    ##  
    createDskFile(PROJECT_DSK_FILE)

    ##
    # Processing of project files
    ##  
    for file_data in data['spec']['files']:
        ##
        # Processing bas files
        ## 
        if file_data['kind'].upper() == 'BAS':
            COUNT = COUNT + 1
            fileExist(f"{PATH_SRC}/{file_data['name']}")
            removeComments(f"{PATH_SRC}/{file_data['name']}", f"{PATH_DISC}/{file_data['name']}")
            convert2Dos(f"{PATH_DISC}/{file_data['name']}", f"{PATH_DISC}/{file_data['name']}")
            if file_data['concat'] == True:
                concatFile(f"{PATH_DISC}/{file_data['name']}", PROJECT_CONCAT_OUT)
                if COUNT == NUMBER_CONCAT_FILES:
                    convert2Dos(PROJECT_CONCAT_OUT,PROJECT_CONCAT_OUT)
                    addBasFileDsk(PROJECT_DSK_FILE,f"{PATH_SRC}/{file_data['name']}")
            else:
                addBasFileDsk(PROJECT_DSK_FILE,f"{PATH_SRC}/{file_data['name']}")
        ##
        # Processing ascii files
        ## 
        elif file_data['kind'].upper() == 'ASCII':
            fileExist(f"{PATH_SRC}/{file_data['name']}")
            addBasFileDsk(PROJECT_DSK_FILE,f"{PATH_SRC}/{file_data['name']}")
        ##
        # Processing C files
        ## 
        elif file_data['kind'].upper() == 'C':
            fileExist(f"{PATH_SRC}/{file_data['name']}")
            print("compile fichero")
            print("Add file bin a DSK")
        ##
        # Processing images files
        ## 
        elif file_data['kind'].upper() == 'IMAGE':
            fileExist(f"{PATH_ASSETS}/{file_data['name']}")
            print("compile fichero")
            print("Add file bin a DSK")
        ##
        # Processing sprites files
        ## 
        elif file_data['kind'].upper() == 'SPRITE':
            fileExist(f"{PATH_ASSETS}/{file_data['name']}")
            print("compile fichero")
            print("Add file bin a DSK")

    ##
    # Show end compilation
    ##  
    endCompilation("OK")


if __name__ == '__main__':
    main()
