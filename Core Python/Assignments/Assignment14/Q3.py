def unique_word(s1):
    unique_wrd = set()
    frequency = {}

    for line in s1:
        words = line.split()
        for word in words:
            word = word.lower()
            unique_wrd.add(word)
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    return unique_wrd, frequency

s1 = [
    "apple banana apple",
    "banana orange",
    "orange banana apple"
]

unique, count = unique_word(s1)

print("Unique words:", unique)

print("\nWord frequencies:")
for word, freq in count.items():
    print(f"{word}: {freq}")
