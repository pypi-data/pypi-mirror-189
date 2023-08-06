import json
import os
import sys

import cerberus
import yaml

from . import template
from .utils import get_jinja_env

# https://docs.python-cerberus.org/en/stable/validation-rules.html
SCHEMA = r"""
---
files:
  type: list
  default: []
  schema:
    type: dict
    default: {}
    nullable: true
    schema:
      path:
        type: string
        required: true
      when:
        type: [string, boolean]
      action:
        type: string
        required: true

questions:
  type: list
  default: []
  schema:
    type: dict
    default: {}
    nullable: true
    schema:
      name:
        type: string
        regex: '^\S+$'
        required: true
      description:
        type: string
      value:
        type: [string, boolean]
      when:
        type: [string, boolean]
      schema:
        type: dict
        default: {}
        nullable: true
        schema:
          type:
            type: string
            allowed: ["string", "boolean"]
          default:
            type: [string, boolean]
          nullable:
            type: boolean
            default: true
          minLength:
            type: integer
            min: 0
          maxLength:
            type: integer
            min: 0
"""


def validate_schema(args):
    """
    Validate the YAML part of the template
    """
    data = template.get_data(args.get("template", ""))
    schema = yaml.safe_load(SCHEMA)
    validator = cerberus.Validator(schema)
    if not validator.validate(data):
        sys.exit("error: YAML schema validation error. Location:\n" + str(json.dumps(validator.errors, indent=2)))
    return data


def validate_template_existance(args):
    template = args["template"]
    template = os.path.abspath(os.path.join(template, "template"))
    if not os.path.isdir(template):
        sys.exit(f'error: no "template" directory found in source template location')


def validate_templates(args, data):
    """
    Validate the contents of the YAML file and that the template dir exists
    """
    env = get_jinja_env()
    ctx = {}

    for file in data.get("files", []):
        action = file.get("action")
        if action not in ["remove"]:
            sys.exit(f'error: unknown file action "{action}"')

    for question in data.get("questions", []):
        schema = question.get("schema", {})
        default = schema.get("default")


def validate(args):
    data = validate_schema(args)
    validate_template_existance(args)
    validate_templates(args, data)
