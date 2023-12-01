import random
from sources.general_chat_bot_response import get_chatbot_response
from .answering_2nd import answer_2nd
from .answering_1st import answer_1st
from .parawise import para_wise
from sources.patterns import (chatbot_responses, engine_response_patterns, incomplete_responses,
    user_game_requests)

question_length = 3

def filter_answer(data):
    key = data.get('key')
    value = data.get('value')
    speak = data.get('value')
    images = data.get('images',[])
    status = data.get('status')
    if value:            
        if key in value or key.title() in value:
            value = value.replace(key, f'<span class="text-green-300 font-extrabold text-md">{key}</span>',1)
            value = value.replace(key.title(), f'<span class="text-green-300 font-extrabold font-mono text-md">{key.title()}</span>',1)        
        try:
            value = para_wise(value, images)
        except Exception as e:  
            raise e
    data = {
        'key':key,
        'value':value,
        'speak' : speak,
        'images':images,
        'status' : status
    }    
    return data

def is_question(sentence):
    sentence = sentence.strip().lower()
    if sentence.endswith('?'):
        return True
    question_words = ('who', 'what', 'when', 'where', 'why', 'how')
    return any(sentence.startswith(word) for word in question_words)    

def get_answer_from_1st(key):
    return answer_1st(key)

def get_answer_from_2nd(key):
        return answer_2nd(key)

def is_asking_game(key):
    if key in user_game_requests:
        data = {
            'mode' : 'game',
            'key': key,
            'value': '',
            'status': True
        }
        return data
    return None

def get_answer(key):
    data = get_chatbot_response(key)
    if data is not None:
        return data
        # return filter_answer(data)
    res = is_asking_game(key)
    if res is not None:
        return res
    
    if is_question(key):
        try:
            data = get_answer_from_2nd(key)
        except:
            data = get_answer_from_1st(key)
            value = data.get('value')
            if not value:
                random.shuffle(chatbot_responses)
                value = random.choice(chatbot_responses) +' '+ random.choice(engine_response_patterns)
                data = {
                    'key': key,
                    'value': value,
                    'status': False
                }
        data = filter_answer(data)        
        return data
    data = get_answer_from_1st(key)
    value = data.get('value')
    if not value:
        try:
            if len(key.split()) >= question_length:
                data = get_answer_from_2nd(key)    
                return data
            random.shuffle(incomplete_responses)
            value = random.choice(incomplete_responses)
            data = {
                'key': key,
                'value': value,
                'status': True
            }
            return data
        except:
            random.shuffle(chatbot_responses)
            value = random.choice(chatbot_responses)+' ' + random.choice(engine_response_patterns)
            data = {
                'key': key,
                'value': value,
                'status': False
            }
    data = filter_answer(data)        
    return data

