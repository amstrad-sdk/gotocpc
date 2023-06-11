# from martine import img2spr
# from common import consoleMessage,ConsoleColor
# from idsk import createDskFile, addBinaryFileDsk
# from ccz80 import compile

# img2spr("/home/destroyer/Documentos/Github/SDK4BASIC/setup/src/pc2cpc/pc2cpc/screen.png","0","16","16","pepe")

# createDskFile("fffff.dsk")
# addBinaryFileDsk("fffff.dsk2","SCREEN.SCR")

# compile("dfasd","dsffasd")

import yaml

with open('project.yaml', 'r') as file:
    data = yaml.safe_load(file)

for file_data in data['spec']['files']:
    if file_data['kind'].upper() == 'BAS':
        print(file_data['file'])
    elif file_data['kind'].upper() == 'ASCII':
        print(file_data['file'])
    elif file_data['kind'].upper() == 'C':
        print(file_data['file'])
    elif file_data['kind'].upper() == 'IMAGE':
        print(file_data['file'])
    elif file_data['kind'].upper() == 'SPRITE':
        print(file_data['file'])
        
        