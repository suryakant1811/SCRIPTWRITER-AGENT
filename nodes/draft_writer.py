from state import ContentState
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

def generate_draft(state: ContentState):
    user_request = state["messages"][-1].content
    prompt = f"""
    Write a high-quality first draft of a script based on the user's request.
    Requirements:   
    - Start with a strong hook.
    - Organize the content logically.
    - Keep the language engaging.
    - End with a conclusion or CTA. 

    User_request: {user_request}
    """

    response = llm.invoke(prompt)

    state["raw_script"] = response.content

    return state