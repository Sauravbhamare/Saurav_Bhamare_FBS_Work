def remove_occurence(li,ele):
    result = []
    for i in li:
        if(i != ele):
            result.append(i)
    return result

li = [1,2,3,4,5,2,6,2,1]
element = int(input("Enter element:"))

new_li = remove_occurence(li,element)

print("Original list:",li)
print(f"List after removing all occurences of {element}:",new_li)
            