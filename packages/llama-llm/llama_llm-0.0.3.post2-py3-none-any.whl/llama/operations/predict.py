from llama.engine.hyper_llama_engine import get_engine

def predict(input, output_spec):
    return get_engine().run(input, output_spec)

