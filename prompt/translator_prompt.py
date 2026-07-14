def get_translator_prompt(engaging_script):
    return f"""
    You are an expert Hindi content creator.
    Convert this script into natural Hinglish.
    Rules:
        - Keep the meaning exactly the same.
        - Make it conversational.
        - Use simple Hinglish.
        - Do not remove any information.
        - Return only the Hinglish script.
    Script:{engaging_script}
"""