
from llama.engine.hyper_llama_engine import get_engine

def get_input(input):
    return get_engine().get_input(input)


