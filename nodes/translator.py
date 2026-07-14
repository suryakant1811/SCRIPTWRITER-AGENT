import os 
from dotenv import load_dotenv
load_dotenv()
from state import ContentState
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt.translator_prompt import get_translator_prompt,   get_translator_promptget_translator_prompt
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)   

def translator(state: ContentState):
    formatted_script = state["formatted_script"]
    prompt = get_translator_prompt(formatted_script)

    response = llm.invoke(prompt)
    state["hinglish_script"] = response.content

    return state
    
        - Keep the meaning exactly the same.
        - Make it conversational.
        - Use simple Hinglish.
        - Do not remove any information.
        - Return only the Hinglish script.
    Script:{formatted_script}    
"""

    response = llm.invoke(prompt)
    state["hinglish_script"] = response.content

    return state

    