lst = [2, 4, 10, 42, 12, 0, 4, 7, 21, 4, 83, 8, 5, 6, 8, 234, 5, 6, 523, 42, 34, 0, 234, 1, 435, 465, 56, 7, 3, 43, 23]

lst_three = []

for num in lst:
    try:
        if 100 % num == 0:
            lst_three.append(num)      
    except ZeroDivisionError as e:
        
        print(e)
        continue
print(lst_three)