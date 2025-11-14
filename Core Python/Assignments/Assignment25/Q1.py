import re

def replace_occurence(text,forbidden_words):
    for word in forbidden_words:
        pattern = re.compile(re.escape(word))
        text = pattern.sub('*'*len(word),text)
    return text
    
    
if(__name__ == '__main__'):
    sample_text ="This movie is bad and worst"
    forbidden_words = ["bad","worst"]
    
    result = replace_occurence(sample_text,forbidden_words)
    print("Original Text:", sample_text)
    print("Forbidden_Text:",result)