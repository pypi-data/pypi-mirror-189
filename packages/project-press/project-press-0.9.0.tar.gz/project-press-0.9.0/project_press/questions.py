import os
import shutil
import sys

import jinja2
from boltons import fileutils
from prompt_toolkit import prompt as user_input
from prompt_toolkit.validation import ValidationError, Validator

from . import template
from .utils import get_jinja_env, var2bool


def validate_answer(text, schema):
    """
    Validate the answer and return modified answer if needed.
    """
    # Handle nullable first to remove conditionals below
    nullable = schema.get("nullable", False)
    if text is None:
        if nullable:
            return True, ""
        else:
            raise ValidationError(message="Answer is required")

    default = schema.get("default")
    if text == "":
        if default is not None:
            return True, default
        else:
            raise ValidationError(message="Answer is required")

    vartype = schema.get("type", "string")
    if vartype == "boolean":
        try:
            return True, var2bool(text)
        except ValueError:
            raise ValidationError(message="Answer must be a boolean (true/false, yes/no)") from None

    if vartype == "string":
        min_length = schema.get("minLength", None)
        if min_length and len(text) < min_length:
            raise ValidationError(message=f"Answer cannot be shorter than {min_length} characters")

        max_length = schema.get("maxLength", None)
        if max_length and len(text) > max_length:
            raise ValidationError(message=f"Answer cannot be longer than {max_length} characters")

    return True, text


def get_answer(text, schema):
    default = schema.get("default")
    if text == "":
        if default is not None:
            return default
    return text


def stdin_input(prompt):
    """
    Convenience function in order to be mocked
    """
    return input(prompt)


def prompt_question(question):
    """
    Ask the question until it is answered or canceled
    """
    # Get question details
    name = question["name"]
    prompt = question["prompt"] + ": "
    description = question.get("description")
    schema = question.get("schema", {})

    def validate_answer_first(x, schema):
        return validate_answer(x, schema)[0]

    validator = Validator.from_callable(lambda x: validate_answer(x, schema))

    while True:
        try:
            if sys.stdin.isatty():
                answer = user_input(
                    prompt,
                    validator=validator,
                    bottom_toolbar=description,
                    validate_while_typing=False,
                )
            else:
                answer = stdin_input(prompt)
            _, answer = validate_answer(answer, schema)
            return name, answer

        except EOFError:
            # ctrl-d was used, don't set default if string
            try:
                _, answer = validate_answer(None, schema)
                return name, answer
            except ValidationError:
                continue


def prepare_question(question, env, ctx):
    """
    Determine if the question is to be asked, and
    if so, build a prompt
    Return true if question is to be asked.
    """

    def templatize(what):
        if isinstance(what, str):
            return env.from_string(what).render(**ctx)
        return what

    # Get question details
    schema = question.get("schema", {})

    # Will we prompt this question?
    when = question.get("when")
    when = templatize(when)
    if when is not None:
        when = var2bool(when)
        question["when"] = when
        if not when:
            return False

    # Build default
    default = schema.get("default")
    default = templatize(default)
    if default is not None:
        vartype = schema.get("type", "string")
        if vartype == "boolean":
            default = var2bool(default)
        schema["default"] = default

    # Build prompt
    name = question["name"]
    if default is None:
        question["prompt"] = name
    else:
        question["prompt"] = f"{name} [{default}]"
    return True


def prompt_questions(questions):
    """
    For every question in the input file, ask the question
    and record the answer in the context

    Fills in `questions`
    """
    env = get_jinja_env()
    ctx = {}

    for question in questions:
        if not prepare_question(question, env, ctx):
            continue

        name, answer = prompt_question(question)
        if name is not None:
            question["value"] = answer
            ctx[name] = answer

    return ctx
