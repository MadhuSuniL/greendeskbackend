from textblob import TextBlob
from difflib import ndiff
import random
# import spacy
# from spacy import displacy
# # Download the required NLTK data
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# nlp = spacy.load("en_core_web_lg")

def total_words(text):
    return len(text.split(' '))

def total_different_words(text):
    return len(set(text.split(' ')))
    
def sentences_count(text):
    return len(text.split('. '))    

def length(text):
    return len(text)

def calculate_average_word_length(character_count, total_words_with_duplicates):
    return character_count / total_words_with_duplicates if total_words_with_duplicates != 0 else 0

def calculate_duplicate_percentage(total_words_with_duplicates, unique_words_count):
    return (total_words_with_duplicates - unique_words_count) / total_words_with_duplicates * 100 if total_words_with_duplicates != 0 else 0

def calculate_unique_word_length(character_count, unique_words_count):
    return character_count / unique_words_count if unique_words_count != 0 else 0

def calculate_characters_per_word(character_count, total_words_with_duplicates):
    return character_count / total_words_with_duplicates if total_words_with_duplicates != 0 else 0

def calculate_words_per_sentence(total_words_with_duplicates, sentences_count):
    return total_words_with_duplicates / sentences_count if sentences_count != 0 else 0

def calculate_characters_per_sentence(character_count, sentences_count):
    return character_count / sentences_count if sentences_count != 0 else 0

def calculate_average_sentence_length(words_per_sentence, sentences_count):
    return words_per_sentence if sentences_count != 0 else 0


def calculate_characters_per_word_unique(character_count, unique_words_count):
    return character_count / unique_words_count if unique_words_count != 0 else 0



def text_operations(text):
    # Variables
    character_count = length(text)
    total_words_with_duplicates = total_words(text)
    unique_words_count = total_different_words(text)
    total_sentences = sentences_count(text)  
    
    # Additional operations
    average_word_length = calculate_average_word_length(character_count, total_words_with_duplicates)
    duplicate_percentage = calculate_duplicate_percentage(total_words_with_duplicates, unique_words_count)

    # More operations
    unique_word_length = calculate_unique_word_length(character_count, unique_words_count)
    characters_per_word_with_duplicates = calculate_characters_per_word(character_count, total_words_with_duplicates)

    # Additional operations
    words_per_sentence = calculate_words_per_sentence(total_words_with_duplicates, total_sentences)
    average_sentence_length = calculate_average_sentence_length(words_per_sentence, total_sentences)
    characters_per_word_unique = calculate_characters_per_word_unique(character_count, unique_words_count)
    
    text_variations = [
        f"The given text is <b class = 'text-2xl'>{character_count}</b> characters long. It has {total_words_with_duplicates} words with duplicates and {unique_words_count} words without duplicates. The average word length is {average_word_length:.2f} characters. {duplicate_percentage:.2f}% of the words are duplicates in the text.",
        
        f"This text is <b class = 'text-2xl'>{character_count}</b> characters long. It consists of {total_words_with_duplicates} words with repetitions and {unique_words_count} distinct words. On average, each word with duplicates is {characters_per_word_with_duplicates:.2f} characters long. The average length of unique words is {unique_word_length:.2f} characters.",
        
        f"The text has <b class = 'text-2xl'>{character_count}</b> characters, with {total_words_with_duplicates} words (including duplicates) and {unique_words_count} unique words. There are approximately {total_sentences} sentences in the text. On average, there are {words_per_sentence:.2f} words per sentence.",
        
        f"So, the text here is <b class = 'text-2xl'>{character_count}</b> characters long. It has about {total_words_with_duplicates} words with repeats and approximately {unique_words_count} unique words. The average word length is {average_word_length:.2f} characters.",
                
        f"On average, each word with duplicates is {characters_per_word_with_duplicates:.2f} characters long. The text has <b class = 'text-2xl'>{character_count}</b> characters, with {total_words_with_duplicates} words (including duplicates) and {unique_words_count} unique words.",
        
        f"The given text is <b class = 'text-2xl'>{character_count}</b> characters long. It has {total_words_with_duplicates} words with duplicates and {unique_words_count} words without duplicates. The average word length is {average_word_length:.2f} characters.",
        
        f"The text has <b class = 'text-2xl'>{character_count}</b> characters, with {total_words_with_duplicates} words (including duplicates) and {unique_words_count} unique words. So, the text here is <b class = 'text-2xl'>{character_count}</b> characters long. It has about {total_words_with_duplicates} words with repeats and approximately {unique_words_count} unique words.",
        
        f"The text is <b class = 'text-2xl'>{character_count}</b> characters, with {total_words_with_duplicates} words (including duplicates) and {unique_words_count} unique words. The average sentence length is {average_sentence_length:.2f} words.",
        
        f"On average, each word with duplicates is {characters_per_word_with_duplicates:.2f} characters long. This text has a length of <b class = 'text-2xl'>{character_count}</b> characters. It includes {total_words_with_duplicates} words with repetitions and {unique_words_count} distinct words.",
        
        f"The average length of unique words is {unique_word_length:.2f} characters. The given text is <b class = 'text-2xl'>{character_count}</b> characters long. It has {total_words_with_duplicates} words with duplicates and {unique_words_count} words without duplicates.",
        
        f"So, the text here is <b class = 'text-2xl'>{character_count}</b> characters long. It has about {total_words_with_duplicates} words with repeats and approximately {unique_words_count} unique words. On average, there are {words_per_sentence:.2f} words per sentence.",
        
        f"The given text is <b class = 'text-2xl'>{character_count}</b> characters long. It has {total_words_with_duplicates} words with duplicates and {unique_words_count} words without duplicates. On average, each word with duplicates is {characters_per_word_with_duplicates:.2f} characters long.",
        
        f"The text has <b class = 'text-2xl'>{character_count}</b> characters, with {total_words_with_duplicates} words (including duplicates) and {unique_words_count} unique words. On average, there are {words_per_sentence:.2f} words per sentence.",
        
        f"The average word length is {average_word_length:.2f}. So, the text here is <b class = 'text-2xl'>{character_count}</b> characters long. It has about {total_words_with_duplicates} words with repeats and approximately {unique_words_count} unique words.",
    ]
    return text_variations[random.randint(0, len(text_variations)-1)]

def correct_text(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)

def find_corrected_words(original_text):
    corrected_text = correct_text(original_text)
    diff = ndiff(original_text.split(), corrected_text.split())
    wrong_words = [word[2:] for word in diff if word.startswith('+ ')]
    corrected_words = [word[2:] for word in diff if word.startswith('+ ')]
    corrections = [wrong +' --> '+ correct for wrong, correct in zip(wrong_words, corrected_words)]
    return corrected_text ,corrections
    # return corrected_text +'</br><u>Corrected words</u> : </br>'+ ',</br> '.join(corrected_words)
    