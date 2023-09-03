from .martine import img2scr, img2spr
from .rvm import rvm_web,rvm_desktop
from .common import imageCompilation, endCompilation, fileExist, messageError, messageInfo, messageWarning
import os
import time
import sys
import yaml



def img2dsk(cpc,image, mode,rvm):
    # Registrar el tiempo de inicio
    start_time = time.time()

    imageCompilation(image)
    if not os.path.isfile(image):
        messageError(f"The " + image +" file does not exist")
        endCompilation("ERROR",start_time)
        sys.exit(1)
        
    img2scr(image, mode,"dsk/image", True)
    img = os.path.basename(os.path.splitext(image)[0]).upper()
    DSK_FILE = img + ".DSK"
    DSK_BAS = img + ".BAS"
    RUN = f'run"{DSK_BAS}"'
    HTML = img.upper() + ".HTML"
    
    if rvm.upper() == "WEB":
        if cpc != "6128":
            cpc = "6128"
            
        rvm_web(cpc,f"dsk/{DSK_FILE}",RUN,image,"RVM.HTML")
    else:
        PROJECT_FILE = "CPC.YAML"
        with open(PROJECT_FILE, 'r') as file:
            data = yaml.safe_load(file)
        PROJECT_RVM_DESKTOP  = data['project']['rvm'].get('rvm_path')
        rvm_desktop(cpc,f"dsk/{DSK_FILE}",RUN,image,PROJECT_RVM_DESKTOP)
    
    endCompilation("OK",start_time)        
