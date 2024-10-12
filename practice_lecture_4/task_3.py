#პროგრამამ შეგვაყვანინოს რიცხვი და გამოიმუშაოს რანდომ რიცხვი. ჩვენს მიერ შეყვანილი რიცხვი დაბეჭდოს იმდენჯერ რაც იქნება რანდომ რიცხვი

from random import randint
number_1 = int(input("please enter number - "))
number_2 = randint(0, 45)
print("random number is " +str(number_2))
for i in range(number_2):
    print(number_1, end="   ")
