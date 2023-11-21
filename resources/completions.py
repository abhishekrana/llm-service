from abc import ABC, abstractmethod

from pydantic import BaseModel


class Messages(BaseModel):
    role: str
    content: str


class CompletionsReq(BaseModel):
    model: str = "llama2"
    messages: list[Messages]


class CompletionsResp(BaseModel):
    content: str


class ICompletions(ABC):

    @abstractmethod
    def create(self, request: CompletionsReq) -> CompletionsResp:
        pass
