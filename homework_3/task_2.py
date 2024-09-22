import random

number = random.uniform(
    int(input("lower bound of interval-")), 
    int(input("upper bound of interval-"))
    )
print(number)

round = round(number, 1)
print(round)
