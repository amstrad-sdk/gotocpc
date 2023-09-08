import os
import subprocess
import sys
from .common import consoleMessage, ConsoleColor, getFileExt, getFile, getFileExtension, messageError,messageInfo,messageWarning
import shutil

def compile(file,file_out,address, include):
    CCZ80 = os.path.dirname(os.path.abspath(__file__)) + "/bin/ccz80.exe"
    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    if sys.platform != "win32" or sys.platform != "win64":
        cmd = ['mono', CCZ80, file, '/org='+address, '/include='+ APP_PATH + '/includes;'+ include]
    else:
        cmd = [CCZ80, file, '/org='+address, '/include='+ APP_PATH + '/includes;'+ include]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        name = getFile(file)
        shutil.move("src/" + name +".bin", file_out+name+".bin")
        messageInfo(name +".c[green] ==> [/green]" + name + ".bin [green]==>[/green] address: " + address)
        return True
    except subprocess.CalledProcessError as e:
        messageError(getFileExt(file) + f' ==> Error executing command: {e.output.decode()}')
        return False