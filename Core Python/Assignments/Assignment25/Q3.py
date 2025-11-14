import re

def count_words(text):
    
    words= re.findall(r'\w+',text.lower())
    
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


text = '''Python is user friendly language.
Python is easy to learn.We use python in data Science.'''

result = count_words(text)
print("Word Frequency:")
for word, count in result.items():
    print(f'{word}:{count}')