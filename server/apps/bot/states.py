from operator import add
from typing import Annotated

from langchain.messages import AnyMessage
from typing_extensions import TypedDict


class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add]
    llm_calls: int
    user_id: str
