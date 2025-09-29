def bubble_sort(li):
    n = len(li)
    for i in range(n):
        for j in range(0,n-i-1):
            if(li[j] > li[j+1]):
                li[j], li[j+1] = li[j+1],li[j]
                
                
def find_second_largest(li):
    bubble_sort(li)
    largest_ele = li[-1]
    for i in range(len(li) -2, -1 ,-1):
        if(li[i] != largest_ele):
            return li[i]
        
        
li = [10,20,4,45,99,23]

bubble_sort(li)
print("Sorted list is:",li)
    