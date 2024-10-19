from random import randint
number_1 = randint(0,10)
number_2 = randint(0,10)

print(f"first number is", number_1, "second number is", number_2)

if number_2 < number_1:
    sum = 0
    for i in range (number_2, number_1+1):
        sum = sum + i
    print(f"sum of numbers between given numbers equals", sum)
else:
    sum = 0
    for i in range (number_1, number_2+1):
        sum = sum + i
    print(f"sum of numbers between given numbers equals", sum)  
        