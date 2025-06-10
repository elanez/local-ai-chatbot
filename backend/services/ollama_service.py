import ollama
from typing import List, Dict

class OllamaService:
    def __init__(self, host: str = "http://localhost:11434"):
        self.client = ollama.Client(host=host)

    def get_available_models(self) -> List[Dict]:
        try:
            models = self.client.list()
            return models.get('models', [])
        except Exception as e:
            print(f"Error fetching models from Ollama: {e}")
            return []

    def chat_completion(self, model: str, messages: List[Dict], stream: bool = False):
        try:
            response = self.client.chat(model=model, messages=messages, stream=stream)
            return response
        except Exception as e:
            print(f"Error during chat completion with Ollama: {e}")
            raise 