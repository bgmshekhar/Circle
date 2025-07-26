from config import AI_MODEL

def get_ai_explanation(text):
    """
    Gets an explanation from the configured AI model.
    """
    if AI_MODEL == "gemini":
        return "Getting explanation from Gemini..."
    elif AI_MODEL == "openai":
        return "Getting explanation from OpenAI..."
    else:
        return "Unknown AI model configured."