from random import randint
word = input("please type your word - ")
number = randint(0,10)
print(f"number is ", number)
i = 0
while i < number:
    print(word)
    i+=1