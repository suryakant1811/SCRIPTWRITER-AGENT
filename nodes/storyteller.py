from state import ContentState
from prompt.storytellar_prompt import get_storyteller_prompt
from llm.llm import get_llm

llm = get_llm()

def storytellar(state: ContentState):
    edited_script = state["edited_script"]
    prompt = get_storyteller_prompt(edited_script)

    result = llm.invoke(prompt)
    state["formatted_script"] = result.content

    return state