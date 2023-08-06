from pydantic import Field

def Context(description: str):
    return Field(description=description)
