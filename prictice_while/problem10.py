#მოთამაშეს აქვს 3 ცდა რომ გამოიცნოს საიდუმლო რიცხვი

from random import randint
secret_number = randint(0,10)
print(secret_number)
i = 0
while i < 3:
    costumers_number = int(input("Please, type your number less then 10 - "))
    if costumers_number == secret_number:
        print("Congratulations!!! You won!!!" )
        print("We are waiting you back soon, have a nice day")
    else:
        i+=1
print("You loose")
