missing_numbers = [] 
one_to_hundred = set(range(1, 101))


with open('one_hundred.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    lines = content.splitlines()

    for line in lines:
        for number_str in line.split():
            number = int(number_str)
            if number in one_to_hundred:
                one_to_hundred.remove(number)
            missing_numbers = list(one_to_hundred)

missing_numbers.sort()


with open('one_hundred_sorted.txt','w', encoding = 'utf-8') as file:
    for number in missing_numbers:
        file.write(str(number) + '\n')
    
    


    
    
        

        





        




