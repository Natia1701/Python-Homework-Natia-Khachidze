#პროგრამა ითვლის ერთი რანდომ რიცხვიდან მეორე შემთხვევით რიცხვამდე ჯამს, შემთხვევითი რიცხვები არის 0-დან 100-მდე

from random import randint
number_1 = randint(0, 100)
number_2 = randint(0, 100)

print(number_1)
print(number_2)

if number_1 <= number_2 :
    sum = 0
    for i in range(number_1, number_2):
        sum = sum + i
    print(sum)
else :
    sum = 0
    for i in range(number_2, number_1):
        sum = sum + i
    print(sum)