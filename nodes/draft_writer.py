from state import ContentState
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt.draft_prompt import get_draft_prompt

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

def generate_draft(state: ContentState):
    user_request = state["messages"][-1].content
    prompt = get_draft_prompt(user_request)

    response = llm.invoke(prompt)

    state["raw_script"] = response.content

    return state