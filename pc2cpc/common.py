import os
import sys

class ConsoleColor:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'




def checkProjectValue(text, value):
    if value is None or value == "":
        print(consoleMessage("\nERROR: The " + str(text) + " key does not exist or has no value.",ConsoleColor.RED))
        sys.exit(1)

##
# Print message color
#
# @param text: text to print
# @param color: Color with which the text will be painted
##
def consoleMessage(text, color):
    colored_text = f"{color}{text}{ConsoleColor.RESET}"
    return colored_text

# Ejemplo de uso
# print_colored("Texto en verde", ConsoleColor.GREEN)
# print_colored("Texto en amarillo", ConsoleColor.YELLOW)
# print_colored("Texto en rojo", ConsoleColor.RED)
# print("Texto normal")

##
# Get Get file without extension
#
# @param source: source filename
##
def getFile(source):
    file_name = os.path.basename(source)
    file_name = os.path.splitext(file_name)[0]
    return file_name

##
# Get file and extension
#
# @param source: source filename
##
def getFileExt(source):
    file_name = os.path.basename(source)
    return file_name

##
# Get extension file
#
# @param source: source filename
##
def getFileExtension(source):
    file_extension = os.path.splitext(source)[1]
    return file_extension

##
# Remove comment lines
#
# @param source: source filename
# @param output: output filename
##
def removeComments(source, output):
    with open(source, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not line.startswith("1'") and not line.startswith("1 '")]

    with open(output, 'w') as file:
        file.writelines(filtered_lines)

##
# Conver unix2dos files
#
# @param source: source filename
# @param output: output filename
##
def convert2Dos(source,output):
    with open(source, 'r') as file:
        unix_lines = file.readlines()

    dos_lines = [line.rstrip('\n') + '\r\n' for line in unix_lines]

    with open(output, 'w') as file:
        file.writelines(dos_lines)


##
# Concatenate Bas files
#
# @param files: list files separate with ","
# @param output: output filename
##
def concatBasFiles(files, output):
    ficheros = files.split(',')

    with open(output, 'w') as salida:
        for fichero in ficheros:
            nombre_fichero = fichero.strip()
            with open(nombre_fichero, 'r') as archivo:
                contenido = archivo.read()
                salida.write(contenido)
            os.remove(nombre_fichero)


