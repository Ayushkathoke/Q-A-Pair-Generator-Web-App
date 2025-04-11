from langchain_ollama.llms import OllamaLLM
import pydantic

class Conf(pydantic.BaseModel):
    model:OllamaLLM


config = Conf(
    model=OllamaLLM(model="llama3.2:latest")
)




