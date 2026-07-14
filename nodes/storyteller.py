import os
from dotenv import load_dotenv
load_dotenv()
from state import ContentState

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

def storytellar(state: ContentState):
    edited_script = state["edited_script"]
    prompt = f"""
        You are an expert YouTube Script Writer.
        Your task is to make this script engaging.
        Rules:
            - Keep the information correct.
            - Add strong hooks.
            - Improve storytelling.
            - Keep the flow natural.
            - Do not translate to Hinglish.
            - Return only the improved script.

        Script: {edited_script}
    """

    result = llm.invoke(prompt)
    state["formatted_script"] = result.content

    return state