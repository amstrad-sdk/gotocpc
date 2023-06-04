import os
import subprocess
import sys
from .common import consoleMessage, ConsoleColor, getFileExt

def compile(file,address, include):
    
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    cmd = ['mono', SDK4BASIC_PATH + '/bin/ccz80.exe', file, '/org='+address, '/include='+ SDK4BASIC_PATH + '/cfg/include;'+ include]
    
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(consoleMessage(f'{file}: {e.output.decode()}', ConsoleColor.RED))
        sys.exit(1)