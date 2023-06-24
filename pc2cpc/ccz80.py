import os
import subprocess
import sys
from .common import consoleMessage, ConsoleColor, getFileExt, getFile, getFileExtension, messageError,messageInfo,messageWarning
import shutil

def compile(file,file_out,address, include):
    
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    cmd = ['mono', SDK4BASIC_PATH + '/bin/ccz80.exe', file, '/org='+address, '/include='+ SDK4BASIC_PATH + '/cfg/include;'+ include]
    
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        name = getFile(file)
        shutil.move("src/" + name +".bin", file_out+name+".bin")
        messageInfo(name +".c", f"Compile c file.")
    except subprocess.CalledProcessError as e:
        print(consoleMessage(f'{file}: {e.output.decode()}', ConsoleColor.RED))
        sys.exit(1)