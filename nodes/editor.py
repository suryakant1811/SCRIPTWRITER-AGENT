from state import ContentState
import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt.editor_prompt import get_editor_prompt
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

def editor(state: ContentState):
    raw_data = state['raw_script']
    prompt = get_editor_prompt(raw_data)

    response = llm.invoke(prompt)

    state["edited_script"] = response.content

    return state