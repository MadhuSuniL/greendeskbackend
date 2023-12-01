import random

def para_wise(text, images = []):
    collected_images = []
    for i in range(len(images)):
        print(images[i])
    para_length = 830
    para_range = range(para_length-100 ,len(text))
    final_paras_list = []
    random_img = None
    while True:
        if len(text) >= para_length:
            para = ''
            index = 0
            for char in text:
                try:
                    first = text[index-1].isnumeric()
                    second = text[index+1].isnumeric()
                except:
                    first = False
                    second = False
                if len(para) in para_range and char == '.' and (not first and not second):
                    classes = f'"rounded-lg shadow-green-300 shadow-2xl"'
                    div_classes = f"max-w-[300px] max-h-[300px] px-3 opacity-70"
                    while len(images):
                        random_img = f"{random.choice(images)}"
                        if random_img not in collected_images:
                            collected_images.append(random_img)
                            break
                    if random_img:                    
                        final_paras_list.append(para+'.'+f'<center><div class={div_classes}><img src={random_img} class={classes}/></div></center>')
                    else:
                        final_paras_list.append(para+'.')
                    text = text.replace(para+'.', '')
                    
                    break
                else:
                    para += char
                
                index += 1
                    
            # break
        else:
            final_paras_list.append(text)
            break
            
    final_text = '<br><br>&nbsp;&nbsp;&nbsp;&nbsp;'.join(final_paras_list)
    
    return '&nbsp;&nbsp;&nbsp;&nbsp;'+final_text
    
    
    
 