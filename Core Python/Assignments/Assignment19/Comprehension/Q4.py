def remove_vowels():
    str1 = input("Enter String:")
    vowels = ['a','e','i','o','u']
    li = [vowel for vowel in str1 if vowel not in vowels]
    print(li)
remove_vowels()