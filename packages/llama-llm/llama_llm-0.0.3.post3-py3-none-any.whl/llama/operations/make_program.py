from llama.engine.hyper_llama_engine import get_engine

def make_program(input):
    return get_engine().make_program(input)


