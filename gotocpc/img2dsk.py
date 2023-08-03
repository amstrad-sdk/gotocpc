from .martine import img2scr, img2spr
from .rvm import rvm_web
from .common import imageCompilation, endCompilation
import os
import time

def img2dsk(cpc,image, mode,rvm):
    # Registrar el tiempo de inicio
    start_time = time.time()  
    imageCompilation(image)
    img2scr(image, mode,"dsk/image", True)
    img = os.path.basename(os.path.splitext(image)[0]).upper()
    DSK_FILE = img + ".DSK"
    DSK_BAS = img + ".BAS"
    RUN = f'run"{DSK_BAS}"'
    HTML = img.upper() + ".HTML"
    
    if rvm.upper() == "WEB":
        if cpc != "6128":
            cpc = "6128"
            
        rvm_web(cpc,f"dsk/{DSK_FILE}",RUN,image,"CPC_RVM.HTML")
    else:
        print("RVM DESKTOP")
    
    endCompilation("OK",start_time)        
