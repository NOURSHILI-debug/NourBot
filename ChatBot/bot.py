from .responses import get_intent_response
from .utils import preprocess_text
class ChatBot:
    def __init__(self, name="NourBot"):
        self.name=name
    def get_response(self, user_input):
        cleaned_input = preprocess_text(user_input)
        response=get_intent_response(cleaned_input)
        return response
