import json
import subprocess
import shutil
import os
import sys
from jinja2 import Template
from .common import messageInfo, getFileExt

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

    messageInfo(getFileExt(file_html), f"Create Template HTML CPC {cpc} Machine Retrovirtual Machine.")
