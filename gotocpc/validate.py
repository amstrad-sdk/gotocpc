import jsonschema
import yaml
from .common import messageError, messageInfo


def validate(file_proyect):
    schema = {
        "type": "object",
        "properties": {
            "Version": {"type": "string"},
            "kind": {"type": "string", "enum": ["cpc"]},
            "project": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "author": {"type": "string"}
                        },
                        "required": ["name", "author"]
                    },
                    "rvm": {
                        "type": "object",
                        "properties": {
                            "system": {
                                "type": "string",
                                "enum": ["web", "desktop"]
                            },
                            "model": {                                
                                "type": "integer",
                                "enum": [464, 6128,664]
                            },
                            "run": {"type": "string"},
                            "rvm_path": {"type": "string"}
                        },
                        "required": ["system", "model", "run","rvm_path"],
                        "dependencies": {
                            "system": {
                                "oneOf": [
                                    {"const": "desktop", "required": ["rvm_path"]},
                                    {"not": {"enum": ["desktop"]}}
                                ]
                            }
                        },
                    },
                    "concatenate": {
                        "type": "object",
                        "properties": {
                            "out": {"type": "string"}
                        },
                        "required": ["out"]
                    },
                    "m4board": {
                        "type": "object",
                        "properties": {
                            "publish": {"type": "boolean"},
                            "folder": {"type": "string"}
                        },
                        "required": ["publish", "folder"]
                    }
                },
                "required": ["data", "rvm", "concatenate", "m4board"]
            },
            "spec": {
                "type": "object",
                "properties": {
                    "files": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "kind": {"type": "string"},
                                "name": {"type": "string"},
                                "concat": {"type": "boolean"},
                                "address": {"type": "integer"},
                                "include": {"type": "string"},
                                "mode": {"type": "integer"},
                                "pal": {"type": "boolean"},
                                "width": {"type": "integer"},
                                "height": {"type": "integer"}
                            },
                            "required": ["kind", "name"]
                        }
                    }
                }
            }
        },
        "required": ["Version", "kind", "project", "spec"]
    }


    try:
        with open(file_proyect, "r") as yaml_file:
            yaml_content = yaml_file.read()

        data = yaml.safe_load(yaml_content)
        jsonschema.validate(data, schema)
        messageInfo(f"{file_proyect}[green] ==> [/green]Validated structure")
        return True
    except (FileNotFoundError, yaml.YAMLError, jsonschema.exceptions.ValidationError) as e:
        messageError(f'Error ' + file_proyect + f' The structure is not valid: {e}')
        return False
