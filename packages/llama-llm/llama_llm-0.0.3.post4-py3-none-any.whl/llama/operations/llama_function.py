
from llama.operations.make_program import make_program

import inspect

def function(function):
    signature = inspect.signature(function)
    input_spec = next(iter(signature.parameters.values())).annotation
    return make_program(function(input_spec))

