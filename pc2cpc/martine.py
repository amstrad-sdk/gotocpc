
import json
import subprocess
import click
import shutil
import os
import sys
from .common import consoleMessage, ConsoleColor, getFileExt

##
# Concar Bas files
#
# @param filename: list files separate with ","
# @param mode: output filename
# @param output: output filename
# @param dsk: True or false if the dsk file is generated
##
def img2scr(filename, mode, fileout, dsk):
    
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    TMP_FOLDER = fileout + "/f-"+os.path.basename(filename)
    TMP_FILE = os.path.basename(os.path.splitext(filename)[0])
    TMP_JSON = TMP_FOLDER + "/" + TMP_FILE+".json"
    
    if dsk:
        cmd = [SDK4BASIC_PATH + '/bin/martine', '-in', filename, '-mode', str(mode), '-out', TMP_FOLDER, '-json','-dsk']
    else:
        cmd = [SDK4BASIC_PATH + '/bin/martine', '-in', filename, '-mode', str(mode), '-out', TMP_FOLDER, '-json']
    
    try:
        if fileout:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            if not os.path.exists(fileout):
                os.makedirs(fileout)
            shutil.copy2(os.path.join(TMP_FOLDER, TMP_FILE.upper() + '.PAL'), fileout)
            shutil.copy2(os.path.join(TMP_FOLDER, TMP_FILE.upper() + '.SCR'), fileout)
        else:
            subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f'Error executing command: {e.output.decode()}')
        sys.exit(1)
        
    # Open JSON file
    with open(TMP_JSON) as f:
        data = json.load(f)

    # Get value of 'palette' key and convert to string
    sw_palette = str(data['palette'])
    hw_palette = str(data['hardwarepalette'])
    
    # Remove single quotes and brackets
    #sw_palette = sw_palette.replace("'", "").strip('[]')

    Message = consoleMessage("Image: ", ConsoleColor.WHITE) + consoleMessage(getFileExt(filename), ConsoleColor.YELLOW) + "\n" + \
              consoleMessage("  SW Palette: ", ConsoleColor.WHITE) + consoleMessage(sw_palette, ConsoleColor.YELLOW) + "\n" + \
              consoleMessage("  HW Palette: ", ConsoleColor.WHITE) + consoleMessage(hw_palette, ConsoleColor.YELLOW) + "\n" + \
              consoleMessage("  Out File  : ", ConsoleColor.WHITE) + consoleMessage(TMP_FILE.upper() + ".SCR", ConsoleColor.YELLOW)
    print(Message)
    if dsk:
        if not os.path.exists("dsk"):
            os.makedirs("dsk")
        shutil.copy2(os.path.join(TMP_FOLDER, TMP_FILE.upper() + '.DSK'), 'dsk/'+ TMP_FILE.upper() + '.DSK')
    # Delete temporary folder
    shutil.rmtree(TMP_FOLDER)

##
# Convert images to sprites C/ASM
#
# @param filename: list files separate with ","
# @param mode: output filename
# @param width: width image in pixels
# @param height: height image in pixels
# @param out: temporal folder
##
def img2spr(filename, mode, width, height, out):
    
    SDK4BASIC_PATH = os.environ.get('SDK4BASIC_PATH')
    TMP_FOLDER = out + "/f-"+os.path.basename(filename)
    ASM_FILE = os.path.basename(os.path.splitext(filename)[0])
    TMP_OBJ = TMP_FOLDER + "/" + ASM_FILE.upper()+".TXT"
    TMP_C = TMP_FOLDER + "/" + ASM_FILE.upper()+"C.TXT"
    OBJ_FOLDER = "obj/"
    TMP_JSON = TMP_FOLDER + "/" + ASM_FILE+".json"
    cmd = [SDK4BASIC_PATH + '/bin/martine', '-in', filename, '-width', str(width),'-height',str(height),'-mode', str(mode), '-out', TMP_FOLDER, '-json','-noheader']
    
    try:
        if out:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            if not os.path.exists(out):
                os.makedirs(out)
        else:
            subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f'Error executing command: {e.output.decode()}')
        sys.exit(1)

    if not os.path.exists(OBJ_FOLDER):
        os.makedirs(OBJ_FOLDER)
    
    only=0
    copy = False
    with open(TMP_C, 'r') as input_file:
        with open(OBJ_FOLDER + "/SPRITES.C", 'a') as output_file:
            if only == 0:
                output_file.write("array byte " + ASM_FILE + " = {\n")
                only = 1
            for line in input_file:
                if line.startswith('; width'):
                    copy = True
                    continue
                elif line.startswith('; Palette'):
                    copy = False
                    continue
                if copy:
                    output_file.write(line.replace("db ", "   "))
            output_file.write("};\n")
            
    only=0

    with open(TMP_OBJ, 'r') as input_file:
        with open(OBJ_FOLDER + "/SPRITES.ASM", 'a') as output_file:
            if only == 0:
                output_file.write(";------ BEGIN SPRITE --------\n")
                output_file.write(ASM_FILE)
                output_file.write("\ndb " + width + " ; ancho")
                output_file.write("\ndb " + height + " ; alto\n")
                only = 1
            for line in input_file:
                if line.startswith('; width'):
                    copy = True
                    continue
                elif line.startswith('; Palette'):
                    copy = False
                    continue
                if copy:
                    output_file.write(line)
            output_file.write("\n;------ END SPRITE --------\n")

    # Delete temporary folder
    shutil.rmtree(TMP_FOLDER)