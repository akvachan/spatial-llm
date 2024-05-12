from abc import ABC, abstractmethod
from prompt import Prompt


class LanguageModel(ABC):
    """
    Abstract base class for custom implementation of a language model.
    """

    @property
    def model_name(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    @abstractmethod
    def generate_response(self, user_message: Prompt) -> str:
        ...

    @staticmethod
    @abstractmethod
    def encode(string: str) -> list[int]:
        ...

    @staticmethod
    @abstractmethod
    def decode(tokens: list[int]) -> str:
        ...




