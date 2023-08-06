
from llama.engine.hyper_llama_engine import get_engine

def fit(examples):
    return get_engine().fit(examples)


