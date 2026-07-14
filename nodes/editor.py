from state import ContentState
from prompt.editor_prompt import get_editor_prompt
from llm.llm import get_llm

llm = get_llm()

def editor(state: ContentState):
    raw_data = state['raw_script']
    prompt = get_editor_prompt(raw_data)

    response = llm.invoke(prompt)

    state["edited_script"] = response.content

    return state