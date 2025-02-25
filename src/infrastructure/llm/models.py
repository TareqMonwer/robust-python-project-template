from enum import Enum


class OllamaMessage:
    """
    Represents a message structure for Ollama's chat API.
    """

    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def __iter__(self):
        yield "role", self.role
        yield "content", self.content


class OllamaChatResponseEnum(Enum):
    """Enum for handling chat response keys."""

    MESSAGE = "message"
    CONTENT = "content"
    ROLE = "role"
