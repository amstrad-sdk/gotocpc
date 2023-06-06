import os
import sys
from rich.console import Console
from rich.text import Text

console = Console()


class ConsoleColor:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


def messageWarning(ambito, file, message):
    console.print(
        "[bold blue]\[" + str(ambito) + "]:[/bold blue][bold yellow]\[" + str(file) + "] " + message + "[/bold yellow]")


def messageError(ambito, file, message):
    console.print(
        "[bold blue]\[" + str(ambito) + "]:\[" + str(file) + "][/bold blue][bold red] " + message + "[/bold red]")


def messageInfo(ambito, file, message):
    console.print(
        "[bold blue]\[" + str(ambito) + "]:\[" + str(file) + "][/bold blue][bold green] " + message + "[/bold green]")


def checkProjectValue(text, value):
    if value is None or value == "":
        messageError("VALIDATE", value, "The " + str(text) + " key does not exist or has no value.")
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
    global file
    if not os.path.exists(source):
        messageError("BAS_FILES", getFileExt(source), "The file does not exist.")
        endCompilation("ERROR")
        sys.exit(1)

    with open(source, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not line.startswith("1'") and not line.startswith("1 '")]

    with open(output, 'w') as file:
        file.writelines(filtered_lines)
    file = getFileExt(source)
    messageInfo("BAS_FILES", file, "File Comments Removed.")


##
# Conver unix2dos files
#
# @param source: source filename
# @param output: output filename
##
def convert2Dos(source, output):
    if not os.path.exists(source):
        messageError("BAS_FILES", getFileExt(source), "The file does not exist.")
        endCompilation("ERROR")
        sys.exit(1)
    with open(source, 'r') as file:
        unix_lines = file.readlines()

    dos_lines = [line.rstrip('\n') + '\r\n' for line in unix_lines]

    with open(output, 'w') as file:
        file.writelines(dos_lines)

    files = getFileExt(source)
    messageInfo("BAS_FILES", files, "Convert unix to dos.")


##
# Concatenate Bas files
#
# @param files: list files separate with ","
# @param output: output filename
##
def concatBasFiles(files, output, folder):
    if files != "":
        ficheros = files.split(',')
        folder = folder + "/"
        if os.path.exists(folder + output):
            os.remove(folder + output)
        with open(folder + output, 'a') as salida:
            for fichero in ficheros:
                nombre_fichero = fichero.strip()
                if os.path.exists(folder + nombre_fichero):
                    with open(folder + nombre_fichero, 'r') as archivo:
                        contenido = archivo.read()
                        salida.write(contenido)
                    os.remove(folder + nombre_fichero)
                    messageInfo("BAS_FILES", nombre_fichero, f"Concatenate in {output}.")
                else:
                    messageError("BAS_FILES", nombre_fichero, "The file does not exist.")
                    endCompilation("ERROR")
                    sys.exit(1)
    else:
        messageWarning("BAS_FILES", "Warning", "Not concat files.")


def endCompilation(type):
    console.print("\n[bold white]-------------------------------------------------------------- [/bold white]")
    if type == "OK":
        console.print("[bold green] BUILD SUCCESSFULLY [/bold green]")
    if type == "ERROR":
        console.print("[bold red] BUILD FAILURE [/bold red]")
    console.print("[bold white]-------------------------------------------------------------- [/bold white]")


def beginCompilation(project):
    console.print("\n[bold white]-------------------------------------------------------------- [/bold white]")
    console.print("[bold blue] PROJECT: [/bold blue][bold white]" + project + "[/bold white]")
    console.print("[bold white]-------------------------------------------------------------- [/bold white]")
