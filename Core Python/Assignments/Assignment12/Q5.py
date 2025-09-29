def count_vowels():
    input_str = input("Enter String:")
    vowels = ['a' ,'e' , 'i' , 'o' ,'u']
    
    count = 0
    for i in input_str:
        if(i in vowels):
            count += 1
    print(count)
    
count_vowels()

    