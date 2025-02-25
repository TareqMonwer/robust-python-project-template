import ollama
from src.infrastructure.llm.models import OllamaMessage


class LLMClient:
    """
    Handles direct API calls to Ollama LLM.
    """

    def chat(self, model: str, messages: list[OllamaMessage]) -> dict:
        """
        Calls the Ollama chat API.

        Args:
            model (str): LLM model name.
            messages (list[OllamaMessage]): Messages to send.

        Returns:
            dict: Response from Ollama API.
        """
        try:
            response = ollama.chat(
                model=model, messages=[dict(msg) for msg in messages]
            )
            return response
        except Exception as e:
            print(f"⚠️ LLMClient Error: {e}")
            return {}
