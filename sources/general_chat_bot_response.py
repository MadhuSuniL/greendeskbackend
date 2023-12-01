from .patterns import chat_bot_data
import random


def get_chatbot_response(text):
    text = text.lower().replace('?','').strip()
    for obj in chat_bot_data:
        patterns = obj['patterns']
        if text in patterns:
            responses = obj['responses']
            return {
                'key' : text,
                'value' : random.choice(responses),
                'images' : [],
                'status' : True
            }
    return None