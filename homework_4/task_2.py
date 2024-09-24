import random
import math 

number = int(input("please enter positive integer less then 30: "))
if number > 0 and number < 30 :
    maximum_value = 0
    for n in range(number) :
        random_numbers = random.randint(0, 1000)
        if maximum_value <= random_numbers :
            maximum_value = random_numbers
    print(maximum_value)
else :
    print("please enter positive integer less then 30")



   

