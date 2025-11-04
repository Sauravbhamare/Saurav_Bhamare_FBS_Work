def word_string():
    text = input("Enter String:")
    
    words = text.split()
    
    short_words = [word for word in words if(len(word) < 5)]
    
    print("WOrds less than 5 letters:",short_words)
    
word_string()