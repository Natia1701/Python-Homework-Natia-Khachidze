from random import randint
number = randint(0,1)
print(number)
if number == 0:
    i = 0
    sum = 0
    while i < 10:
        sum = sum + i
        i+=1
    print(f"The sum of numbers between 0 and 10 equals", sum)
else:
    sum = 0
    for i in range(0,10):
        sum = sum + i
    print(f"The sum of numbers between 0 and 10 equals", sum)
