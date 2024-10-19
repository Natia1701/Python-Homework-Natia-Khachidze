from random import randint

computer_number = randint(0, 100)
print(computer_number)

i = 0
while i < 10 :
    costumer_number = int(input("please write your number between 0 and 100 - "))
    if costumer_number == computer_number:
        print("You are winner!")
    elif costumer_number < computer_number:
        print("your number is low")
    else:
        print("your number is high")
    i+=1
print("Computer is winner!")