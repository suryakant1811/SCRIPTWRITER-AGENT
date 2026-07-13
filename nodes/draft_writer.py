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
        Your task is to write the FIRST draft of a YouTube script. 
            Requirements:
            - Write in simple English.
            - Keep the information accurate.
            - Organize the script into clear paragraphs.
            - Do not use emojis.
            - Do not convert it to Hinglish.
            - Do not make it overly engaging.
            - Focus only on creating a clean first draft.

            Topic: {user_request}
    """

    response = llm.invoke(prompt)

    state["raw_script"] = response.content

    return state