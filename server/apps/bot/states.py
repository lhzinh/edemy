from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
from operator import add


class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add]
    llm_calls: int
    user_id: str