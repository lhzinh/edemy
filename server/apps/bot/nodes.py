from langchain.messages import SystemMessage, ToolMessage
from langchain_core.runnables import RunnableConfig

from bot.tools import model_with_tools, tools_by_name


def llm_call(state: dict):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            model_with_tools.invoke([SystemMessage(content="")] + state["messages"])
        ],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


def tool_node(state: dict, config: RunnableConfig):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"], config)
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}
