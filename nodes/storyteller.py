import os
from dotenv import load_dotenv
load_dotenv()
from state import ContentState
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt.storytellar_prompt import get_storyteller_prompt

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

def storytellar(state: ContentState):
    edited_script = state["edited_script"]
    prompt = get_storyteller_prompt(edited_script)

    result = llm.invoke(prompt)
    state["formatted_script"] = result.content

    return state