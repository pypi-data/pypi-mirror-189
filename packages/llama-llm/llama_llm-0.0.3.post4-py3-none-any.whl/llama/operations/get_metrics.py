
from llama.engine.hyper_llama_engine import get_engine

def metrics():
    return get_engine().get_metrics()

