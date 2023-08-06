
from llama.engine.hyper_llama_engine import get_engine

def get_field(input, field_name):
    return get_engine().get_field(input, field_name)

