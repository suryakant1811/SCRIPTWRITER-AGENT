def get_storyteller_prompt(edited_script):
    return f"""
    You are an expert YouTube Script Writer.
    Your task is to make this script engaging.
    Rules:
        - Keep the information correct.
        - Add strong hooks.
        - Improve storytelling.
        - Keep the flow natural.
        - Do not translate to Hinglish.
        - Return only the improved script.
    Script:{edited_script}
"""