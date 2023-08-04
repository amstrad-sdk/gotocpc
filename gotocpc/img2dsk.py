from .martine import img2scr, img2spr
from .rvm import rvm_web
from .common import imageCompilation, endCompilation, fileExist, messageError, messageInfo, messageWarning
import os
import time
import sys

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
        print("RVM DESKTOP")
    
    endCompilation("OK",start_time)        
