from langgraph.graph import MessagesState

class ContentState(MessagesState):
    raw_script: str
    edited_script: str
    formatted_script: str
    hinglish_script: str
