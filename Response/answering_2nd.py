from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re, requests, random
from nltk.stem import PorterStemmer
from googlesearch import search
from bs4 import BeautifulSoup


max_results = 10
samples = 5


def get_paras(url):
    para_list = []
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    paras = soup.find_all('p')
    if len(paras) > 1 and paras:
        for para in paras:
            if len(para.text) > 250 and para.text.endswith('.') and not para.text.endswith('?'):
                para_list.append(para.text)
        return para_list
    
    return False


def get_list_of_urls(results):
    urls = []
    for i, result in enumerate(results, start=1):
        urls.append(result.url)        
    return urls

def get_random_results(results,num_of_results):    
    random_results = []
    results = get_list_of_urls(results)
    while True:
        random_result = random.choice(results)
        if random_result not in random_results:
            random_results.append(random_result)
        if len(random_results) == num_of_results:
            break
    return random_results
        
def google_search(query, num_results=max_results):
    main_para_list = []
    results = search(term=query,advanced=True,num_results = num_results)
    for result in get_random_results(results,samples):
        paras = get_paras(result)
        if paras:
            main_para_list += paras                 
    return main_para_list

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

def find_related_paragraph(sentence, paragraphs):
    all_text = [preprocess_text(sentence)] + [preprocess_text(p) for p in paragraphs]
    vectorizer = TfidfVectorizer().fit_transform(all_text)
    similarity_matrix = cosine_similarity(vectorizer)
    most_similar_index = similarity_matrix[0, 1:].argmax() + 1
    return most_similar_index

def answer_2nd(question):
    all_paragraph_contexts = google_search(question,max_results)
    related_paragraph_index = find_related_paragraph(question, all_paragraph_contexts)
    value = all_paragraph_contexts[related_paragraph_index - 1]
    data = {
        'key': question,
        'value' : value,
        'status': True,
        'images' : []
    }    
    return data
