def even (main):
    list = []
    for num in main:
        if num % 2 == 0:
            list.append(str(num))
    new_list = "-".join(list)
    print(new_list)

list = [1,48,16,3]

even(list)






        
