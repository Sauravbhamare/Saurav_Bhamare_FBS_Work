def length_ele(li):
    li.sort(key=len)

li = ["apple", "banana", "kiwi", "fig", "pineapple", "pear"]
print("Original List:", li)
length_ele(li)
print("Sorted by Length:", li)
