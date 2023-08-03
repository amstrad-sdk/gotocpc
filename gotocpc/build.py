import os
import sys
import configparser
from rich import print
from .common import consoleMessage, ConsoleColor, removeComments, convert2Dos, concatBasFiles, \
    messageError, messageWarning, messageInfo, endCompilation, beginCompilation, concatFile, fileExist, getFile
from .project import readProjectIni
from rich.console import Console
from rich.text import Text
from .idsk import createDskFile, addBasFileDsk, addBinaryFileDsk, addBinFileDsk
from .rvm import rvm_web
from .martine import img2scr, img2spr
from .ccz80 import compile
import yaml
import shutil
from os import remove
import time

console = Console()

def build():
        # Registrar el tiempo de inicio
        start_time = time.time()  
        
        # PWD = os.getcwd() + "/"
        PROJECT_FILE = "project.yaml"

        # check if the project.ini file necessary for the execution of the program exists
        fileExist(PROJECT_FILE)

        ##
        # Define Variables
        ##

        with open(PROJECT_FILE, 'r') as file:
            data = yaml.safe_load(file)

        SDK4BASIC_PATH       = os.environ.get('SDK4BASIC_PATH')
        PWD                  = os.getcwd() + "/"
        NUMBER_CONCAT_FILES  = sum(1 for item in data['spec']['files'] if item.get('kind') == 'bas' and item.get('concat') == True)
        COUNT                = 0
        PATH_DISC            = "CPC"
        PATH_SRC             = "src"
        PATH_DSK             = "dsk"
        PATH_ASSETS          = "assets"
        PROJECT_NOT_SECTIONS = ["PROJECT", "CONCATENATE", "RVM"]
        PROJECT_NAME         = data['project']['data'].get('name', 'No project mame')
        PROJECT_AUTHOR       = data['project']['data'].get('author', 'No author mame')
        PROJECT_RVM_SYSTEM   = data['project']['rvm'].get('system', 'web')
        PROJECT_RVM_MODEL    = data['project']['rvm'].get('model', '6128')
        PROJECT_RVM_RUN      = data['project']['rvm'].get('name', 'run"main.bas"')
        PROJECT_CONCAT_OUT   = PATH_DISC + "/" + data['project']['concatenate'].get('out', 'PROJECT.BAS')
        PROJECT_DSK_FILE     = f"{PATH_DSK}/{PROJECT_NAME}.DSK"
        RVM_WEB              = "CPC_RVM.HTML"

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
                #convert2Dos2(f"{PATH_DISC}/{file_data['name']}")
                if file_data['concat'] == True:
                    concatFile(f"{PATH_DISC}/{file_data['name']}", PROJECT_CONCAT_OUT)
                    if COUNT == NUMBER_CONCAT_FILES:
                        convert2Dos(PROJECT_CONCAT_OUT, PROJECT_CONCAT_OUT)
                        addBasFileDsk(PROJECT_DSK_FILE, f"{PATH_DISC}/{file_data['name']}")
                else:
                    addBasFileDsk(PROJECT_DSK_FILE, f"{PATH_DISC}/{file_data['name']}")
            ##
            # Processing ascii files
            ## 
            elif file_data['kind'].upper() == 'ASCII':
                fileExist(f"{PATH_SRC}/{file_data['name']}")
                addBasFileDsk(PROJECT_DSK_FILE, f"{PATH_SRC}/{file_data['name']}")
            ##
            # Processing C files
            ## 
            elif file_data['kind'].upper() == 'C':
                fileExist(f"{PATH_SRC}/{file_data['name']}")
                compile(f"{PATH_SRC}/{file_data['name']}", f"{PATH_DISC}/", f"{file_data['address']}",
                        f"{file_data['include']}")
                
                addBinaryFileDsk(f"{PROJECT_DSK_FILE}", f"{PATH_DISC}/" + getFile(f"{PATH_DISC}/{file_data['name']}") + ".bin")
                #addBinFileDsk(f"{PROJECT_DSK_FILE}", f"{PATH_DISC}/" + getFile(f"{PATH_DISC}/{file_data['name']}") + ".bin",
                #              f"{file_data['address']}")

            ##
            # Processing images files
            ## 
            elif file_data['kind'].upper() == 'IMAGE':
                fileExist(f"{PATH_ASSETS}/{file_data['name']}")
                img2scr(f"{PATH_ASSETS}/{file_data['name']}", f"{file_data['mode']}", "assets", "")
                NEW_FILE = getFile(f"{PATH_ASSETS}/{file_data['name']}").upper()
                addBinaryFileDsk(f"{PROJECT_DSK_FILE}", f"{PATH_DISC}/{NEW_FILE}.SCR")
                if not file_data['pal']:
                    remove(f"{PATH_DISC}/{NEW_FILE}.PAL")
            ##
            # Processing sprites files
            ## 
            elif file_data['kind'].upper() == 'SPRITE':
                fileExist(f"{PATH_ASSETS}/{file_data['name']}")
                print("compile fichero")
                print("Add file bin a DSK")

        rvm_web(PROJECT_RVM_MODEL,f"dsk/{PROJECT_NAME}.DSK",PROJECT_RVM_RUN,PROJECT_NAME,RVM_WEB)

        ##
        # Show end compilation
        ##  
        endCompilation("OK")
        end_time = time.time()  # Registrar el tiempo de finalización

        execution_time = end_time - start_time
        print(f'El script tardó {execution_time:.6f} segundos en ejecutarse.')

    