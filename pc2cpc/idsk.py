import os
import subprocess
import sys
from .common import consoleMessage, ConsoleColor, getFileExt, messageError, messageInfo, messageWarning, fileExist

global IDSK

if  sys.platform == "win64":
    DSK = os.path.dirname(os.path.abspath(__file__)) + "/bin/win/iDSK.exe"
elif sys.platform == "win32":
    messageError("PLATFORM", f'WIN32 Platform not supported')
    sys.exit(1)
else:
    IDSK = os.path.dirname(os.path.abspath(__file__)) + "/bin/" + sys.platform + "/iDSK"


# APP_PATH = os.path.dirname(os.path.abspath(__file__))

def createDskFile(imagefile):

    cmd = [IDSK, '-n', imagefile]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(imagefile), f"Create image DSK.")
    except subprocess.CalledProcessError as e:
        messageError(getFileExt(imagefile), f'Error executing command: {e.output.decode()}')
        sys.exit(1)


def addBasFileDsk(imagefile, file):
    cmd = [IDSK, imagefile, "-i", file, '-t', '0']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(file), f"Added file to dsk image.")
    except subprocess.CalledProcessError as e:
        messageError(getFileExt(imagefile), f'Error executing command: {e.output.decode()}')
        sys.exit(1)

def addBinaryFileDsk(imagefile, file):
    cmd = [IDSK, imagefile, "-i", file, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(file), f"Added file to dsk image.")
    except subprocess.CalledProcessError as e:
        messageError(imagefile, f'Error executing command: {e.output.decode()}')
        sys.exit(1)


def addBinFileDsk(imagefile, file, laddress):
    cmd = [IDSK, f"{imagefile}", '-i', file, '-c', laddress, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(file), f"Added file to dsk image:\n           address: {laddress} ")
    except subprocess.CalledProcessError as e:
        messageError(imagefile, f'Error executing command: {e.output.decode()}')
        sys.exit(1)


def extractFileDsk(imagefile, file):
    FNULL = open(os.devnull, 'w')
    cmd = [IDSK, imagefile, "-g", file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        messageError(imagefile, f'Error executing command: {e.output.decode()}')
        sys.exit(1)
