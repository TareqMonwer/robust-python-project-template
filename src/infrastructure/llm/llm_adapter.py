from src.infrastructure.llm.prompts import ORCHESTRATOR_PROMPT_TEMPLATE
from src.infrastructure.llm.models import OllamaMessage, OllamaChatResponseEnum
from src.infrastructure.llm.llm_client import LLMClient
from src.core.constants import (
    INTENT_CLASSIFICATION_MODEL,
    CAR_RECOMMENDATION_AGENT,
    GENERAL_CHAT_AGENT,
)


class LLMAdapter:
    """
    Adapter to interact with Ollama for intent classification.
    """

    def __init__(self, llm_client: LLMClient = None):
        self.llm_client = llm_client or LLMClient()

    def get_intents(self) -> list[str]:
        """Returns the list of supported intents."""
        return [CAR_RECOMMENDATION_AGENT, GENERAL_CHAT_AGENT]

    def classify_intent(self, message: str) -> str:
        """
        Classifies user intent using Ollama's LLM.

        Args:
            message (str): User input message.

        Returns:
            str: Identified intent.
        """
        prompt = ORCHESTRATOR_PROMPT_TEMPLATE.format(message=message)
        request_message = OllamaMessage(role="user", content=prompt)

        response = self.llm_client.chat(
            model=INTENT_CLASSIFICATION_MODEL, messages=[request_message]
        )

        if not response:
            return (
                GENERAL_CHAT_AGENT
            )

        response_body = response.get(OllamaChatResponseEnum.MESSAGE.value, {})
        resp_message = OllamaMessage(
            content=response_body.get(
                OllamaChatResponseEnum.CONTENT.value, ""
            ).strip(),
            role=response_body.get(
                OllamaChatResponseEnum.ROLE.value, "assistant"
            ),
        )

        intent = resp_message.content

        return intent if intent in self.get_intents() else GENERAL_CHAT_AGENT
