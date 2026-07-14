def get_editor_prompt(draft_script):
    return f"""
    You are a professional editor.
    Improve the grammar, readability and sentence flow.
    Rules:
        - Do not change the meaning.
        - Do not add extra information.
        - Keep the structure.
        - Return only the edited script.
    Script:{draft_script}
"""