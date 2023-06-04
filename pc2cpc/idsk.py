import os
import subprocess
import sys
from .common import consoleMessage, ConsoleColor, getFileExt

def createDskFile(imagefile):
    
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    cmd = [SDK4BASIC_PATH + '/bin/iDSK', '-n', imagefile]
    
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(consoleMessage(f'Error executing command: {e.output.decode()}', ConsoleColor.RED))
        sys.exit(1)


def addBinaryFileDsk(imagefile, file):
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    cmd = [SDK4BASIC_PATH + '/bin/iDSK', imagefile, "-i", file, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(consoleMessage(f'Error executing command: {e.output.decode()}', ConsoleColor.RED))
        sys.exit(1)

def addBinFileDsk(imagefile, file,laddress,eaddress):
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    cmd = [SDK4BASIC_PATH + '/bin/iDSK', imagefile, '-i', file, '-e',eaddress,'-c', laddress,'-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(consoleMessage(f'Error executing command: {e.output.decode()}', ConsoleColor.RED))
        sys.exit(1)

def extractFileDsk(imagefile, file):

    FNULL = open(os.devnull, 'w')
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    cmd = [SDK4BASIC_PATH + '/bin/iDSK', imagefile, "-g", file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(consoleMessage(f'Error executing command: {e.output.decode()}', ConsoleColor.RED))
        sys.exit(1)
    