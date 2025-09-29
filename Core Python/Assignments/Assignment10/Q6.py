def Remove_Duplicate(li):
    new_li = []
    for i in li:
        if(i not in new_li):
            new_li.append(i)
    return new_li

li = [1,2,3,4,5,6,7,8,9,2,3]
result = Remove_Duplicate(li)

print("Original List:",li)
print("List after removing Duplicates:",result)