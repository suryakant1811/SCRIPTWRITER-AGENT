from state import ContentState
from prompt.translator_prompt import get_translator_prompt
from llm import llm



def translator(state: ContentState):
    formatted_script = state["formatted_script"]
    prompt = get_translator_prompt(formatted_script)

    response = llm.invoke(prompt)
    state["hinglish_script"] = response.content
    print("Currently in 4 node")
    return state
