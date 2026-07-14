from langchain.chat_models import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )
    return llm