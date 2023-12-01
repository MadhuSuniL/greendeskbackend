import wikipedia as wk

def answer_1st(word):
        if word == 'python' or word == 'Python':
            word = 'Python (programming language)'
        if word == 'C' or word == 'C programming':
            word = 'C Programming Language'   
        key = word
        try :
            page = wk.page(word,auto_suggest=True)
            value = page.summary
            images = page.images if page.images else []
            images =  [image for image in images if page.title in image and not image.endswith('.svg')]
        except:
            value = None 
            images = []
        try:
            extra = wk.search(word)
            if word in extra:
                extra.remove(word)
        except:
            extra = None
        if extra is not None:
            extras = 'You may search about these lines also...\n\n'
        try:
            if len(extra) > 6 and extra is not None:
                extra = extra[0:10]
        except:
            pass
        
        # if value and flag:            
        #     if key in value or key.title() in value:
        #         value = value.replace(key, f'<span class="text-white font-extrabold text-xl">{key}</span>',1)
        #         value = value.replace(key.title(), f'<span class="text-white font-extrabold font-mono text-xl">{key.title()}</span>',1)        
        #     try:
        #         value = para_wise(value, images)
        #     except Exception as e:
        #         raise e
        
        
        data = {
        'key':key,
        'value':value,
        'images':images,
        'status': True,
        'extra':extra
        }
        return data

