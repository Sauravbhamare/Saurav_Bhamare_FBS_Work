def count_word_freq(str):
    words = str.split()
    frequency = {}
    
    
    for word in words:
        if(word in frequency):
            frequency[word] += 1
        else:
            frequency[word] = 1
            
            
    return frequency

str = input("Enter String:")
result = count_word_freq(str)
print("Word Frequency:",result)