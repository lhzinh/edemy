from typing import Literal
from langgraph.graph import StateGraph, START, END

from bot.states import MessagesState
from bot.nodes import llm_call, tool_node


def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]
    
    if last_message.tool_calls:
        return "tool_node"
    
    return END


agent_builder = StateGraph(MessagesState)

agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
agent_builder.add_edge("tool_node", "llm_call")

agent = agent_builder.compile()

from IPython.display import Image, display

display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

from langchain.messages import HumanMessage

messages = [HumanMessage(content="What are my recent courses?")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()