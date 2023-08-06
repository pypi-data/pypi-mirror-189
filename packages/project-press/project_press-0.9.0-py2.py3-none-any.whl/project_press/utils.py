from jinja2 import Environment, StrictUndefined


def get_jinja_env():
    env = Environment()
    env.undefined = StrictUndefined
    return env


def var2bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return bool(value)

    lvalue = value.lower().strip()
    if lvalue in ["true", "tru", "tr", "t", "yes", "y"]:
        return True
    if lvalue in ["false", "fals", "fal", "fa", "f", "no", "n"]:
        return False
    raise ValueError(f"Expected boolean value, got '{value}' instead.")
