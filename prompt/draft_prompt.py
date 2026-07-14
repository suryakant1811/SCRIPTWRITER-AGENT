def get_draft_prompt(user_value):
    return f"""
        Your task is to write the FIRST draft of a YouTube script. 
            Requirements:
            - Write in simple English.
            - Keep the information accurate.
            - Organize the script into clear paragraphs.
            - Do not use emojis.
            - Do not convert it to Hinglish.
            - Do not make it overly engaging.
            - Focus only on creating a clean first draft.
            Topic: {user_value}
    """