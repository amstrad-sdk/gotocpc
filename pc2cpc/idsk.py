import os
import subprocess
import sys
from .common import consoleMessage, ConsoleColor, getFileExt, messageError, messageInfo, messageWarning, fileExist


def createDskFile(imagefile):
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    IDSK = str(SDK4BASIC_PATH) + '/bin/iDSK'
    cmd = [IDSK, '-n', imagefile]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(imagefile), f"Create image DSK.")
    except subprocess.CalledProcessError as e:
        messageError(getFileExt(imagefile), f'Error executing command: {e.output.decode()}')
        sys.exit(1)


def addBasFileDsk(imagefile, file):
    # ruta_actual = os.path.dirname(os.path.realpath(__file__))
    # imagefile = os.getcwd() + "/" + imagefile
    # file = os.getcwd() + "/" + file
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    # print(imagefile)
    # print(file)
    # fileExist(imagefile)
    # fileExist(file)
    cmd = [SDK4BASIC_PATH + '/bin/iDSK', imagefile, "-i", file, '-t', '0']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(file), f"Added file to dsk image.")
    except subprocess.CalledProcessError as e:
        messageError(getFileExt(imagefile), f'Error executing command: {e.output.decode()}')
        sys.exit(1)
    # comando = SDK4BASIC_PATH + '/bin/iDSK ' + imagefile + " -i " + file + ' -t 0'
    # # Ejecutar el comando y capturar la salida
    # salida = subprocess.check_output(comando, shell=True)

    # # Decodificar la salida en formato UTF-8
    # salida_decodificada = salida.decode("utf-8")

    # # Imprimir la salida
    # print(salida_decodificada)

def addBinaryFileDsk(imagefile, file):
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')

    cmd = [SDK4BASIC_PATH + '/bin/iDSK', imagefile, "-i", file, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(file), f"Added file to dsk image.")
    except subprocess.CalledProcessError as e:
        messageError(imagefile, f'Error executing command: {e.output.decode()}')
        sys.exit(1)


def addBinFileDsk(imagefile, file, laddress):
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    # cmd = [SDK4BASIC_PATH + '/bin/iDSK', imagefile, '-i', file, '-e',eaddress,'-c', laddress,'-t', '1']
    cmd = [SDK4BASIC_PATH + '/bin/iDSK', f"{imagefile}", '-i', file, '-c', laddress, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        messageInfo(getFileExt(file), f"Added file to dsk image:\n           address: {laddress} ")
    except subprocess.CalledProcessError as e:
        messageError(imagefile, f'Error executing command: {e.output.decode()}')
        sys.exit(1)


def extractFileDsk(imagefile, file):
    FNULL = open(os.devnull, 'w')
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    cmd = [SDK4BASIC_PATH + '/bin/iDSK', imagefile, "-g", file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        messageError(imagefile, f'Error executing command: {e.output.decode()}')
        sys.exit(1)
