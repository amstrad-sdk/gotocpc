import click
import os
import sys
import configparser

from .common import consoleMessage, ConsoleColor, checkProjectValue, removeComments, convert2Dos, concatBasFiles
from .project import readProjectIni


@click.command()
@click.option('-f', '--file', required=False, help='Input file name')
@click.option('-m', '--mode', type=click.Choice(['0', '1', '2']), default='0', help='Image Mode')
def main(file, mode):
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    PWD = os.getcwd() + "/"
    PROJECT_FILE = "project.ini"

    # check if the project.ini file necessary for the execution of the program exists
    if not os.path.isfile(PROJECT_FILE):
        print(consoleMessage("\nERROR: The " + PROJECT_FILE + " file does not exist.", ConsoleColor.RED))
        sys.exit(1)

    ##
    # Define Variables
    ##
    config = configparser.ConfigParser()
    PROJECT_DATA = readProjectIni(PROJECT_FILE)
    PROJECT_NOT_SECTIONS = ["PROJECT", "CONCATENATE", "RVM"]
    PROJECT_NAME = PROJECT_DATA.get('PROJECT', {}).get('name')
    PROJECT_CONCAT_SOURCE = PROJECT_DATA.get('CONCATENATE', {}).get('source')
    PROJECT_CONCAT_OUT = PROJECT_DATA.get('CONCATENATE', {}).get('out')
    PROJECT_RVM_SYSTEM = PROJECT_DATA.get('RVM', {}).get('system')
    PROJECT_RVM_MODEL = PROJECT_DATA.get('RVM', {}).get('model')
    PROJECT_RVM_RUN = PROJECT_DATA.get('RVM', {}).get('run')
    PROJECT_BAS_FILE_1 = PROJECT_DATA.get('BAS_FILES', {}).get('file_1')
    PROJECT_DISC = "disc"

    ##
    # Check the project values
    ##

    checkProjectValue("Project --> name", PROJECT_NAME)
    checkProjectValue("Project --> system", PROJECT_RVM_SYSTEM)
    checkProjectValue("Project --> model", PROJECT_RVM_MODEL)
    checkProjectValue("Bas Files --> file_!", PROJECT_BAS_FILE_1)

    ##
    # Check the disc folder
    ##
    if not os.path.exists(PROJECT_DISC):
        os.makedirs(PROJECT_DISC)

    config.read(PROJECT_FILE)

    for section in config.sections():
        if section not in PROJECT_NOT_SECTIONS:
            for key, value in config.items(section):
                # BAS FILE PROCESSING
                if section.upper() == "BAS_FILES":
                    if not os.path.isfile(f"src/{value}"):
                        print(
                            consoleMessage(f"\nERROR: The src/{value} file does not exist.", ConsoleColor.RED))
                        sys.exit(1)
                    removeComments(f"src/{value}", f"disc/{value}")
                    convert2Dos(f"disc/{value}", f"disc/{value}")

    if PROJECT_CONCAT_SOURCE != "" and PROJECT_CONCAT_SOURCE is not None:
        concatBasFiles(PROJECT_CONCAT_SOURCE, PROJECT_CONCAT_OUT, PROJECT_DISC)
        convert2Dos(f"disc/{PROJECT_CONCAT_OUT}", f"disc/{PROJECT_CONCAT_OUT}")
    else:
        section = consoleMessage(f"[BAS_FILES]:", ConsoleColor.BLUE)
        message = consoleMessage("[warning] Not concat files.", ConsoleColor.YELLOW)
        print(section + message)


if __name__ == '__main__':
    main()
