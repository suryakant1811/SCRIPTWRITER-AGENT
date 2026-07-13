from state import ContentState
import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

def editor(state: ContentState):
    raw_data = state['raw_script']
    prompt = f"""
    You are a professional editor.
    Improve the grammar, readability and sentence flow.
    Rules:
        - Do not change the meaning.
        - Do not add extra information.
        - Keep the structure.
        - Return only the edited script.
    Script: {raw_data}
    """

    response = llm.invoke(prompt)

    state["edited_script"] = response.content

    return state