import json
import subprocess
import shutil
import os
import sys
from jinja2 import Template
from .common import messageInfo, getFileExt, messageError

def rvm_web(cpc, dsk,run, project,file_html):
    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    context = {
        'cpc': cpc,
        'dsk': dsk,
        'run': run,
        'project': project
    }

    with open(APP_PATH +"/templates/cpc.j2", 'r') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(context)
    with open(file_html, 'w') as file:
        file.write(rendered_template)

    messageInfo(getFileExt(file_html) + f"[green] ==> [/green]Create CPC Retro Virtual Machine Web")



def rvm_desktop(cpc, dsk,run, project,rvm_path):
    FNULL = open(os.devnull, 'w')
    try:
        retcode = subprocess.Popen([rvm_path,"-i", dsk,"-b=cpc"+str(cpc),"-c="+run + "\n"], stdout=FNULL, stderr=subprocess.STDOUT)
        messageInfo(f"Retro Virtual Machine [green]==> [/green]Launch")
        return True
    except:
        messageError(f"Error launching {dsk} on RetroVirtualMachine")
        return False
        
    