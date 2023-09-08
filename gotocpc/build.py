import os
import sys
import configparser
from rich import print
from .common import consoleMessage, ConsoleColor, removeComments, convert2Dos, concatBasFiles, \
    messageError, messageWarning, messageInfo, endCompilation, beginCompilation, concatFile, fileExist, getFile
from .project import readProjectIni
from .validate import validate
from rich.console import Console
from rich.text import Text
from .idsk import createDskFile, addBasFileDsk, addBinaryFileDsk, addBinFileDsk
from .rvm import rvm_web,rvm_desktop
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
        PROJECT_FILE = "CPC.YAML"

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
        PATH_DISC            = "out"
        PATH_SRC             = "src"
        PATH_DSK             = "dsk"
        PATH_ASSETS          = "assets"
        PROJECT_NOT_SECTIONS = ["PROJECT", "CONCATENATE", "RVM"]
        PROJECT_NAME         = data['project']['data'].get('name', 'No project mame')
        PROJECT_AUTHOR       = data['project']['data'].get('author', 'No author mame')
        PROJECT_RVM_SYSTEM   = data['project']['rvm'].get('system')
        PROJECT_RVM_DESKTOP  = data['project']['rvm'].get('rvm_path')
        PROJECT_RVM_MODEL    = data['project']['rvm'].get('model')
        PROJECT_RVM_RUN      = data['project']['rvm'].get('run')
        PROJECT_CONCAT_OUT   = PATH_DISC + "/" + data['project']['concatenate'].get('out', 'PROJECT.BAS')
        PROJECT_DSK_FILE     = f"{PATH_DSK}/{PROJECT_NAME}.DSK"
        RVM_WEB              = "RVM.HTML"

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
        beginCompilation(PROJECT_NAME,PROJECT_AUTHOR,PROJECT_RVM_MODEL)

        # validate yaml
        if not validate(PROJECT_FILE): endCompilation("ERROR",start_time)
            

        ##
        # Create image DSK
        ##  
        if not createDskFile(PROJECT_DSK_FILE):
            endCompilation("ERROR",start_time)

        ##
        # Processing of project files
        ##  
        for file_data in data['spec']['files']:
            ##
            # Processing bas files
            ## 
            if file_data['kind'].upper() == 'BAS':
                COUNT = COUNT + 1
                if not fileExist(f"{PATH_SRC}/{file_data['name']}"): endCompilation("ERROR",start_time)
                if not removeComments(f"{PATH_SRC}/{file_data['name']}", f"{PATH_DISC}/{file_data['name']}"): endCompilation("ERROR",start_time)
                if not convert2Dos(f"{PATH_DISC}/{file_data['name']}", f"{PATH_DISC}/{file_data['name']}"): endCompilation("ERROR",start_time)
                #convert2Dos2(f"{PATH_DISC}/{file_data['name']}")
                if file_data['concat'] == True:
                    if not concatFile(f"{PATH_DISC}/{file_data['name']}", PROJECT_CONCAT_OUT): endCompilation("ERROR",start_time)
                    if COUNT == NUMBER_CONCAT_FILES:
                        if not convert2Dos(PROJECT_CONCAT_OUT, PROJECT_CONCAT_OUT): endCompilation("ERROR",start_time)
                        if not addBasFileDsk(PROJECT_DSK_FILE, f"{PATH_DISC}/{file_data['name']}") : endCompilation("ERROR",start_time)
                else:
                    if not addBasFileDsk(PROJECT_DSK_FILE, f"{PATH_DISC}/{file_data['name']}"): endCompilation("ERROR",start_time)
            ##
            # Processing ascii files
            ## 
            elif file_data['kind'].upper() == 'ASCII':
                if not fileExist(f"{PATH_SRC}/{file_data['name']}"): endCompilation("ERROR",start_time)
                if not addBasFileDsk(PROJECT_DSK_FILE, f"{PATH_SRC}/{file_data['name']}"): endCompilation("ERROR",start_time)
            ##
            # Processing C files
            ## 
            elif file_data['kind'].upper() == 'C':
                if not fileExist(f"{PATH_SRC}/{file_data['name']}"): endCompilation("ERROR",start_time)
                if not compile(f"{PATH_SRC}/{file_data['name']}", f"{PATH_DISC}/", f"{file_data['address']}",
                        f"{file_data['include']}"): endCompilation("ERROR",start_time)
                
                if not addBinaryFileDsk(f"{PROJECT_DSK_FILE}", f"{PATH_DISC}/" + getFile(f"{PATH_DISC}/{file_data['name']}") + ".bin"): endCompilation("ERROR",start_time)

            ##
            # Processing images files
            ## 
            elif file_data['kind'].upper() == 'IMAGE':
                if not fileExist(f"{PATH_ASSETS}/{file_data['name']}"): endCompilation("ERROR",start_time)
                if not img2scr(f"{PATH_ASSETS}/{file_data['name']}", f"{file_data['mode']}", "assets", ""): endCompilation("ERROR",start_time)
                NEW_FILE = getFile(f"{PATH_ASSETS}/{file_data['name']}").upper()
                if not addBinaryFileDsk(f"{PROJECT_DSK_FILE}", f"{PATH_DISC}/{NEW_FILE}.SCR"): endCompilation("ERROR",start_time)
                if not file_data['pal']:
                    remove(f"{PATH_DISC}/{NEW_FILE}.PAL")
            ##
            # Processing sprites files
            ## 
            elif file_data['kind'].upper() == 'SPRITE':
                if not fileExist(f"{PATH_ASSETS}/{file_data['name']}"): endCompilation("ERROR",start_time)
                if not img2spr(f"{PATH_ASSETS}/{file_data['name']}",f"{file_data['mode']}",f"{file_data['width']}",f"{file_data['height']}","assets"): endCompilation("ERROR",start_time)

        if PROJECT_RVM_SYSTEM == "web":
            rvm_web(PROJECT_RVM_MODEL,f"dsk/{PROJECT_NAME}.DSK",PROJECT_RVM_RUN,PROJECT_NAME,RVM_WEB)
        elif PROJECT_RVM_SYSTEM == "desktop":
            if PROJECT_RVM_DESKTOP == "":
                messageError("There is no path to Retro virtual machine")
                endCompilation("ERROR",start_time)
            if not os.path.isfile(PROJECT_RVM_DESKTOP):
                messageError(PROJECT_RVM_DESKTOP +"[red] ==> FILE DOES NOT EXIST")
                endCompilation("ERROR",start_time)
            if not rvm_desktop(PROJECT_RVM_MODEL,f"{PWD}/dsk/{PROJECT_NAME}.DSK",PROJECT_RVM_RUN,PROJECT_NAME,PROJECT_RVM_DESKTOP):endCompilation("ERROR",start_time)

        ##
        # Show end compilation
        ##  

        endCompilation("OK",start_time)


    