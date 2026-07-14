from state import ContentState
from prompt.draft_prompt import get_draft_prompt
from llm import llm


def generate_draft(state: ContentState):
    user_request = state["messages"][-1].content
    prompt = get_draft_prompt(user_request)

    response = llm.invoke(prompt)

    state["raw_script"] = response.content
    print("Currently in 1 node")
    return state